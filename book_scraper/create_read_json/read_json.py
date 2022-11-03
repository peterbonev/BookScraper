import json
from defines_json import JSON_FILE

class ReadJson():
    key_search = "title"

    def check_title_json_file(self, titles, dir= JSON_FILE):
        """
            Read Json file and search for given title in it
            param: title,
            param: dir(optional).
        """
        with open(dir, 'r') as file_handler:
            json_file = json.load(file_handler)

        for item in json_file.values():
            for title in titles:
                if item == title[self.key_search]:
                    print(json.dumps(title, indent=4))