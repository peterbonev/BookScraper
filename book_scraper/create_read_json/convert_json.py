import json
from defines_json import JSON_FILE


class ConvertToJson:
    def convert(self, items, dir=JSON_FILE):
        """
        Create/open file to write in it
        param: items = [{}],
        param: dir(optional).
        """
        with open(dir, "w+") as json_file:
            json.dump(items, json_file, indent=4)
