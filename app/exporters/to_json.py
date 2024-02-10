import json
from .export import ExportStrategy
from parsers.parser import ResultBase
from typing import List


class JsonExport(ExportStrategy):
    def export(self, parsed_data: List[ResultBase]) -> None:
        data = self.convert_to_dict(parsed_data)
        with open("data.json", 'w', encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

    def convert_to_dict(self, obj):
        if hasattr(obj, '__dict__'):
            result = obj.__dict__.copy()
            for key, value in result.items():
                if hasattr(value, '__dict__'):
                    result[key] = self.convert_to_dict(value)
            return result
        elif isinstance(obj, list):
            return [self.convert_to_dict(item) for item in obj]
        else:
            return obj
