class Browser:
    def make_http_request(self,url):
        print("Let's make the http request without auth ",url)

    def make_http_request(self,url,auth=None):
        print("Let's make http request with auth ",url,auth)

t= Browser()
print(t.make_http_request("google.com","admin"))
print(t.make_http_request("google.com"))