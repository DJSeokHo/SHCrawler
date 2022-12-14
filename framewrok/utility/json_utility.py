# coding: utf-8

import json

from framewrok.utility.log_utility import ILog


class JSONUtility:

    @staticmethod
    def to_json_object(json_object_str) -> dict:
        return json.loads(json_object_str)

    @staticmethod
    def to_json_array(json_array_str) -> list:
        return json.loads(json_array_str)

    @staticmethod
    def parsing_str(the_json_object: dict, key: str, default_value: str = "") -> str:
        try:
            return the_json_object[key]
        except Exception as e:
            ILog.debug(__file__, e)
            return default_value

    @staticmethod
    def parsing_int(the_json_object: dict, key: str, default_value: int = "") -> int:
        try:
            return the_json_object[key]
        except Exception as e:
            ILog.debug(__file__, e)
            return default_value

    @staticmethod
    def parsing_float(the_json_object: dict, key: str, default_value: float = "") -> float:
        try:
            return the_json_object[key]
        except Exception as e:
            ILog.debug(__file__, e)
            return default_value

    @staticmethod
    def parsing_bool(the_json_object: dict, key: str, default_value: bool = "") -> bool:
        try:
            return the_json_object[key]
        except Exception as e:
            ILog.debug(__file__, e)
            return default_value

    @staticmethod
    def to_json_string(the_json_object: dict) -> str:
        return json.dumps(the_json_object)


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
