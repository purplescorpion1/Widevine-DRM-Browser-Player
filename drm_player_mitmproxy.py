from mitmproxy import http
import json

class HeaderInjector:
    def __init__(self):
        self.referer = ""
        self.origin = ""

    def load(self, loader):
        loader.add_option(
            "config_file", str, "proxy_config.json",
            "File to store proxy configuration"
        )

    def request(self, flow: http.HTTPFlow):
        try:
            with open("proxy_config.json", "r") as f:
                config = json.load(f)
                self.referer = config.get("referer", "")
                self.origin = config.get("origin", "")
        except Exception:
            pass

        if self.referer:
            flow.request.headers["Referer"] = self.referer
        if self.origin:
            flow.request.headers["Origin"] = self.origin

        if flow.request.url.startswith("http://192.168.1.25:8080/"):
            flow.request.url = flow.request.url.replace("http://192.168.1.25:8080/", "")

addons = [HeaderInjector()]