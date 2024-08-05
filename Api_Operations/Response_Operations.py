import logging
import traceback
from Utils.Logging_Operations import Logger
import json
import requests

log = Logger(__name__, logging.INFO)


class Request_Operations:

    def __init__(self, response):
        self.response = response

    # This method returns api response status code as integer
    def get_response_status_code(self):
        try:
            status_code = self.response.status_code
            log.logger.info(f"Response status code is {status_code}")
            print(f"Response status code is {status_code}")
            return status_code

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api complete response as text(str)
    def get_response_as_text(self):
        try:
            response_text = self.response.text
            log.logger.info(f"Response in text is {response_text}")
            print(f"Response in text is {response_text}")
            return response_text

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response as json encoded content
    def get_response_as_json(self):
        try:
            response_json = self.response.json()
            log.logger.info(f"Response in json is {response_json}")
            print(f"Response in json is {response_json}")
            return response_json

        except:
            print(traceback.print_exc())
            assert False

    # This method returns parsed header links of the response in dict format if any
    def get_parsed_header_links_response(self):
        try:
            response_links = self.response.links
            log.logger.info(f"Parsed header links in response are {response_links}")
            print(f"Parsed header links in response are {response_links}")
            return response_links

        except:
            print(traceback.print_exc())
            assert False

    # This method returns response as request for prepared request <preparedrequest class obj>
    def get_response_for_prepared_request(self):
        try:
            response_prepared_request = self.response.request
            log.logger.info(f"Response request is {response_prepared_request}")
            print(f"Response request is {response_prepared_request}")
            return response_prepared_request

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response request method
    def get_response_request_method(self):
        try:
            response_request_method = self.response.request.method
            log.logger.info(f"Response request method is {response_request_method}")
            print(f"Response request method is {response_request_method}")
            return response_request_method

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response request body
    def get_response_request_body(self):
        try:
            response_request_body = self.response.request.body
            log.logger.info(f"Response request body is {response_request_body}")
            print(f"Response request body is {response_request_body}")
            return response_request_body

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response request hooks
    def get_response_request_hooks(self):
        try:
            response_request_hooks = self.response.request.hooks
            log.logger.info(f"Response request hooks are {response_request_hooks}")
            print(f"Response request hooks are {response_request_hooks}")
            return response_request_hooks

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response request url
    def get_response_request_url(self):
        try:
            response_request_url = self.response.request.url
            log.logger.info(f"Response request url is {response_request_url}")
            print(f"Response request url is {response_request_url}")
            return response_request_url

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response request path url
    def get_response_request_path_url(self):
        try:
            response_request_path_url = self.response.request.path_url
            log.logger.info(f"Response request path url is {response_request_path_url}")
            print(f"Response request path url is {response_request_path_url}")
            return response_request_path_url

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response request headers
    def get_response_request_headers(self):
        try:
            response_request_headers = self.response.request.headers
            log.logger.info(f"Response request headers are {response_request_headers}")
            print(f"Response request headers are {response_request_headers}")
            return response_request_headers

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response request copy
    def get_response_request_copy(self):
        try:
            response_request_headers_copy = self.response.request.copy()
            log.logger.info(f"Response request headers copy {response_request_headers_copy}")
            print(f"Response request headers copy {response_request_headers_copy}")
            return response_request_headers_copy

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response reason
    def get_response_reason(self):
        try:
            response_reason = self.response.reason
            log.logger.info(f"Response reason is {response_reason}")
            print(f"Response reason is {response_reason}")
            return response_reason

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response headers
    def get_response_headers(self):
        try:
            response_headers = self.response.headers
            log.logger.info(f"Response headers are {response_headers}")
            print(f"Response headers is {response_headers}")
            return response_headers

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response url
    def get_response_url(self):
        try:
            response_url = self.response.url
            log.logger.info(f"Response url is {response_url}")
            print(f"Response url is {response_url}")
            return response_url

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response content
    def get_response_content(self):
        try:
            response_content = self.response.content
            log.logger.info(f"Response content is {response_content}")
            print(f"Response content is {response_content}")
            return response_content

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response cookies
    def get_response_cookies(self):
        try:
            response_cookies = self.response.cookies
            log.logger.info(f"Response cookies are {response_cookies}")
            print(f"Response cookies are {response_cookies}")
            return response_cookies

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response elapsed time
    def get_response_elapsed(self):
        try:
            response_elapsed = self.response.elapsed
            log.logger.info(f"Response elapsed time is {response_elapsed}")
            print(f"Response elapsed time is {response_elapsed}")
            return response_elapsed

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response encoding format
    def get_response_encoding(self):
        try:
            response_encoding = self.response.encoding
            log.logger.info(f"Response encoding is {response_encoding}")
            print(f"Response encoding is {response_encoding}")
            return response_encoding

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response history
    def get_response_history(self):
        try:
            response_history = self.response.history
            log.logger.info(f"Response history is {response_history}")
            print(f"Response history is {response_history}")
            return response_history

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response is redirect or not (bool)
    def get_response_redirect_status(self):
        try:
            response_redirect_status = self.response.is_redirect
            log.logger.info(f"Response redirect status is {response_redirect_status}")
            print(f"Response redirect status is {response_redirect_status}")
            return response_redirect_status

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response is permanent redirect or not (bool)
    def get_response_permanent_redirect_status(self):
        try:
            response_permanent_redirect_status = self.response.is_permanent_redirect
            log.logger.info(f"Response permanent redirect status is {response_permanent_redirect_status}")
            print(f"Response permanent redirect status is {response_permanent_redirect_status}")
            return response_permanent_redirect_status

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api raw response
    def get_raw_response(self):
        try:
            raw_response = self.response.raw
            log.logger.info(f"Response raw is {raw_response}")
            print(f"Response raw is {raw_response}")
            return raw_response

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response raise_for_status
    def get_response_raise_for_status(self):
        try:
            response_raise_for_status = self.response.raise_for_status()
            log.logger.info(f"Response raise_for_status is {response_raise_for_status}")
            print(f"Response raise_for_status is {response_raise_for_status}")
            return response_raise_for_status

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response apparent_encoding
    def get_response_apparent_encoding(self):
        try:
            response_apparent_encoding = self.response.apparent_encoding
            log.logger.info(f"Response apparent_encoding is {response_apparent_encoding}")
            print(f"Response apparent_encoding is {response_apparent_encoding}")
            return response_apparent_encoding

        except:
            print(traceback.print_exc())
            assert False

    # This method returns true if api response status code is between 200 and 400
    def get_response_ok(self):
        try:
            response_ok = self.response.ok
            log.logger.info(f"Response 200 <= status < 400, true is {response_ok}")
            print(f"Response 200 <= status < 400, true is {response_ok}")
            return response_ok

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response next
    def get_response_next(self):
        try:
            response_next = self.response.next
            log.logger.info(f"Response next is {response_next}")
            print(f"Response next is {response_next}")
            return response_next

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response links as dict
    def get_response_links(self):
        try:
            response_links = self.response.links
            log.logger.info(f"Response links dict is {response_links}")
            print(f"Response links dict is {response_links}")
            return response_links

        except:
            print(traceback.print_exc())
            assert False

    # This method returns api response close
    def get_response_close(self):
        try:
            response_close = self.response.close()
            log.logger.info(f"Response close is {response_close}")
            print(f"Response close is {response_close}")
            return response_close

        except:
            print(traceback.print_exc())
            assert False
