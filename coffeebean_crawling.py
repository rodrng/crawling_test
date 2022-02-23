import time

import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

wd = webdriver.Chrome('webdriver/chromedriver.exe')
result = []

# wd.get("http://www.naver.com")

for i in range(1,1000): # 커피빈 매장수만큼 반복
    wd.get('https://www.coffeebeankorea.com/store/store.asp')
    wd.execute_script("storePop2('%d')" %i) # 대리점 정보를 볼 수 있는 자바스크립트 호출
    time.sleep(1)
    try:
        bean_html = wd.page_source
        bean_soup = BeautifulSoup(bean_html, 'html.parser')
        # print(bean_soup)

        store_name_h2 = bean_soup.select("div.store_txt>h2")
        # print(store_name_h2[0].string) # 대리점 이름 저장 (인덱스 써줘야됨)
        store_name = store_name_h2[0].string

        store_info = bean_soup.select("div.store_txt>table.store_table>tbody>tr>td")
        # print(store_info[2])
        store_address = list(store_info[2]) # 대리점 주소 저장
        # print(store_address)
        store_address = store_address[0] # 대리점 주소만 추출 저장
        store_phone = store_info[3].string
        # print(store_phone)

        result.append([store_name] + [store_address] + [store_phone])
    except:
        print("{0}번 페이지는 없는 대리점페이지입니다.".format(i))

bean_df = pd.DataFrame(result, columns=('대리점이름', '대리점주소', '전화번호'))
bean_df.to_csv('커피빈대리점목록.csv', encoding='cp949', mode='w', index=True)