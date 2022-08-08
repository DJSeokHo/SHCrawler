# _*_ coding: utf-8 _*_
# @Time : 2022/08/04 5:07 PM
# @Author : Coding with cat
# @File : url_demo_baidu
# @Project : SHCrawler
import random
import time

from framewrok.utility.json_utility import JSONUtility
from framewrok.utility.log_utility import ILog
from framewrok.utility.urllib_utility import UrlLibUtility


def __test_1():
    url = "http://www.baidu.com/"

    response_object = UrlLibUtility.get(url)
    ILog.debug(__file__, response_object.get_dictionary())


def __test_2():
    """
    下载 网页，图片，视频
    :return:
    """
    url = "http://www.baidu.com/"
    image_url = "https://pbs.twimg.com/profile_images/1214465358981029888/H8xw2866_400x400.jpg"
    url_video = "https://vd2.bdstatic.com/mda-nh30qtb4dg7cy3y1/sc/cae_h264/1659573175809402548/mda-nh30qtb4dg7cy3y1.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1659605103-0-0-5130724d6bac03437182a5f02488022f&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=3303663310&vid=5929847066257230243&abtest=103525_1-103742_2-103890_1&klogid=3303663310"

    response_object = UrlLibUtility.download(url=url_video, file_name='video.mp4')
    ILog.debug(__file__, response_object.get_dictionary())


def __test_3():
    # 百度搜索
    url = "https://www.baidu.com/s"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    # query_params = {
    #     'wd': '周杰伦'
    # }

    query_params = {
        'wd': '周杰伦',
        'sex': '男',
        'location': '英国'
    }

    response_object = UrlLibUtility.get(url, headers=headers, query_params=query_params)
    ILog.debug(__file__, response_object.get_dictionary())


def __test_4():
    # 百度翻译
    url = "https://fanyi.baidu.com/sug"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    form_data = {
        'kw': 'hello'
    }

    response_object = UrlLibUtility.post(url, headers=headers, form_data=form_data)
    ILog.debug(__file__, response_object.get_dictionary())
    ILog.debug(__file__, JSONUtility.to_json_object(response_object.get_dictionary().get("data")))


