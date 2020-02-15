import requests
import re
import jieba
import wordcloud
from lxml import etree
import sys
import signal


# 强制退出不报错
def Quit(signum, frame):
    print('Quit')
    sys.exit()


signal.signal(signal.SIGINT, Quit)


def get_xml(data_id_url, oid):
    # data_id_url = "https://www.bilibili.com/bangumi/play/ep307446"
    list_url = "https://api.bilibili.com/x/v1/dm/list.so?oid=" + oid

    data_id_response = requests.get(data_id_url)
    data_id_response.encoding = 'utf-8'
    data_id_html = data_id_response.text

    name = re.findall(r'<title>(.*?)</title>', data_id_html, re.S)[0]
    name = name.replace(':', '')
    print(name)

    list_response = requests.get(list_url)

    with open('%s.xml' % name, mode='wb') as f:
        f.write(list_response.content)

    return name


data_id_url = input('请输入网址：')
oid = input('请输入oid：')
name = get_xml(data_id_url, oid)


def obtain_xml(name):
    html = etree.parse('%s.xml' % name, etree.HTMLParser())
    # 解析xml，获取内容
    results = html.xpath('//d//text()')
    return results


results = obtain_xml(name)


def count(results):
    danmustr = ''.join(element for element in results)
    words = list(jieba.lcut(danmustr))

    i = 0
    for word in words:
        if word == '宝藏':
            i = i + 1

    wc = wordcloud.WordCloud(width=1000, background_color='white', font_path='simfang.ttf', height=800)
    wc.generate(' '.join(words))
    wc.to_file(r'%s.png' % name)
    return i


numbers = count(results)

print("宝藏值为：%d" % numbers)
