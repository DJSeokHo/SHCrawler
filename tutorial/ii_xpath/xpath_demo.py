# _*_ coding: utf-8 _*_
# @Time : 2022/08/08 6:03 PM
# @Author : Coding with cat
# @File : xpath_demo
# @Project : SHCrawler

from lxml import etree

from framewrok.utility.log_utility import ILog

'''
xpath 基本语法
1. 路径查询
// 查找所有子孙节点，不考虑层级关系
/ 找直接子节点

2. 谓词查询
//div[@id]
//div[@id="maincontent"]

3. 属性查询
//@class

4. 模糊查询
//div[contains(@id, "he")]
//div[starts-with(@id, "he")]

5. 内容查询
//div/h1/text()

6. 逻辑运算
//div[@id="head" and @class="s_down"]
//title | //price
'''


def __test_1():
    # xpath 解析本地文件
    tree = etree.parse('local_xpath_test_file.html')
    li_list = tree.xpath('//body/ul/li')
    ILog.debug(__file__, li_list)
    ILog.debug(__file__, len(li_list))

    # 查找所有有id的li标签
    li_with_id_list = tree.xpath('//ul/li[@id]')
    ILog.debug(__file__, li_with_id_list)
    ILog.debug(__file__, len(li_with_id_list))

    # 查找所有有id的li标签的内容
    li_with_id_list = tree.xpath('//ul/li[@id]/text()')
    ILog.debug(__file__, li_with_id_list)
    ILog.debug(__file__, len(li_with_id_list))


if __name__ == '__main__':
    __test_1()
