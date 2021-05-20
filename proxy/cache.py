from abc import abstractmethod
import requests


# Http Request Interface
class IHttpRequest:

    @abstractmethod
    def make_request(self, url):
        pass

    @abstractmethod
    def get_response(self):
        pass


class HttpRequest:

    def make_request(self, url):
        request = requests.get(url)
        return request

    def get_response(self, request):
        response = request.text
        return response

# Proxy Pattern


class HttpCache:
    def __init__(self):
        self._fetch = HttpRequest()
        self.cache = {}

    def make_request(self, url):
        if url in self.cache.keys():
            request = self.cache[url]
            return request
        request = self._fetch.make_request(url)
        self.cache[url] = request
        return request

    def get_response(self, request):
        response = self._fetch.get_response(request)
        return response


cache = HttpCache()
req = cache.make_request("http://b19cc105bbc4.ngrok.io")
res = cache.get_response(req)
req = cache.make_request("https://google.com")
res = cache.get_response(req)
req = cache.make_request("http://twitter.com")
res = cache.get_response(req)
req = cache.make_request("http://b19cc105bbc4.ngrok.io")
res = cache.get_response(req)

print(cache.cache)
