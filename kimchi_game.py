from urllib import request
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
import requests
import random

# 함수명 : kimchi_game
# 전달인자 : 진행중인 순서 i
# 반환 값 : 없음
# 기능 : 게임 초기 세팅
#       블로그에서 여러 채소와 과일 이름들을 스크래핑 해온다.
#       이를 리스트로 추가하고, game 에서 사용될 리스트를 kimchi_game_start()에 전달한다.
def kimchi_game(i):
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
            # 위 리스트에 추가함.
            vegetables.append(veg_name.text.replace("\n", ""))

    kimchi_game_start(vegetables, i)

    for i in player_list:
        print(f"{i['player_name']}의 치사량까지 {i['player_life']} 남았다! (지금까지 {i['count']} 🍺)")


# 함수명 :  search_kimchi
# 전달인자 : kimchi_name (검색할 채소 혹은 과일의 이름 ex - 배추, 사과, 바나나)
# 반환 값 : bool
# 기능 : 구글에 전달받은 재료로 만든 김치를 검색하고,
#       검색 결과의 이미지에 alt 태그로 해당 김치가 있다면 True를 리턴한다.
def search_kimchi(kimchi_name):
    url = (f"https://www.10000recipe.com/recipe/list.html?q={kimchi_name} 김치&order=accuracy")
    response = requests.get(url)
    if response.status_code == 200:
        soup = (bs(response.text, "html.parser"))

    links = []
    links.extend(soup.find_all('div', class_="common_sp_caption_tit line2"))

    for link in links:
        if link.text:
            title = link.text
            if (kimchi_name + ' 김치') in title or (kimchi_name in title and '김치' in title):
                print(url)
                print(title)
                return True



# 함수명 :  kimchi_game_start(vegetables)
# 전달인자 : vegetables (컴퓨터가 쓸 과일, 채소 리스트), i (게임을 부른 사람)
# 반환 값 : None
# 기능 : 사용자에게 김치 재료를 입력받고
#       search_kimchi 에 전달하여 bool 값을 전달 받는다.
#       있다면 게임오버, 없다면 다음차례로 넘어간다.
def kimchi_game_start(vegetables, i):
    print("************************************************************")
    print("*                           RULE                           *")
    print("*    1. 만개의 레시피에 00 김치를 검색합니다.                    *")
    print("*    2. 00으로 만든, 혹은 00이 들어간 김치가 있는지 확인합니다.    *")
    print("*    3. 하나라도 있다면 패배, 없다면 다음 차례로 넘어갑니다.       *")
    print("*    4. 단 00 은 채소나 과일 이름이어야 합니다.                  *")
    print("*    5. 게임은 부른 사람부터 순서대로 갑니다.                    *")
    print("************************************************************")
    print("없을 것 같은 김치 재료를 하나 골라 '00 김치'를 입력해주세요! (ex : 브로콜리 김치!)")
    print("아 김치! 김치! 김치 게임 start!")
    used_answer = []
    # 입력 못 했을 시 기회 한번
    count = 1

    while True:

        if i % len(player_list):
            # 컴퓨터 플레이어들의 차례
            random_vegetable = random.choice(vegetables)
            print("%s : %s 김치" % (player_list[i]["player_name"], random_vegetable))
            if (random_vegetable not in used_answer):
                used_answer.append(random_vegetable)
                print("%s 🔍 김치 검색중....." % (random_vegetable))
                if search_kimchi(random_vegetable):
                    print("🌶️🌶️%s 김치 있다!🌶️🌶️" % (random_vegetable))
                    print("🥃아 누가누가 술을 마셔 %s이가 술을 마셔 원~~~~ 샷!🥃" % (player_list[i]["player_name"]))
                    player_list[i]["player_life"] -= 1  # 해당 순서 플레이어 목숨 하나 제거
                    player_list[i]["count"] += 1 # 해당 순서 플레이어 카운트 증가
                    return
                else:
                    print("%s 👏👏김치 없어!👏👏" % (random_vegetable))
                    i += 1  # 다음 차례로 이동
            else:
                print("이미 누가 %s 김치 했어!" % (random_vegetable))
                print("😝아 병x샷! 아 병x샷!😝")
                player_list[i]["player_life"] -= 1  # 해당 순서 플레이어 목숨 하나 제거
                player_list[i]["count"] += 1 # 해당 순서 플레이어 카운트 증가
                return

        # player 차례일 때
        else:
            # input_answer = input("%s : "%(player.name)).split() # 플레이어 이름 받기
            while True:
                kimchi = input("%s : " % (player_list[0]['player_name'])).split()
                try:
                    veg_name = kimchi[0]
                    if kimchi == "":
                        raise Exception('입력하지 않았습니다. ')
                    if (veg_name not in used_answer):
                        used_answer.append(veg_name)
                        print("%s 🔍 김치 검색중....." % (veg_name))
                        if search_kimchi(veg_name):
                            print("🌶️🌶️%s 김치 있다!🌶️🌶️" % (veg_name))
                            print("🥃아 누가누가 술을 마셔 %s이가 술을 마셔 원~~~~ 샷!🥃" % (player_list[0]['player_name']))
                            player_list[0]["player_life"] -= 1  # 플레이어 목숨 하나 제거
                            player_list[0]["count"] += 1 # 플레이어 카운트 증가
                            return
                        else:
                            print("%s 👏👏김치 없어!👏👏" % (veg_name))
                            i += 1  # 다음 차례로
                            break
                    else:
                        print("이미 누가 %s 김치 했어!" % (veg_name))
                        print("😝아 병x샷! 아 병x샷!😝")
                        player_list[0]["player_life"] -= 1  # 플레이어 목숨 하나 제거
                        player_list[0]["count"] += 1  # 플레이어 카운트 증가
                        return
                except Exception as e:
                    # 한번의 미입력은 기회 제공
                    if count == 1:
                        print("🤣부끄러워하지 말고, 김치 이름 말해줘!🤣")
                        count -= 1
                    # 타이밍을 놓치면~ 벌주!
                    else:
                        print("😝아 병x샷! 아 병x샷!😝")
                        player_list[0]["player_life"] -= 1  # 플레이어 목숨 하나 제거
                        player_list[0]["count"] += 1  # 플레이어 카운트 증가
                        return

