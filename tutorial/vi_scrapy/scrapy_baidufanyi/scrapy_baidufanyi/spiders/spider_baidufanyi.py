import scrapy
from scrapy import cmdline
from scrapy.http import HtmlResponse

from framewrok.utility.json_utility import JSONUtility
from framewrok.utility.log_utility import ILog

"""
这里是post请求，所以起始url, parse函数都无用了
"""


class SpiderBaidufanyiSpider(scrapy.Spider):
    name = 'spider_baidufanyi'
    allowed_domains = ['fanyi.baidu.com']

    # start_urls = ['https://fanyi.baidu.com/sug']
    #
    # def parse(self, response):
    #
    #     html_response: HtmlResponse = response

    # 这个用于post请求
    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        form_data = {
            'kw': 'final'
        }

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            # "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6",
            "Connection": "keep-alive",
            "Content-Length": "8",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            # "Cookie": "BAIDUID=9D5654968E19555DE2ED2D6444894C9B:FG=1; BIDUPSID=9D5654968E19555DE2ED2D6444894C9B; PSTM=1652859445; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1658214351; BDSFRCVID=-FKOJexroG0mWT6DPvT-JmGJqeKKv3JTDYLE8yu9T4VNR5DVgxpaEG0Pt_ZYMak-XolpogKK5mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJFqoI0aJCt3H48k-4QEbbQH-UnLq-Q9WmOZ04n-ah02DDoM0xOJhtTX5fT2L6bLW20j0h7m3UTdsq76Wh35K5tTQP6rLtJ35NT4KKJxbpb_jlnae-5fX-c0hUJiB5QLBan7_qvIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_Cj60bjjQQeU5eetjK2CntsJOOaCvDqqQOy4oWK441DMFHQpjR52vCbt58KMKbDqvoD-Jc3M04X-o9-hvT-54e2p3FBUQjjbbaQft20b0vhx67L6va5gJ0_R7jWhkhDq72y5jvQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCet5_tJn4OV-582R7_KJO1MtbOq4IOqxby26nRbJR9aJ5y-J7nhb68j6oU0hKUQqoX5hLfam3ion3vQpbZ8h5a-tcHyjDF3H5ptp5M-HTGKl0MLPbrSj6zQJ8Vy6kq5UnMBMPtamOnaIQc3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFGDT05j5cBeU5eetjK2CntsJOOaCv4HCbOy4oWK441DMcULT5RLTcABhcE3hcaeqvo56bk3M04X-o9-hvT-54e2p3FBUQJJ-JpQft20b0mWRru54PLyIOQQn7jWhkhDq72y5jvQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCtJ58eJnKqVbcaa4JSfJrpq6_Wq4tehH4L0fn9WDTOQJ7Ttn6RSKQe0bjxqfIDQP6DKxnibJ7Z-pbwBpKWJtKw35O4Xlj0QbjMhnOK3mkjbPb7yfTYHJkzW-nSK-4syP4t2xRnWnciKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJzJCcjqR8Zj5uhej5P; BCLID_BFESS=7512001008843199905; H_BDCLCKID_SF_BFESS=tJFqoI0aJCt3H48k-4QEbbQH-UnLq-Q9WmOZ04n-ah02DDoM0xOJhtTX5fT2L6bLW20j0h7m3UTdsq76Wh35K5tTQP6rLtJ35NT4KKJxbpb_jlnae-5fX-c0hUJiB5QLBan7_qvIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_Cj60bjjQQeU5eetjK2CntsJOOaCvDqqQOy4oWK441DMFHQpjR52vCbt58KMKbDqvoD-Jc3M04X-o9-hvT-54e2p3FBUQjjbbaQft20b0vhx67L6va5gJ0_R7jWhkhDq72y5jvQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCet5_tJn4OV-582R7_KJO1MtbOq4IOqxby26nRbJR9aJ5y-J7nhb68j6oU0hKUQqoX5hLfam3ion3vQpbZ8h5a-tcHyjDF3H5ptp5M-HTGKl0MLPbrSj6zQJ8Vy6kq5UnMBMPtamOnaIQc3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFGDT05j5cBeU5eetjK2CntsJOOaCv4HCbOy4oWK441DMcULT5RLTcABhcE3hcaeqvo56bk3M04X-o9-hvT-54e2p3FBUQJJ-JpQft20b0mWRru54PLyIOQQn7jWhkhDq72y5jvQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCtJ58eJnKqVbcaa4JSfJrpq6_Wq4tehH4L0fn9WDTOQJ7Ttn6RSKQe0bjxqfIDQP6DKxnibJ7Z-pbwBpKWJtKw35O4Xlj0QbjMhnOK3mkjbPb7yfTYHJkzW-nSK-4syP4t2xRnWnciKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJzJCcjqR8Zj5uhej5P; BDSFRCVID_BFESS=-FKOJexroG0mWT6DPvT-JmGJqeKKv3JTDYLE8yu9T4VNR5DVgxpaEG0Pt_ZYMak-XolpogKK5mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=8ha5202k000l24a185a7kook1hfn8b617; ZFY=BIF1Nc7nkjwFwf6Eww8SGlN:Ak:A0laRSoaSUOUnq2WVs:C; BAIDUID_BFESS=9D5654968E19555DE2ED2D6444894C9B:FG=1; delPer=0; PSINO=7; H_PS_PSSID=36556_36624_36981_36918_36569_37105_37137_37055_26350_36861_22159; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1660744416; ab_sr=1.0.1_MjM5YTIxZDczZTg2NTA3YTE1Mzc2ZDEzNjc3ZmNmOWQ0YTQ3NzBlY2RmMmRhNmRiMGE2Zjc0NzBjODkwMDQ1ZjIwNzY4MDQxMjgzM2RlNjc4MDc1NTllOWZlNzdlYjNmZjA5YWYxMDZlOGFkNjg4MWJjN2M2OTI2OTExNWM5Yjk4Mzg1ODg3NTkyNTA1N2U1NzI5YjIzMjI5MWMxNGZlOQ==",
            "Host": "fanyi.baidu.com", "Origin": "https://fanyi.baidu.com",
            "Referer": "https://fanyi.baidu.com/?aldtype=16047",
            "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
            "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"macOS\"", "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/104.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }

        yield scrapy.FormRequest(url=url, headers=headers, formdata=form_data, callback=self.response_parse)

    def response_parse(self, response):
        html_response: HtmlResponse = response
        # ILog.debug(__file__, html_response.text)
        response_object = JSONUtility.to_json_object(html_response.text)
        ILog.debug(__file__, response_object)


if __name__ == '__main__':
    cmdline.execute(f'scrapy crawl {SpiderBaidufanyiSpider.name}'.split())
