# _*_ coding: utf-8 _*_
# @Time : 2022/08/10 1:27 PM
# @Author : Coding with cat
# @File : auth_code
# @Project : SHCrawler

import ddddocr


class AuthCodeUtility:

    @staticmethod
    def auth_code_ocr(image_name: str) -> str:
        ocr = ddddocr.DdddOcr()
        with open(image_name, 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        return res
