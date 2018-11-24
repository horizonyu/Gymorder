# coding=utf-8
# import urllib2
import urllib
import requests


def login(loginUrl, postdata, header):
    # req = urllib2.Request(
    #     url=loginUrl,
    #     data=postdata,
    #     headers=header
    # )
   #  result = urllib2.urlopen(req)
   #  response = result.info()
   #  print response
   # # return '振华' in responsez`
    s = requests.session()
    response = s.post(loginUrl, postdata, headers=header)
    return  response.text

header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Origin': 'https://newids.seu.edu.cn',
            'Referer': 'https://newids.seu.edu.cn/authserver/login?goto=http://my.seu.edu.cn/index.portal',
            'Cookie':'zg_did=%7B%22did%22%3A%20%22166e74de5900-0ebddf8aaff284-9393265-e1000-166e74de5951b9%22%7D; zg_8da79c30992d48dfaf63d538e31b0b27=%7B%22sid%22%3A%201541478933916%2C%22updated%22%3A%201541478951500%2C%22info%22%3A%201541478933924%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%7D; gr_user_id=591a7b5a-527f-4c86-aeec-de4759f9359d; amlbcookie=01; AMAuthCookie=AQIC5wM2LY4Sfcxys4vidajKyPsdpqyE22Resv9upRxXX%2Fg%3D%40AAJTSQACMDE%3D%23; gr_session_id_93fbdae88f63b950=f8e06eee-2b12-4da8-ad84-6cf36399e248; gr_session_id_93fbdae88f63b950_f8e06eee-2b12-4da8-ad84-6cf36399e248=true; JSESSIONID=0000TicrdjaElzIW-UySglgwq4x:19up4fjo1;'
        }
loginUrl = 'https://newids.seu.edu.cn/authserver/login?goto=http://my.seu.edu.cn/index.portal '
loginPostdata = {
            'username': '220184427',
            'password': '3e146f868cc3a2881175b668b1fb8347',
            'lt': 'LT-7396-mT5LdF2e4IphcfRoAOqjNdjfb5ZVtJ1541665865258-kSdB-cas',
            'dllt': 'userNamePasswordLogin',
            'execution': 'e1s1',
            '_eventId': 'submit',
            'rmShown': 1
        }

yuyueurl = 'http://yuyue.seu.edu.cn/eduplus/order/initOrderIndex.do?sclId=1'
posstdata = {
    'itemId':7,
    'dayInfo':'2018-11-08',
    'pageNumber':1
}

print(login(yuyueurl, postdata=posstdata, header=header ))