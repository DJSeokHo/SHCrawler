# _*_ coding: utf-8 _*_
# @Time : 2022/08/08 6:03 PM
# @Author : Coding with cat
# @File : xpath_demo
# @Project : SHCrawler

from lxml import etree

from framewrok.module.url_lib_wrapper.url_lib_wrapper import UrlLibWrapper
from framewrok.utility.json_utility import JSONUtility
from framewrok.utility.log_utility import ILog
from framewrok.utility.proxies_utility import ProxiesUtility

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

    # 查询所有id里包含'l'的标签的内容
    li_with_id_contain_l_list = tree.xpath('//ul/li[contains(@id, "l")]/text()')
    ILog.debug(__file__, li_with_id_contain_l_list)
    ILog.debug(__file__, len(li_with_id_contain_l_list))

    # 查询所有id里以'c'的标签的内容
    li_with_id_start_with_c_list = tree.xpath('//ul/li[starts-with(@id, "c")]/text()')
    ILog.debug(__file__, li_with_id_start_with_c_list)
    ILog.debug(__file__, len(li_with_id_start_with_c_list))


def __test_2():
    response_object = UrlLibWrapper().url('https://www.baidu.com/').headers({
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        # "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6",
        "Cache-Control": "max-age=0", "Connection": "keep-alive",
        "Cookie": "BAIDUID=9D5654968E19555DE2ED2D6444894C9B:FG=1; BIDUPSID=9D5654968E19555DE2ED2D6444894C9B; "
                  "PSTM=1652859445; BD_UPN=123253; "
                  "BDSFRCVID"
                  "=bqFOJexroG0m2PRDgGARuncU7mKK0gOTDYLEOwXPsp3LGJLVchdUEG0PtDnjHU8bdLi5ogKK5mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRk8oCDhJIvDqTrP-trf5DCShUFsKUrWB2Q-XPoO3Kt-EIonQ-bULf40hxbPt-r3yebqBfbgy4op8P3y0bb2DUA1y4vp5MLfJeTxoUJ25ROW8pCmqtnWXtCebPRit4r9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wDjA5D6PVKgTa54cbb4o2WbCQ-n-28pcN2b5oQT8D0Nut0UcLJT6tWJOGJ-oNSlr8jqOUWJDkXpJvQnJjt2JxaqRCKhKMep5jDh3MQMIeMGAJe4ROtKJy0hvcJR6cShPCyUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDHt8J6ketJ3aQ5rtKRTffjrnhPF3Q68TXP6-hnjy3bRLbKIa3pTVMhnGh4bljnDF34Twtl3Ry6r42-39LPO2hpRjyxv4-UQ3bPoxJpOJ3gQyBDP2HR7WhnRvbURvjtug3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoDLKtI0hMDtr-R-_-4_tbh_X5-RLfKT9al7F54nKDp0xhj5m0x0shfCH-462QRvLahkM5h7xsMTsQfnbWh8yKabr0MTrQD730U5N3KJmfhbkMx7le-DOXMut2-biWbTL2MbdJqvP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe6K-j6OWjH_jq-jeHDrKBRbaHJOoDDvPKfjcy4LbKxnxJPuHLNrR0h3pLt5_HUK6hfRvD--g3-OkWUQ9babTQ-tbBp3k8MQnM-OlQfbQ0hOR2tT7QRba0pRVJR7JOpkGhfnxy5KUQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ut6T2-DA__IP2tC5P; BDSFRCVID_BFESS=bqFOJexroG0m2PRDgGARuncU7mKK0gOTDYLEOwXPsp3LGJLVchdUEG0PtDnjHU8bdLi5ogKK5mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tRk8oCDhJIvDqTrP-trf5DCShUFsKUrWB2Q-XPoO3Kt-EIonQ-bULf40hxbPt-r3yebqBfbgy4op8P3y0bb2DUA1y4vp5MLfJeTxoUJ25ROW8pCmqtnWXtCebPRit4r9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wDjA5D6PVKgTa54cbb4o2WbCQ-n-28pcN2b5oQT8D0Nut0UcLJT6tWJOGJ-oNSlr8jqOUWJDkXpJvQnJjt2JxaqRCKhKMep5jDh3MQMIeMGAJe4ROtKJy0hvcJR6cShPCyUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDHt8J6ketJ3aQ5rtKRTffjrnhPF3Q68TXP6-hnjy3bRLbKIa3pTVMhnGh4bljnDF34Twtl3Ry6r42-39LPO2hpRjyxv4-UQ3bPoxJpOJ3gQyBDP2HR7WhnRvbURvjtug3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoDLKtI0hMDtr-R-_-4_tbh_X5-RLfKT9al7F54nKDp0xhj5m0x0shfCH-462QRvLahkM5h7xsMTsQfnbWh8yKabr0MTrQD730U5N3KJmfhbkMx7le-DOXMut2-biWbTL2MbdJqvP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe6K-j6OWjH_jq-jeHDrKBRbaHJOoDDvPKfjcy4LbKxnxJPuHLNrR0h3pLt5_HUK6hfRvD--g3-OkWUQ9babTQ-tbBp3k8MQnM-OlQfbQ0hOR2tT7QRba0pRVJR7JOpkGhfnxy5KUQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ut6T2-DA__IP2tC5P; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=850g208g8h0k20ah0ha4e6dl1hf1cmu17; BAIDUID_BFESS=9D5654968E19555DE2ED2D6444894C9B:FG=1; ZFY=BIF1Nc7nkjwFwf6Eww8SGlN:Ak:A0laRSoaSUOUnq2WVs:C; delPer=0; BD_CK_SAM=1; PSINO=7; BD_HOME=1; baikeVisitId=d4149abe-2188-48d2-a721-c3a63819aa58; COOKIE_SESSION=234906_0_7_9_1_3_1_0_7_4_0_1_0_0_4_0_1659941940_0_1659941936%7C9%231806907_3_1658126607%7C2; ZD_ENTRY=baidu; H_PS_PSSID=36556_36624_36726_36981_36413_36954_36949_36166_36918_36569_37105_36745_37055_26350_36861_22159",
        "Host": "www.baidu.com",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"macOS\"", "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.0.0 Safari/537.36 "
    }).response()

    tree = etree.HTML(response_object.get_data())

    result = tree.xpath('//input[@id="su"]/@value')
    ILog.debug(__file__, result)


