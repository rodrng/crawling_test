from bs4 import BeautifulSoup

test_html = open('naver.test.html','r', encoding='utf-8')

soup = BeautifulSoup(test_html, 'html.parser')
# print(soup.prettify())

# print(soup.h1)

tag_h1 = soup.h1
tag_div = soup.div
# print(tag_div)
tag_ul = soup.ul
# print(tag_ul) # 여러개의 ul 태그 중 첫번째 ul태그만 출력됨
tag_li = soup.li
# print(tag_li) # 여러개의 li 태그 중 첫번째 li태그만 출력됨
tag_a = soup.a
# print(tag_a)
tag_ul_all = soup.find_all("ul") # 모든 ul 태그를 리스트형태로 반환
# print(tag_ul_all)
tag_li_all = soup.find_all('li')
# print(tag_li_all[2])
# print(tag_a.attrs) # 해당 태그의 속성이름과 속성값으로 dci 형태 변환
# print(tag_a['href']) # 해당 태그의 속성값만 출력
# print(tag_a['class'])

# print(soup.find('ul',attrs={'class':'section'})) # ul 태그 중에서 class가 section인 ul 만 출력(파싱)
h1_title = (soup.find(id='title'))
# print(h1_title.string)

li_list = soup.select('div>ul.section>li')
print(li_list)

# print(li_list[0].string) # 이렇게해도 출력되는데 아래와 같이 반복문으로 가능
# print(li_list[1].string)

for li in li_list:
    print(li.string)
