import logging
import traceback
from Utils.Logging_Operations import Logger
import json
import requests

log = Logger(__name__, logging.INFO)


class Prepared_Request_Operations:

    def __init__(self, response_request):
        self.response_request = response_request

    # This method returns prepared request type obj with url
    def get_response_status_code(self):
        try:
            response_request_with_prepared_url = self.response_request.prepare_url()
            log.logger.info(f"Response request with prepared url is {response_request_with_prepared_url}")
            print(f"Response status code is {response_request_with_prepared_url}")
            return response_request_with_prepared_url

        except:
            print(traceback.print_exc())
            assert False