def __test_5():
    # 百度详细翻译
    url = "https://fanyi.baidu.com/v2transapi"

    # Cookie 最重要，一般用于反爬 特别注意
    headers = {"Accept": "*/*",
               # "Accept-Encoding": "gzip, deflate, br", 这个注意，需要注释掉
               "Accept-Language": "zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6",
               "Acs-Token": "1659596409550_1659672965266_8eJgrEth6bwbRTBpSj5E6kq3n7m7wGTgus+1vCNKUJCiGHE5jj9VC4u4X36f/t+aiHoW2CrYULWh77ICGewwupPmRdBcRaiL0IWIoeqWrKQYoEWLcrv7FnPQDi134InVnSAAzvPbiTUkaIRq74EI4Vl3aLxIXZXRscrCl96VmYoCI9rXWqsMzGYCg0nXrT1qoSY4y96yVgnqBVHHx3EGYTzCr3tdR/HRmkwkmNK7PZfBa/HFXKs3ulT1e7JUk7qOQrUPkISHiinmVU6rt0SauY5NZw12yYbWpm36RdBAuiulvs4jhHlE9bBkv8s3aE1cCHi323tHNcfKOxo4ex/9Kw==",
               "Connection": "keep-alive",
               "Content-Length": "135",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Cookie": "BAIDUID=9D5654968E19555DE2ED2D6444894C9B:FG=1; BIDUPSID=9D5654968E19555DE2ED2D6444894C9B; PSTM=1652859445; BDUSS=RpVHV2TH5jSkQ1WDJFTVZ1T2M2aWFzbTdjTkZzbFBFOFR3RlRhTEQyR2pLNnhpRVFBQUFBJCQAAAAAAAAAAAEAAABnxPkMREpTZW9raG8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKOehGKjnoRiS3; BDUSS_BFESS=RpVHV2TH5jSkQ1WDJFTVZ1T2M2aWFzbTdjTkZzbFBFOFR3RlRhTEQyR2pLNnhpRVFBQUFBJCQAAAAAAAAAAAEAAABnxPkMREpTZW9raG8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKOehGKjnoRiS3; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1658214351; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=7; ZFY=fSJTSwX:Bn96VrOmFitPGfHF7gfByyZ:B:AIktBpq0x:Anc:C; BAIDUID_BFESS=9D5654968E19555DE2ED2D6444894C9B:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BCLID=10593910014607114771; BDSFRCVID=bqFOJexroG0m2PRDgGARuncU7mKK0gOTDYLEOwXPsp3LGJLVchdUEG0PtDnjHU8bdLi5ogKK5mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRk8oCDhJIvDqTrP-trf5DCShUFsKUrWB2Q-XPoO3Kt-EIonQ-bULf40hxbPt-r3yebqBfbgy4op8P3y0bb2DUA1y4vp5MLfJeTxoUJ25ROW8pCmqtnWXtCebPRit4r9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wDjA5D6PVKgTa54cbb4o2WbCQ-n-28pcN2b5oQT8D0Nut0UcLJT6tWJOGJ-oNSlr8jqOUWJDkXpJvQnJjt2JxaqRCKhKMep5jDh3MQMIeMGAJe4ROtKJy0hvcJR6cShPCyUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDHt8J6ketJ3aQ5rtKRTffjrnhPF3Q68TXP6-hnjy3bRLbKIa3pTVMhnGh4bljnDF34Twtl3Ry6r42-39LPO2hpRjyxv4-UQ3bPoxJpOJ3gQyBDP2HR7WhnRvbURvjtug3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoDLKtI0hMDtr-R-_-4_tbh_X5-RLfKT9al7F54nKDp0xhj5m0x0shfCH-462QRvLahkM5h7xsMTsQfnbWh8yKabr0MTrQD730U5N3KJmfhbkMx7le-DOXMut2-biWbTL2MbdJqvP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe6K-j6OWjH_jq-jeHDrKBRbaHJOoDDvPKfjcy4LbKxnxJPuHLNrR0h3pLt5_HUK6hfRvD--g3-OkWUQ9babTQ-tbBp3k8MQnM-OlQfbQ0hOR2tT7QRba0pRVJR7JOpkGhfnxy5KUQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ut6T2-DA__IP2tC5P; BCLID_BFESS=10593910014607114771; BDSFRCVID_BFESS=bqFOJexroG0m2PRDgGARuncU7mKK0gOTDYLEOwXPsp3LGJLVchdUEG0PtDnjHU8bdLi5ogKK5mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tRk8oCDhJIvDqTrP-trf5DCShUFsKUrWB2Q-XPoO3Kt-EIonQ-bULf40hxbPt-r3yebqBfbgy4op8P3y0bb2DUA1y4vp5MLfJeTxoUJ25ROW8pCmqtnWXtCebPRit4r9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wDjA5D6PVKgTa54cbb4o2WbCQ-n-28pcN2b5oQT8D0Nut0UcLJT6tWJOGJ-oNSlr8jqOUWJDkXpJvQnJjt2JxaqRCKhKMep5jDh3MQMIeMGAJe4ROtKJy0hvcJR6cShPCyUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDHt8J6ketJ3aQ5rtKRTffjrnhPF3Q68TXP6-hnjy3bRLbKIa3pTVMhnGh4bljnDF34Twtl3Ry6r42-39LPO2hpRjyxv4-UQ3bPoxJpOJ3gQyBDP2HR7WhnRvbURvjtug3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoDLKtI0hMDtr-R-_-4_tbh_X5-RLfKT9al7F54nKDp0xhj5m0x0shfCH-462QRvLahkM5h7xsMTsQfnbWh8yKabr0MTrQD730U5N3KJmfhbkMx7le-DOXMut2-biWbTL2MbdJqvP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe6K-j6OWjH_jq-jeHDrKBRbaHJOoDDvPKfjcy4LbKxnxJPuHLNrR0h3pLt5_HUK6hfRvD--g3-OkWUQ9babTQ-tbBp3k8MQnM-OlQfbQ0hOR2tT7QRba0pRVJR7JOpkGhfnxy5KUQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ut6T2-DA__IP2tC5P; BA_HECTOR=85858laga12l04800182db7r1hemvj217; BDRCVFR[fb3VbsUruOn]=ddONZc2bo5mfAF9pywdpAqVuNqsus; RT=\"z=1&dm=baidu.com&si=gglgqh8sppk&ss=l6esygam&sl=2&tt=3xm&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=3rg&ul=58o8&hd=58oq\"; H_PS_PSSID=36556_36624_36824_36981_36413_36954_36949_36166_36918_36745_26350_36861_22159; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1659666957; ab_sr=1.0.1_M2QwOTkzZDE3YTFjNWI1MThiYTUxNDQ5OGQ1ZGIyYWMxOThlNDFiOWE3OGEyZTUzZGRjYjllMGE1OGFmOWI4MGVjMGIwOGUzYjBkNmZlNjIyNGI3ZDMyZGM5ODk2ZmUzMTczOTljYWY0M2Q3OTUyOWJiZjI5YTlhYjU3NTg5NzRmMTU5YjdhZDczODE5NTQ5ZmY1YzQxMzMyYTVmNzUyYmJmZTBhNzU0MzkzZmIxMjRkNDQ2NzQ4ZmE5ZDQxOTAy",
               "Host": "fanyi.baidu.com",
               "Origin": "https://fanyi.baidu.com",
               "Referer": "https://fanyi.baidu.com/?aldtype=16047",
               "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
               "sec-ch-ua-mobile": "?0",
               "sec-ch-ua-platform": "\"macOS\"",
               "Sec-Fetch-Dest": "empty",
               "Sec-Fetch-Mode": "cors",
               "Sec-Fetch-Site": "same-origin",
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
               "X-Requested-With": "XMLHttpRequest"}

    query_params = {
        'from': 'en',
        'to': 'zh'
    }

    form_data = {
        'from': 'en',
        'to': 'zh',
        'query': 'hello',
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': '54706.276099',
        'token': 'b25941327be32216d1048bba4854f5b9',
        'domain': 'common'
    }

    response_object = UrlLibUtility.post(url, headers=headers, query_params=query_params, form_data=form_data)
    ILog.debug(__file__, response_object.get_dictionary())
    ILog.debug(__file__, JSONUtility.to_json_object(response_object.get_dictionary().get("data")))


