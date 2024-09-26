import json
import logging
import traceback
from Utils.Logging_Operations import Logger

log = Logger(__name__, logging.INFO)


class Json_Operations:

    def __init__(self, base_url):
        self.base_url = base_url

# Return Dict of json data
# path eg : '../d_Requests_Practice/Jsons/create_customer_copy.json'
    def read_json_file_via_path(self, path):
        try:
            json_file = open(str(path), 'r')
            json_data = json.load(json_file)
            print(f"json data: {json_data}")
            log.logger.info(f"json data: {json_data}")
            return json_data
        except:
             print(traceback.print_exc())
             assert False

# Return json string
    def json_to_string(self, json_file):
        try:
            json_string = json.dumps(json_file)
            print(f"json string: {json_string}")
            print(f"json string: {json.dumps(json_file, indent=4)}")
            log.logger.info(f"json string: {json_string}")
            return json_string
        except:
             print(traceback.print_exc())
             assert False

# Target path should always contain .json file name eg : ../Sample.json
# Return Json File on targated location
    def dictionary_to_json(self, target_path, dict):
        try:
            with open(target_path, "w") as outfile:
                json.dump(dict, outfile)
            log.logger.info(f"Json file created at: {target_path} from dictionary")
        except:
             print(traceback.print_exc())
             assert False
