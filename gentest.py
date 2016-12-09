#!/usr/bin/env python3.5
import requests
from bs4 import BeautifulSoup
# class a(object):
#     x=1
#     gen=(x for _ in range(10))
#
# if __name__=="__main__":
#     print(list(a.gen))


# class a(object):
#     x=1
#     gen=(lambda x:(x for _ in range(10)))(x)
#
# if __name__=="__main__":
#     print(list(a.gen))

init_url='http://172.30.46.237:8800/PhonePlatform/test.html'
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"}
start_html = requests.get(init_url,headers=headers)
start_resource=BeautifulSoup(start_html.text,"lxml")
# urls=start_resource.find_all("a")
urls=start_resource.find_all("a")


#Because this demo for check deadlinks without whole environment to do it. And i am a lazy people
#so the below  fist for...in...\'s you can improve it.i will use other methods to finish this experience
number=0

# for link in urls:
#     check_url = link.get("href")
#     res_code=requests.get(check_url)
    # print(res_code.text)
    # if(res_code=='200'):
    #     print('Advertising balloon')
    # else:
    #     number=number+1
    #     print(number)

for link in urls:
    check_urls=link.get("href")
    res_out=requests.get(check_urls)
    #Now,you can assert use code,but as i know ,if you do it like this,some error you will be miss
    # print(res_out.status_code)
    if "必应" in (res_out.text):
        print('arrived')
    else:
        number=number+1
print('the bad access numbers %d : %s'%(number,check_urls))
