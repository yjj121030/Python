"""
从西刺爬取免费透明的代理IP(只爬取第一页，数量应该为50，返回形式为
"{'HTTP': '163.125.69.146:8888'}"的一个字典，返回的结果是从爬取的50各种随机抽取一个)
"""

import random
import urllib.request
from bs4 import BeautifulSoup

__all__ = ["getIp"]


def getIp():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0",
        "Referer": "https://www.xicidaili.com/nn/",
        "Cookie": "BAIDUID=F660214629B549A8C8C22F50416150B7:FG=1; BIDUPSID=F660214629B549A8C8C22F50416150B7; PSTM=1540432706; HMACCOUNT=03EE5D782043D96A; BDUSS=X4teUpSZGxxVUNwZmNuaEFzfnFsazlDYjFFSjRGY3ZMMXpMRHF3ZnRlOVVFdmxiQVFBQUFBJCQAAAAAAAAAAAEAAACwLQs30Ka~tMLkyNWy0NH0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFSF0VtUhdFbU; H_PS_PSSID=1447_21125_20697_28557_28608_28584_28604_28626_28605; HMVT=6bcd52f51e9b3dce32bec4a3997715ac|1552614124|; delPer=0; PSINO=1"
    }
    req = urllib.request.Request(
        url="https://www.xicidaili.com/nt/", headers=headers)
    response = urllib.request.urlopen(req)
    ip_proxy = []
    if response.getcode() == 200:
        html = response.read()
        soup = BeautifulSoup(html, features="lxml")
        ip_list = soup.find_all("tr", class_="odd")
        for ips in ip_list:
            ip = ips.find_all("td")
            ip_proxy.append((ip[5].text+","+ip[1].text+":"+ip[2].text))
    else:
        print("请求失败")
    proxy = random.choice(ip_proxy)
    Ip = {}
    Ip[str(proxy).split(",")[0]] = str(proxy).split(",")[1]
    return Ip


if __name__ == '__main__':
    print(getIp())