def __test_6():
    # 豆瓣电影排行榜第一页
    url = "https://movie.douban.com/j/chart/top_list"

    headers = {
        "Accept": "*/*",
        # "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6",
        "Connection": "keep-alive",
        "Cookie": "ll=\"108235\"; bid=lGxfI9VB8JU; __utmc=30149280; __utmc=223695111; "
                  "trc_cookie_storage=taboola%2520global%253Auser-id%3Dd4b35f2b-234e-4000-8350-a9e7f87d3b53"
                  "-tuct97b59c9; "
                  "_vwo_uuid_v2=DF4D7DF90213DCB0E689F7190288D51FD|e3880f349a85cfbc9071ec7027bd30bc; "
                  "_cc_id=faa78df734d38389d037aa512d5299b6; douban-fav-remind=1; "
                  "__utmz=30149280.1659675059.20.12.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; "
                  "__utmz=223695111.1659675059.20.12.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,"
                  "6.0; __gpi=UID=0000055a9420c923:T=1652681567:RT=1659675059:S"
                  "=ALNI_MZL5MfBHi3t18MlvrggDeyCZ9ICHw; "
                  "__gads=ID=320c7f13541eb470-226084af6cd50058:T=1652681567:RT=1659675059:S"
                  "=ALNI_MZ79S9vSHStwno3pHjGih_qC2A9kQ; "
                  "__utma=30149280.969812328.1652681565.1659675059.1659676984.21; "
                  "__utmb=30149280.0.10.1659676984; "
                  "__utma=223695111.588294267.1652681565.1659675059.1659676984.21; "
                  "__utmb=223695111.0.10.1659676984; "
                  "_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1659676984%2C%22https%3A%2F%2Fwww.baidu.com%2Flink"
                  "%3Furl%3DwQgaPqx8Ur17UPDAkWkzX4q8N23KD_f7MkK3gLcMTjoohuwTA2w9qXfGCr2QTeEC%26wd%3D%26eqid"
                  "%3Dcef04fbd0001954a0000000662eca1ae%22%5D; _pk_ses.100001.4cf6=*; "
                  "_pk_id.100001.4cf6=36cc4fe285eb9bab.1652681565.21.1659677072.1659675078.",
        "Host": "movie.douban.com",
        "Referer": "https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C%E7%89%87&type=5&interval_id"
                   "=100:90&action=",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"macOS\"", "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    query_params = {
        'type': '5',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'
    }

    response_object = UrlLibUtility.get(url=url, headers=headers, query_params=query_params)
    ILog.debug(__file__, response_object.get_dictionary())
    data_string = response_object.get_dictionary()['data']

    fp = open('douban.json', 'w', encoding='utf-8')
    fp.write(data_string)


