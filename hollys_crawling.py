from bs4 import BeautifulSoup
import urllib.request
import  pandas as pd

result = [] # 작업결과를 저장할 빈 리스트 선언
end_flag = 0

for page in range(1,100):
    if end_flag == 1:
        break
    hollys_url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' %page
    print(hollys_url)
    hollys_html = urllib.request.urlopen(hollys_url)
    soupHollys = BeautifulSoup(hollys_html, 'html.parser') #호출 결과값을 파싱한 html 저장
    tag_tbody = soupHollys.find('tbody')
    # print(tag_tbody)
    tag_tr = tag_tbody.find_all('tr') # 모든 tr 정보가 들어있는 리스트를 저장
    # print(tag_tr)
    for store in tag_tr: # 각 페이지당 10개의 대리점 정보가 stroe 저장되어 추출
        if len(store) == 3:
            end_flag = 1
            break
        store_td = store.find_all('td') # 각 tr 내의 td 정보를 리스트로 추출하여 저장
        store_sido = store_td[0].string # 대리점 시도
        store_name = store_td[1].string # 대리점 이름
        store_address = store_td[3].string # 대리점 주소
        store_phone = store_td[5].string # 대리점 전화번호

        result.append([store_name] + [store_sido] + [store_address] + [store_phone])

hollys_df = pd.DataFrame(result, columns=('대리점이름','대리점시도','대리점주소','전화번호'))

hollys_df.to_csv('할리스대리점정보.csv', encoding='cp949',mode='w',index=True)