def __test_3():
    # 站长素材 情侣图片
    # 第一页地址：https://sc.chinaz.com/tupian/qinglvtupian.html
    # 第二页地址：https://sc.chinaz.com/tupian/qinglvtupian_2.html

    wrapper = UrlLibWrapper().headers({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.0.0 Safari/537.36 '
    })

    for i in range(0, 10):

        if i == 0:
            wrapper.url('https://sc.chinaz.com/tupian/qinglvtupian.html')
        else:
            wrapper.url(f'https://sc.chinaz.com/tupian/qinglvtupian_{i + 1}.html')

        response_object = wrapper.response()
        tree = etree.HTML(response_object.get_data())

        names = tree.xpath('//div[contains(@class, "tupian-list")]//img/@alt')
        images = tree.xpath('//div[contains(@class, "tupian-list")]//img/@data-original')  # 网站用了懒加载

        for j in range(0, len(names)):
            UrlLibWrapper().url(f'https:{images[j]}').download(f'images/{names[j]}.jpg')


def __test_4():
    # 解析淘票票
    url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1660024491168_108&jsoncallback=jsonp109' \
          '&action=cityAction&n_s=new&event_submit_doGetAllRegion=true '

    response_object = UrlLibWrapper().url(url).headers({
        "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, "
                  "*/*; q=0.01",
        # "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6",
        "bx-v": "2.2.2",
        "cookie": "_samesite_flag_=true; cookie2=1e56af060d60cf02c82ced94a68af82c; "
                  "t=1befbfa356e2340d4ced6d4b963f6013; _tb_token_=51e0b6e707b5e; cna=sj8JGyuDYBUCATsd6ipEIQP7; "
                  "sgcookie"
                  "=E100t5jB3Az7lXuVD0eEB25Xg3Sx1FaTIV3ulUCSiN8BagxdlKofMH0Pft9bJDIyQCgGw1RInp3f25SHl4zjDcn1ewrTFfKA1Z9QEC02B%2BEY4ws%3D; csg=ad57dfd6; cancelledSubSites=empty; dnk=shsysw1; skt=324631b9e48c690e; existShop=MTY1NDU4MTk5OA%3D%3D; tracknick=shsysw1; _cc_=UtASsssmfA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; uc1=cookie14=UoexOt8ZFw7pAg%3D%3D; _gid=GA1.2.505744909.1659948838; xlly_s=1; _uetsid=a391871016f711eda665c93087c63c7d; _uetvid=ddc40ef0066411edbca981d4f9b24a2f; _ga_YFVFB9JLVB=GS1.1.1660019303.3.0.1660019303.0; _ga=GA1.2.229693332.1658126581; _m_h5_tk=a95dab1e2813250e2308aa5a71b54fa9_1660028303525; _m_h5_tk_enc=8c6415519645c7813e1d4b5059bc29d8; v=0; tb_city=110100; tb_cityName=\"sbG+qQ==\"; tfstk=crnGBdtYnW17XYDr3cZ6mnqNHt8RZfs4ZmoIYdTaAoUbaooFiFQFzjwBK5AW_Z1..; l=eBTniu7RL0z-hnF8BOfZnurza779KIRAguPzaNbMiOCPO2CH5iUOW6YjZ08MCnMVhsLWR3uO6DEMBeYBc5vsjqj4axom4uHmn; isg=BElJp9S_TwnhkTMZKQpkDI8-WHOjlj3I4jpqFOu-hzBvMmlEM-QTmBvsdIaEatUA",
        "referer": "https://dianying.taobao.com/",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"macOS\"", "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }).response()

    response_json_object = JSONUtility.to_json_object(response_object.get_data().split('(')[1].split(')')[0])
    address_json_object_string = response_json_object['returnValue']

    ILog.debug(__file__, address_json_object_string)


if __name__ == '__main__':
    # __test_1()
    # __test_2()
    # __test_3()
    __test_4()
