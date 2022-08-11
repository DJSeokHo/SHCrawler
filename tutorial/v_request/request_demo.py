# _*_ coding: utf-8 _*_
# @Time : 2022/08/09 10:15 PM
# @Author : Coding with cat
# @File : request_demo
# @Project : SHCrawler

from bs4 import BeautifulSoup

from framewrok.module.http.requests_wrapper.requests_wrapper import RequestsWrapper
from framewrok.utility.auth_code_utility import AuthCodeUtility
from framewrok.utility.json_utility import JSONUtility
from framewrok.utility.log_utility import ILog
from framewrok.utility.proxies_utility import ProxiesUtility


def __test_1():

    response_object = RequestsWrapper().url('https://www.baidu.com').proxies(ProxiesUtility.get_ssl_proxy()).get()
    ILog.debug(__file__, response_object.get_dictionary())


def __test_2():

    response_object = RequestsWrapper().url('https://www.baidu.com/s').headers({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.0.0 Safari/537.36 '
    }).query_params({
        'wd': '周杰伦'
    }).get()

    ILog.debug(__file__, response_object.get_dictionary())


def __test_3():

    response_object = RequestsWrapper().url('https://fanyi.baidu.com/sug').headers({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.0.0 Safari/537.36 '
    }).form_datas({
        'kw': 'hello'
    }).post()

    # ILog.debug(__file__, response_object.get_dictionary())
    ILog.debug(__file__, JSONUtility.to_json_object(response_object.get_data()).get("data"))


def __test_4():
    # 古诗文网
    # session
    # 绕过验证码登录
    """
    __VIEWSTATE: yb/qgTiQDaoGdGe4J78iieiLdmWrdQM7+QNgZUH2InCdawOV3IijXp9a8HTXMKNqsJjeBRf+q+uMr2jjcO5FbhLbWoMYwTq7hC773PHG92QZ4Q3Lb+rAAazwMjFOF4iSodtYuWqnxgq9zD4SnKr3ds6q9jY=
    __VIEWSTATEGENERATOR: C93BE1AE
    from: http://so.gushiwen.cn/user/collect.aspx
    email: djseokho@hotmail.com
    pwd: qwer12345 错误的密码可以捕获登录接口
    code: VQ1E
    denglu: 登录

    难点: __VIEWSTATE  __VIEWSTATEGENERATOR 是什么？ 一般情况下，查看页面源代码可以获得
    验证码怎么识别？
    """

    # 这里有坑，是无论如何都无法登录的，因为你之前打开了网页，下载了验证码，然后这里再发起一次登录的话，相当于第二次打开网页，那么肯定是新的验证码。
    # 存储的是之前的验证码，所以肯定无法打开。怎么办？ session 了解一下。
    wrapper = RequestsWrapper()\
        .url('https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx').headers({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/104.0.0.0 Safari/537.36 '
        }).session(True)

    response_object = wrapper.post()
    ILog.debug(__file__, response_object.get_dictionary())
    soup = BeautifulSoup(response_object.get_data(), 'html5lib')

    view_state = soup.select('#__VIEWSTATE')[0].attrs.get('value')
    view_state_generator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

    ILog.debug(__file__, view_state)
    ILog.debug(__file__, view_state_generator)

    code_image = soup.select('#imgCode')[0].attrs.get('src')
    code_image_url = f'https://so.gushiwen.cn{code_image}'

    # session 访问登录页下载验证码图片
    wrapper.download(url=code_image_url, file_name='image_code.jpg')
    res = AuthCodeUtility.auth_code_ocr('image_code.jpg')
    ILog.debug(__file__, res)

    wrapper.form_datas({
        '__VIEWSTATE': view_state,
        '__VIEWSTATEGENERATOR': view_state_generator,
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': 'djseokho@hotmail.com',
        'pwd': 'qwer1234',
        'code': res,
        'denglu': '登录'
    })

    # session 访问登录页进行登录
    response_object = wrapper.post()

    ILog.debug(__file__, response_object.get_dictionary())
    with open('gushiwen.html', 'w', encoding='utf-8') as fp:
        fp.write(response_object.get_data())


if __name__ == '__main__':
    # __test_1()
    # __test_2()
    # __test_3()
    __test_4()
