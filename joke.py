#coding:utf8
import requests,random,re
from lxml import etree
useragent = [
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
]

headers = {
    "User-agent":random.choice(useragent)
}


proxies = { "http": "http://106.15.183.117:16818" }


def joke(url,pattern,data=None):
    if data is None:
        response = requests.get(url,headers = headers,proxies=proxies)
    else:
        response = requests.get(url,headers=headers,data=data,proxies=proxies)
    # response.encoding = 'utf-8'
    cont1 = response.content
    cont2 = etree.HTML(cont1)
    cont3 = cont2.xpath(pattern)
    return cont3


if __name__=="__main__":
    start_url_list = ["http://www.jokeji.cn/list_{}.htm".format(n) for n in range(1, 612)]
    base_url = "http://www.jokeji.cn"
    start_xpath = "//div[@class='list_title']/ul/li/b/a/@href"
    titles_xpath = "//div[@class='list_title']/ul/li/b/a"
    while True:
        try:
            for index,start_url in enumerate(start_url_list):
                print("第{}页".format(index+1))
                url_list = joke(start_url,start_xpath)

                for url in url_list:
                    #拼接url
                    target_url = base_url+ url
                    # con = requests.get(target_url,headers=headers)
                    # content = re.findall(r'<span id="text110">(.*?)</span>',con.text,re.S)
                    # for a in content:

                    joke_detail_xpath = "string(///div[@class='left_up']/ul/span[@id='text110']/p)"
                    content = joke(target_url, joke_detail_xpath)
                    # print(c)
                    # title = joke(start_url, titles_xpath)
                    # for t in title:
                    #     print(t.text)

                    print("_________________________________")
                    # with open("joke.txt","a") as f:
                    #     f.write(content)
        except:
            print("数据采集超时,重新发起请求...")
        continue


