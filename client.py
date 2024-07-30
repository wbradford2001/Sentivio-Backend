from http.client import HTTPSConnection
from base64 import b64encode
from json import loads
from json import dumps

import os


class RestClient:
    def __init__(self, sandbox):
        self.username = "william@sentivio.com"
        self.password = os.environ['API_KEY']
        if sandbox:
            self.domain =  "sandbox.dataforseo.com"
        else:
            self.domain = "api.dataforseo.com"

    def request(self, path, method, data=None):
        connection = HTTPSConnection(self.domain)
        try:
            base64_bytes = b64encode(
                ("%s:%s" % (self.username, self.password)).encode("ascii")
                ).decode("ascii")
            headers = {'Authorization' : 'Basic %s' %  base64_bytes, 'Content-Encoding' : 'gzip'}
            connection.request(method, path, headers=headers, body=data)
            response = connection.getresponse()
            return loads(response.read().decode())
        finally:
            connection.close()

    def get(self, path):
        return self.request(path, 'GET')

    def post(self, path, data):
        if isinstance(data, str):
            data_str = data
        else:
            data_str = dumps(data)
        return self.request(path, 'POST', data_str)



class API:
    def __init__(self, sandbox):
        self.client = RestClient(sandbox)

    def call(self, path, params, method="post"):
        post_data = dict()
        post_data[len(post_data)] = params


        if method=="post":
            response = self.client.post("/v3/" + path, post_data)
        else:
            response = self.client.get("/v3/" + path)


        # you can find the full list of the response codes here https://docs.dataforseo.com/v3/serp/id_list
        if response["status_code"] == 20000:

            return (response), response["cost"]
            # do something with result
        else:
            print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
        return (response), response["cost"]


   
    



