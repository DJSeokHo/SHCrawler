# _*_ coding: utf-8 _*_
# @Time : 2022/08/04 5:07 PM
# @Author : Coding with cat
# @File : url_demo_baidu
# @Project : SHCrawler
import ssl
import urllib.request
from http.client import HTTPResponse

from framewrok.utility.log_utility import ILog


def __test_1():
    url = "http://www.baidu.com/"
    response: HTTPResponse = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')

    ILog.debug(__file__, content)


def __test_2():
    url = "http://www.baidu.com/"
    response: HTTPResponse = urllib.request.urlopen(url)
    ILog.debug(__file__, type(response))  # <class 'http.client.HTTPResponse'>

    # 返回5个字节
    # content = response.read(5).decode('utf-8')
    # ILog.debug(__file__, content)

    # content = response.readline().decode('utf-8')
    # ILog.debug(__file__, content)

    # content: [] = response.readlines()
    # ILog.debug(__file__, content)

    code = response.getcode()
    ILog.debug(__file__, code)

    url = response.geturl()
    ILog.debug(__file__, url)

    headers: [] = response.getheaders()
    ILog.debug(__file__, headers)


def __test_3():
    """
    下载 网页，图片，视频
    :return:
    """

    ssl._create_default_https_context = ssl._create_unverified_context

    url = "http://www.baidu.com/"
    urllib.request.urlretrieve(url, 'baidu.html')

    image_url = "https://pbs.twimg.com/profile_images/1214465358981029888/H8xw2866_400x400.jpg"
    urllib.request.urlretrieve(url=image_url, filename='lisa.jpg')

    url_video = "https://vd2.bdstatic.com/mda-nh30qtb4dg7cy3y1/sc/cae_h264/1659573175809402548/mda-nh30qtb4dg7cy3y1.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1659605103-0-0-5130724d6bac03437182a5f02488022f&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=3303663310&vid=5929847066257230243&abtest=103525_1-103742_2-103890_1&klogid=3303663310"
    urllib.request.urlretrieve(url=url_video, filename='video.mp4')


if __name__ == '__main__':
    # __test_1()
    # __test_2()
    __test_3()
