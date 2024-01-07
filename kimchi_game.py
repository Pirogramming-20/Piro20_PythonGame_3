from urllib import request
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
import requests
import random

# 많은 야채들을 가져와서 저장해놓는 리스트. 컴퓨터가 사용할 것이다.
vegetables = ['오이', '당근', '자두', '메론', '락교']
# 이미 사용된 답변들 매 게임시 초기화 된다.
used_answer = []

# 여러 채소들을 나열해 놓은 블로그
veg_url = (f"https://soonsin.com/376")
response = requests.get(veg_url)
if response.status_code == 200:
    soup = (bs(response.text, "html.parser"))
pre_veg_list = [p for p in soup.find_all('p') if not p.find() and p.text.strip()]

for veg_name in pre_veg_list:
    if veg_name.text and len(veg_name.text) <= 4:
        vegetables.append(veg_name.text.replace("\n",""))


def search_kimchi(kimchi_name):

    url = (f"https://www.google.com/search?q={kimchi_name} 김치")
    response = requests.get(url)
    #print(url)
    if response.status_code == 200:
        soup = (bs(response.text, "html.parser"))
    # print("target_url = ",target_urls)
    # print("soups[0] = ", soups[0].prettify())
    links = []
    links.extend(soup.find_all('img'))

    #print(links)

    for link in links:
        # 이미지 태그에서 alt 속성이 있는지 확인하고 특정 내용을 찾는다.
        if 'alt' in link.attrs:
            alt_content = link['alt']
            if (kimchi_name + ' 김치') in alt_content or (kimchi_name in alt_content and '김치' in alt_content):
                return True

def kimchi_game_start():
    print("없을 것 같은 김치 재료를 하나 골라 '00 김치'를 입력해주세요! 단 채소나 과일 이름이어야 합니다.(ex : 브로콜리 김치!)")
    print("아 김치! 김치! 김치 게임 start!")
    used_answer = []
    # 입력 못 했을 시 기회 한번
    count = 1
    while True:
        # input_answer = input("%s : "%(player.name)).split() # 플레이어 이름 받기
        while True :
            kimchi = input("player: ").split()
            try:
                veg_name = kimchi[0]
                if (veg_name not in used_answer):
                    used_answer.append(veg_name)
                    print("%s 김치 검색중....."%(veg_name))
                    if search_kimchi(veg_name):
                        print("%s 김치 있다!" % (veg_name))
                        # print("아 누가누가 술을 마셔 %s가 술을 마셔 원~~~~ 샷!"%(player.name))
                        print("아 누가누가 술을 마셔 player가 술을 마셔 원~~~~ 샷!")
                        # player.life -= 1  #플레이어 목숨 하나 제거
                        return
                    else:
                        print("%s 김치 없어!" % (veg_name))
                        break
                else:
                    print("이미 누가 %s 김치 했어!" % (veg_name))
                    print("아 병x샷! 아 병x샷!")
                    # player.life -= 1  #플레이어 목숨 하나 제거
                    return
            except:
                if count == 1:
                    print("부끄러워하지 말고, 김치 이름 말해줘!")
                    count -= 1
                else:
                    print("아 병x샷! 아 병x샷!")
                    # player.life -= 1  #플레이어 목숨 하나 제거
                    return


        #컴퓨터 플레이어들의 차례
        for i in range(3):
            random_vegetable = random.choice(vegetables)
            print("player%d : %s 김치" % (i + 1, random_vegetable))
            if (random_vegetable not in used_answer):
                used_answer.append(random_vegetable)
                print("%s 김치 검색중....." % (random_vegetable))
                if search_kimchi(random_vegetable):
                    print("%s 김치 있다!" % (random_vegetable))
                    # print("아 누가누가 술을 마셔 %s가 술을 마셔 원~~~~ 샷!"%(player.name))
                    print("아 누가누가 술을 마셔 player가 술을 마셔 원~~~~ 샷!")
                    # player.life -= 1  #플레이어 목숨 하나 제거
                    return
                else:
                    print("%s 김치 없어!" % (random_vegetable))
            else:
                print("이미 누가 %s 김치 했어!" % (random_vegetable))
                print("아 병x샷! 아 병x샷!")
                # player.life -= 1  #플레이어 목숨 하나 제거
                return


kimchi_game_start()




