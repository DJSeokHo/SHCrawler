# coding: utf-8

import json

from framewrok.utility.log_utility import ILog


class JSONUtility:

    @staticmethod
    def to_json_object(json_object_str) -> dict:
        return json.loads(json_object_str)

    @staticmethod
    def parsing_str(json_object: dict, key: str, default_value: str = "") -> str:
        try:
            return json_object[key]
        except:
            return default_value

    @staticmethod
    def parsing_int(json_object: dict, key: str, default_value: int = "") -> int:
        try:
            return json_object[key]
        except:
            return default_value

    @staticmethod
    def parsing_float(json_object: dict, key: str, default_value: float = "") -> float:
        try:
            return json_object[key]
        except:
            return default_value

    @staticmethod
    def parsing_bool(json_object: dict, key: str, default_value: bool = "") -> bool:
        try:
            return json_object[key]
        except:
            return default_value

    @staticmethod
    def to_json_string(json_object: dict) -> str:
        return json.dumps(json_object)


if __name__ == '__main__':
    # Python 字典类型转换为 JSON 对象
    json_object = {
        'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoob.com',
        'array': [
            "1", 2, "c"
        ]
    }

    json_string = JSONUtility.to_json_string(json_object)
    ILog.debug(__name__, json_string)

    new_json_object = JSONUtility.to_json_object(json_string)
    ILog.debug(__name__, new_json_object)

    name = JSONUtility.parsing_str(new_json_object, "name")
    ILog.debug(__name__, name)

    test = JSONUtility.parsing_str(new_json_object, "test", "666")
    ILog.debug(__name__, test)
