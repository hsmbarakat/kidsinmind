import requests
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
newlinks= []
url = 'https://kids-in-mind.com/search-desktop.htm?fwp_paged='
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
with open ('kidsinmind.txt','w',encoding='utf-8') as r:

    for page in range(1,258):
        response= requests.get(url+str(page), headers = headers)

        soup = bs(response.content, 'html5lib')

        itemstr= soup.findAll('div',{'class':'fwpl-result'})

        for item in itemstr:
            for link in item.findAll('a'):
                links= link.get('href')
                r.write (links)
                r.write('\n')



                # with open('kidsinmind.txt', 'r') as f:
                #     for line in f:
                #         inner_list = [elt.strip() for elt in line.split(',')]
                #         # in alternative, if you need to use the file content as numbers
                #         # inner_list = [int(elt.strip()) for elt in line.split(',')]
                #         print(inner_list)
                #         # b= newlinks.append(inner_list)
                #         # print(b)




                # for i in [links]:
                #     newlinks.append(i.strip())
                #     print(newlinks)
                #     print(len(newlinks))

                # print(links)
                # print(links)
                # r.write( '"' + links + '"' + ',')
                # r.write('\n')
                # newlinks.append(links)
                # # print(newlinks)
                # for i in newlinks:
                #
                #
                #     response2 = requests.get(i, headers=headers)
                #     soup2 = bs(response2.text, 'html5lib')
                #     for page2 in range(4, 12):
                # #         container = soup2.find('div', {'class': 'et_pb_text_' + str(page2)})
                # #     #
                #         print(container.text)