def __test_7():
    # 豆瓣电影排行榜第一页
    url = "https://movie.douban.com/j/chart/top_list"

    headers = {
        "Accept": "*/*",
        # "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6",
        "Connection": "keep-alive",
        "Cookie": "ll=\"108235\"; bid=lGxfI9VB8JU; __utmc=30149280; __utmc=223695111; "
                  "trc_cookie_storage=taboola%2520global%253Auser-id%3Dd4b35f2b-234e-4000-8350-a9e7f87d3b53"
                  "-tuct97b59c9; "
                  "_vwo_uuid_v2=DF4D7DF90213DCB0E689F7190288D51FD|e3880f349a85cfbc9071ec7027bd30bc; "
                  "_cc_id=faa78df734d38389d037aa512d5299b6; douban-fav-remind=1; "
                  "__utmz=30149280.1659675059.20.12.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; "
                  "__utmz=223695111.1659675059.20.12.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,"
                  "6.0; __gpi=UID=0000055a9420c923:T=1652681567:RT=1659675059:S"
                  "=ALNI_MZL5MfBHi3t18MlvrggDeyCZ9ICHw; "
                  "__gads=ID=320c7f13541eb470-226084af6cd50058:T=1652681567:RT=1659675059:S"
                  "=ALNI_MZ79S9vSHStwno3pHjGih_qC2A9kQ; "
                  "__utma=30149280.969812328.1652681565.1659675059.1659676984.21; "
                  "__utmb=30149280.0.10.1659676984; "
                  "__utma=223695111.588294267.1652681565.1659675059.1659676984.21; "
                  "__utmb=223695111.0.10.1659676984; "
                  "_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1659676984%2C%22https%3A%2F%2Fwww.baidu.com%2Flink"
                  "%3Furl%3DwQgaPqx8Ur17UPDAkWkzX4q8N23KD_f7MkK3gLcMTjoohuwTA2w9qXfGCr2QTeEC%26wd%3D%26eqid"
                  "%3Dcef04fbd0001954a0000000662eca1ae%22%5D; _pk_ses.100001.4cf6=*; "
                  "_pk_id.100001.4cf6=36cc4fe285eb9bab.1652681565.21.1659677072.1659675078.",
        "Host": "movie.douban.com",
        "Referer": "https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C%E7%89%87&type=5&interval_id"
                   "=100:90&action=",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"macOS\"", "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    __temp_list = list()

    for i in range(0, 5):
        query_params = {
            'type': '5',
            'interval_id': '100:90',
            'action': '',
            'start': f'{i * 20}',
            'limit': '20'
        }

        response_object = UrlLibUtility.get(url=url, headers=headers, query_params=query_params)
        ILog.debug(__file__, response_object.get_dictionary())
        data_string = response_object.get_dictionary()['data']

        __temp_array = JSONUtility.to_json_array(data_string)

        for item in __temp_array:
            __temp_list.append(item)

        time.sleep(3)

    fp = open('douban5.json', 'w', encoding='utf-8')
    fp.write(str(__temp_list))


def __test_8():
    # 肯德基餐厅位置
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx"

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6",
        "Connection": "keep-alive",
        "Content-Length": "53",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "route-cell=ksa; ASP.NET_SessionId=1lgkqnohehztrt2m5dr5mlhy; Hm_lvt_5fd8501a4e4e0eddf0c4596de7bd57ab=1659681439; Hm_lvt_1039f1218e57655b6677f30913227148=1659681439; Hm_lpvt_5fd8501a4e4e0eddf0c4596de7bd57ab=1659681524; Hm_lpvt_1039f1218e57655b6677f30913227148=1659681525; SERVERID=02f4c994014ba2083ffa81762e56b1a0|1659682037|1659681438",
        "Host": "www.kfc.com.cn",
        "Origin": "http://www.kfc.com.cn",
        "Referer": "http://www.kfc.com.cn/kfccda/storelist/index.aspx",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    query_params = {
        'op': 'cname'
    }

    __temp_list = list()

    for i in range(0, 5):

        form_data = {
            'cname': '北京',
            'pid': '',
            'pageIndex': f'{(i + 1)}',
            'pageSize': '10'
        }

        response_object = UrlLibUtility.post(url=url, headers=headers, query_params=query_params, form_data=form_data)
        data_string = response_object.get_dictionary()['data']
        __temp_table = JSONUtility.to_json_object(data_string)['Table1']
        ILog.debug(__file__, __temp_table)
        # __temp_array = JSONUtility.to_json_array(str(__temp_table))

        for item in __temp_table:
            __temp_list.append(item)

        time.sleep(3)

    fp = open('kendeji5.json', 'w', encoding='utf-8')
    fp.write(str(__temp_list))


def __test_9():
    # 微博cookie绕过登录和详细信息
    url = "https://weibo.com/ajax/profile/info"

    headers = {
        "accept": "application/json, text/plain, */*",
        # "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6",
        "client-version": "v2.34.76",
        "cookie": "login_sid_t=dad79da3fddc0e3fa0f92ea665ee873e; cross_origin_proto=SSL; "
                  "_s_tentry=passport.weibo.com; Apache=2763422235674.613.1652751815618; "
                  "SINAGLOBAL=2763422235674.613.1652751815618; "
                  "ULV=1652751815621:1:1:1:2763422235674.613.1652751815618:; "
                  "WBtopGlobal_register_version=2022051709; SSOLoginState=1652751840; "
                  "XSRF-TOKEN=EL1hfx1JJ9Z743JWhEn1pKrl; "
                  "SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW9uubII4-Ou2jXh4f6QDNv5JpX5KMhUgL"
                  ".FoeEeh5cSo5N1hz2dJLoIpUKHcHDdbH8SFHF1FHF1CH8SCHWSbHWxBtt; "
                  "YF-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0; "
                  "SCF=Aj6ZlH9rjOrnyy_1_9mZY0OFXtR53aVEAbaqEXcPSv99eiwJLsTrJAeeltV3BTFTprdEDgOmKIMmQd21qlfYQvE"
                  ".; SUB=_2A25P6LVeDeRhGeVM61IX9i7Lwz6IHXVsn6GWrDV8PUNbmtAfLVjAkW9NTMKiQS3kzMBzozt"
                  "-dzjsfYS1pN_HEIEM; ALF=1691220109; "
                  "WBPSESS=s-0NQ4M0QVQpcAEHgxJPBrcZKtb9tN3_hCT0PgdZ2KV-Aw1SBjKwWG3ZPu"
                  "-q9ekbTW37V9ll6dvnBTDrDnPxMc6JPmwh9vRwUg1MZ2h7yyqL7YtMvI8vZYpOc6-qBHvOdICVIjRX"
                  "-G1HfgdURmsZnA==",
        "referer": "https://weibo.com/u/1712572452",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"macOS\"", "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "server-version": "v2022.08.03.1",
        "traceparent": "00-a2d193708e0b0be2b9d887077134039a-074b1727632d0d45-00",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest", "x-xsrf-token": "EL1hfx1JJ9Z743JWhEn1pKrl"
    }

    query_params = {
        'uid': '1712572452'
    }

    response_object = UrlLibUtility.get(url=url, headers=headers, query_params=query_params)
    ILog.debug(__file__, response_object.get_dictionary())


def __test_10():
    # 微博cookie绕过登录下载详情页
    url = "https://weibo.com/u/1712572452"

    headers = {
        "accept": "application/json, text/plain, */*",
        # "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6",
        "client-version": "v2.34.76",
        "cookie": "login_sid_t=dad79da3fddc0e3fa0f92ea665ee873e; cross_origin_proto=SSL; "
                  "_s_tentry=passport.weibo.com; Apache=2763422235674.613.1652751815618; "
                  "SINAGLOBAL=2763422235674.613.1652751815618; "
                  "ULV=1652751815621:1:1:1:2763422235674.613.1652751815618:; "
                  "WBtopGlobal_register_version=2022051709; SSOLoginState=1652751840; "
                  "XSRF-TOKEN=EL1hfx1JJ9Z743JWhEn1pKrl; "
                  "SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW9uubII4-Ou2jXh4f6QDNv5JpX5KMhUgL"
                  ".FoeEeh5cSo5N1hz2dJLoIpUKHcHDdbH8SFHF1FHF1CH8SCHWSbHWxBtt; "
                  "YF-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0; "
                  "SCF=Aj6ZlH9rjOrnyy_1_9mZY0OFXtR53aVEAbaqEXcPSv99eiwJLsTrJAeeltV3BTFTprdEDgOmKIMmQd21qlfYQvE"
                  ".; SUB=_2A25P6LVeDeRhGeVM61IX9i7Lwz6IHXVsn6GWrDV8PUNbmtAfLVjAkW9NTMKiQS3kzMBzozt"
                  "-dzjsfYS1pN_HEIEM; ALF=1691220109; "
                  "WBPSESS=s-0NQ4M0QVQpcAEHgxJPBrcZKtb9tN3_hCT0PgdZ2KV-Aw1SBjKwWG3ZPu"
                  "-q9ekbTW37V9ll6dvnBTDrDnPxMc6JPmwh9vRwUg1MZ2h7yyqL7YtMvI8vZYpOc6-qBHvOdICVIjRX"
                  "-G1HfgdURmsZnA==",
        "referer": "https://weibo.com/",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"macOS\"", "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "server-version": "v2022.08.03.1",
        "traceparent": "00-a2d193708e0b0be2b9d887077134039a-074b1727632d0d45-00",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest", "x-xsrf-token": "EL1hfx1JJ9Z743JWhEn1pKrl"
    }

    response_object = UrlLibUtility.get(url=url, headers=headers)
    ILog.debug(__file__, response_object.get_dictionary())


def __test_11():
    # 使用代理
    # 代理的协议要和url的协议一致才行！ http 需要 http 代理， https 需要 https 代理
    url = "https://httpbin.org/get"

    headers = {
         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/104.0.0.0 Safari/537.36"
    }

    proxies_poor = [
        {
            'https': '125.21.3.41:8080'
        }
    ]

    proxies = random.choice(proxies_poor)

    response_object = UrlLibUtility.get(url, headers=headers, proxies=proxies)
    ILog.debug(__file__, response_object.get_dictionary())


if __name__ == '__main__':
    # header 里有个 referer，用途是防盗链，如果你的当前访问不是通过referer进来的，那么就会出错
    # __test_1()
    # __test_2()
    # __test_3()
    # __test_4()
    # __test_5()
    # __test_6()
    # __test_7()
    # __test_8()
    # __test_9()
    # __test_10()
    __test_11()
