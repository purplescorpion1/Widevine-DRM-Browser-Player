from flask import Flask, request, Response
import requests
from xml.etree import ElementTree as ET
import os

app = Flask(__name__)

proxy_config = {}

@app.route('/')
def index():
    static_folder = os.path.join(os.path.dirname(__file__), 'static')
    file_path = os.path.join(static_folder, 'drm_proxy_player.html')
    if os.path.exists(file_path):
        return app.send_static_file('drm_proxy_player.html')
    else:
        return "File not found: drm_proxy_player.html", 404

@app.route('/set_proxy_config', methods=['POST'])
def set_proxy_config():
    global proxy_config
    proxy_config = request.get_json()
    app.logger.debug(f"Proxy config saved: {proxy_config}")
    return {"status": "success", "config": proxy_config}

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return "URL parameter is required", 400

    headers = {
        'User-Agent': request.headers.get('User-Agent', 'Mozilla/5.0'),
    }
    if proxy_config.get('referer'):
        headers['Referer'] = proxy_config['referer']
    if proxy_config.get('origin'):
        headers['Origin'] = proxy_config['origin']

    try:
        response = requests.get(url, headers=headers, stream=True, verify=False)
        response.raise_for_status()

        app.logger.debug(f"Proxy request to {url} returned status {response.status_code}")
        app.logger.debug(f"Response headers: {dict(response.headers)}")

        mpd_content = response.content.decode('utf-8')
        app.logger.debug(f"Original MPD content: {mpd_content}")

        base_uri = url.rsplit('/', 1)[0] + '/'
        root = ET.fromstring(mpd_content)
        for segment_template in root.findall('.//{urn:mpeg:dash:schema:mpd:2011}SegmentTemplate'):
            for attr in ['media', 'initialization']:
                if attr in segment_template.attrib:
                    relative_url = segment_template.attrib[attr]
                    segment_template.attrib[attr] = base_uri + relative_url

        modified_mpd = ET.tostring(root, encoding='utf-8', method='xml')
        app.logger.debug(f"Modified MPD content: {modified_mpd.decode('utf-8')}")

        proxy_headers = dict(response.headers)
        return Response(modified_mpd, status=response.status_code, headers=proxy_headers, mimetype='application/dash+xml')
    except requests.RequestException as e:
        app.logger.error(f"Proxy request failed: {str(e)}")
        return str(e), 502
    except ET.ParseError as e:
        app.logger.error(f"Failed to parse MPD XML: {str(e)}")
        return "Invalid MPD XML", 500

if __name__ == '__main__':
    app.run(host='192.168.1.25', port=5098, debug=True, ssl_context=('cert.pem', 'key.pem'))