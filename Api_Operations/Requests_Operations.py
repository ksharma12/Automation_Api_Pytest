import logging
import traceback

from Api_Operations.Json_Operations import Json_Operations
from Api_Operations.Prepared_Request_Operations import Prepared_Request_Operations
from Api_Operations.Response_Operations import Response_Operations
from Utils.Logging_Operations import Logger
import json
import requests

log = Logger(__name__, logging.INFO)


class Request_Operations(Json_Operations, Prepared_Request_Operations, Response_Operations):

    def __init__(self, base_url):
        Json_Operations.__init__(self, base_url)
        Prepared_Request_Operations.__init__(self, base_url)
        Response_Operations.__init__(self, base_url)
        self.base_url = base_url

    # def get_method(self, inputs):
    #     try:
    #          response = requests.get(headers=inputs["headers"],
    #                      cookies=inputs["cookies"],
    #                      files=inputs["files"],
    #                      auth=inputs["auth"],
    #                      timeout=inputs["timeout"],
    #                      allow_redirects=inputs["allow_redirects"],
    #                      proxies=inputs["proxies"],
    #                      hooks=inputs["hooks"],
    #                      cert=inputs["cert"],
    #                      stream=inputs["stream"],
    #                      verify=inputs["verify"],
    #                      json=inputs["json"],
    #                      url=inputs["url"])
    #          log.logger.info(f"Api skeleton with GET method {inputs}")
    #          return response
    #     except:
    #          print(traceback.print_exc())
    #          assert False

    def get_method(self, inputs):
        try:
            response = requests.request(method=inputs["Method"], url=inputs["url"])
            log.logger.info(f"Api skeleton is: {inputs}")
            return response
        except:
            print(traceback.print_exc())
            assert False
