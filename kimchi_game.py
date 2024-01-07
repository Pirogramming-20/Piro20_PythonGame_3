# 함수명 : baeck_game
# 전달인자 : 진행중인 순서 i
# 반환 값 : 없음
# 기능 : 게임 초기 세팅
#       블로그에서 여러 음식 이름들을 스크래핑 해온다.
#       이를 리스트로 추가하고, game 에서 사용될 리스트를 baeck_game_start()에 전달한다.
def baeck_game(i):
    # 많은 음식들을 가져와서 저장해놓는 리스트. 컴퓨터가 사용할 것이다.
    foods = []
    # 이미 사용된 답변들 매 게임시 초기화 된다.
    used_answer = []

    # 여러 음식들을 나열해 놓은 블로그
    food_url = (f"https://cjhong.tistory.com/604")
    response = requests.get(food_url)
    if response.status_code == 200:
        soup = (bs(response.text, "html.parser"))
    pre_food_list = [span for span in soup.find_all('span') if not span.find() and span.text.strip()]

    for food_name in pre_food_list:
        if food_name.text and 2 <= len(food_name.text) <= 8:
            # 위 리스트에 추가함.
            foods.append(food_name.text.replace("\n", ""))
    while ". " in foods:
        foods.remove('. ')
    while ", " in foods:
        foods.remove(', ')
    foods.remove('by 청주홍')
    foods.remove('공유하기')
    foods.remove('게시글 관리')
    foods.remove('저작자표시')
    foods.remove('비영리')
    foods.remove('변경금지')
    foods.remove('찌개')
    foods.remove('전골')
    foods.remove('해산물')
    foods.remove('고기')
    foods.remove('메뉴')

    baeck_game_start(foods, i)

    for i in player_list:
        print(f"{i['player_name']}의 치사량까지 {i['player_life']} 남았다! (지금까지 {i['count']} 🍺)")


# 함수명 :  search_food
# 전달인자 : kimchi_name (검색할 채소 혹은 과일의 이름 ex - 배추, 사과, 바나나)
# 반환 값 : bool
# 기능 : 1000 레시피에 백종원 + 입력받은 음식 이름을 검색하고,
#       검색 결과의 제목에 백종원 이름과 음식이 있다면 True를 리턴한다.
def search_food(food_name):
    url = (f"https://www.10000recipe.com/recipe/list.html?q=백종원 {food_name}&order=accuracy")
    response = requests.get(url)
    if response.status_code == 200:
        soup = (bs(response.text, "html.parser"))

    links = []
    links.extend(soup.find_all('div', class_="common_sp_caption_tit line2"))

    for link in links:
        if link.text:
            title = link.text
            if ("백종원" + food_name ) in title or ('백종원' in title and food_name in title):
                print(url)
                print(title)
                return True



# 함수명 :  baedck_game_start(foods, i)
# 전달인자 : foods (컴퓨터가 쓸 음식 리스트), i (게임을 부른 사람)
# 반환 값 : None
# 기능 : 사용자에게 음식을 입력받고
#       search_food 에 전달하여 bool 값을 전달 받는다.
#       있다면 게임오버, 없다면 다음차례로 넘어간다.
def baeck_game_start(foods, i):
    game_title = Figlet(font='univers')
    print(game_title.renderText("Beack Game!   "))
    print("************************************************************")
    print("*                           RULE                           *")
    print("*    1. 만개의 레시피에 백종원 000를 검색합니다.                 *")
    print("*    2. 백종원의 00 음식 레시피가 있는지 확인합니다.              *")
    print("*    3. 하나라도 있다면 패배, 없다면 다음 차례로 넘어갑니다.        *")
    print("*    4. 단 00 은 음식 이름이어야 합니다.                        *")
    print("*    5. 다른 사람이 이미 말했던 음식은 제외해야합니다.             *")
    print("*    6. 게임은 부른 사람부터 순서대로 갑니다.                    *")
    print("************************************************************")
    print("백종원 법전 레시피가 없을 것 같은 음식을 하나 골라입력해주세요! (ex : 두루치기)")
    print("백종원 게임~~~ start!")
    used_answer = []
    # 입력 못 했을 시 기회 한번
    count = 1

    while True:
        turn = i % (len(player_list) + 1)
        if turn:
            # 컴퓨터 플레이어들의 차례
            random_food = random.choice(foods)
            print("%s : %s " % (player_list[turn]["player_name"], random_food))
            if (random_food not in used_answer):
                used_answer.append(random_food)
                print("🔍 백종원 %s 검색중....." % (random_food))
                if search_food(random_food):
                    print("🌶️🌶️ 백종원 %s 있다!🌶️🌶️" % (random_food))
                    print("🥃아 누가누가 술을 마셔 %s이가 술을 마셔 원~~~~ 샷!🥃" % (player_list[turn]["player_name"]))
                    player_list[turn]["player_life"] -= 1  # 해당 순서 플레이어 목숨 하나 제거
                    player_list[turn]["count"] += 1 # 해당 순서 플레이어 카운트 증가
                    return
                else:
                    print("👏👏 백종원 %s 없어!👏👏" % (random_food))
                    i += 1  # 다음 차례로 이동
            else:
                print("이미 누가 %s  했어!" % (random_food))
                print("😝아 병x샷! 아 병x샷!😝")
                player_list[i]["player_life"] -= 1  # 해당 순서 플레이어 목숨 하나 제거
                player_list[i]["count"] += 1 # 해당 순서 플레이어 카운트 증가
                return

        # player 차례일 때
        else:
            # input_answer = input("%s : "%(player.name)).split() # 플레이어 이름 받기
            while True:
                food = input("%s : " % (player_list[0]['player_name']))
                try:
                    if food == "":
                        raise Exception('입력하지 않았습니다. ')
                    if ( food not in used_answer):
                        used_answer.append(food)
                        print("🔍 백종원 %s  검색중....." % (food))
                        if search_food(food):
                            print("🌶️🌶️ 백종원 %s 있다!🌶️🌶️" % (food))
                            print("🥃아 누가누가 술을 마셔 %s이가 술을 마셔 원~~~~ 샷!🥃" % (player_list[0]['player_name']))
                            player_list[0]["player_life"] -= 1  # 플레이어 목숨 하나 제거
                            player_list[0]["count"] += 1 # 플레이어 카운트 증가
                            return
                        else:
                            print("👏👏 백종원 %s 없어!👏👏" % (food))
                            i += 1  # 다음 차례로
                            break
                    else:
                        print("이미 누가 %s 했어!" % (food))
                        print("😝아 병x샷! 아 병x샷!😝")
                        player_list[0]["player_life"] -= 1  # 플레이어 목숨 하나 제거
                        player_list[0]["count"] += 1  # 플레이어 카운트 증가
                        return
                except Exception as e:
                    # 한번의 미입력은 기회 제공
                    if count == 1:
                        print("🤣부끄러워하지 말고, 음식 이름 말해줘!🤣")
                        count -= 1
                    # 타이밍을 놓치면~ 벌주!
                    else:
                        print("😝아 병x샷! 아 병x샷!😝")
                        player_list[0]["player_life"] -= 1  # 플레이어 목숨 하나 제거
                        player_list[0]["count"] += 1  # 플레이어 카운트 증가
                        return