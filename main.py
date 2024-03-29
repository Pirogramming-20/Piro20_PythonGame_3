import random
import requests
from bs4 import BeautifulSoup as bs
from pyfiglet import Figlet

player_list = []
player_name = ''


# player_list는 전역변수로 만들어서 어떤 함수에서든 조작이 가능하도록 만듦
# 그래서 모든 참여자가 게임을 선택해야 하는 조건때문에 player_list의 인덱스 수정은 어려움
# player_list는 임의로
# player_list = [{'player_name': '하연', 'player_life': 3, 'count': 0}, {'player_name': '은서', 'player_life': 4, 'count': 0} ...]
# 와 같은 구성으로 되어 있음.

def start():
    global player_list
    global player_name

    game_title = Figlet(font='slant')
    print(game_title.renderText('Archol Game!\n    Lets go!'))

    while True:
        a = input('게임을 진행할까요? (y/n) : ')
        if a == 'y':
            break
        else:
            print('다음에 봐요~')

    player_name = input('오늘 거하게 취해볼 당신의 이름은? : ')
    player_life = 0
    invite_friend = 0

    print('~~~~~~~~~~~~~~~🍺소주 기준 당신의 주량은?🍺~~~~~~~~~~~~~~~')
    print('   1. 소주 1잔')
    print('   2. 소주 2잔')
    print('   3. 소주 3잔')
    print('   4. 소주 4잔')
    print('   5. 소주 5잔')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    while True:
        try:
            player_life = int(input('당신의 치사량(주량)은 얼마만큼인가요? (1~5을 선택해주세요.) : '))
            if 1 <= player_life <= 5:
                break
            else:
                print('숫자를 다시 입력해주세요!')
        except ValueError:
            print('숫자를 다시 입력해주세요!')

    while True:
        try:
            invite_friend = int(input('함께 취할 친구들은 얼마나 필요하신가요? (사회적 거리두기로 인해 최대 3명까지 초대 할 수 있어요!) : '))
            if 1 <= invite_friend <= 3:
                break
            else:
                print('숫자를 다시 입력해주세요!')
        except ValueError:
            print('숫자를 다시 입력해주세요!')

    random_list = ['은서', '하연', '연서', '예진', '헌도']
    random.shuffle(random_list)

    player_list = [
        {'player_name': player_name, 'player_life': player_life, 'count': 0},
    ]

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    for i in range(invite_friend):
        life = random.randrange(1, 6)
        print(f"오늘 함께 취할 친구는 {random_list[i]}입니다! (치사량 : {life})")
        player_list.append({'player_name': random_list[i], 'player_life': life, 'count': 0})

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    for i in player_list:
        print(f"{i['player_name']}은(는) 지금까지 {i['count']} 🍺 치사량까지 {i['player_life']}")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def select_game():
    global player_list
    i = 0

    while not any(player['player_life'] <= 0 for player in player_list):
        print('~~~~~~~~~~~~~~~~~~~~오늘의 알코올 게임~~~~~~~~~~~~~~~~~~~~')
        print('   🍺 1. 러시안룰렛 게임')
        print('   🍺 2. 업다운 게임')
        print('   🍺 3. 더 게임 오브 데스 게임')
        print('   🍺 4. 좋아 게임')
        print('   🍺 5. 백종원 게임')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        try:
            # if i == (0 % (len(player_list) + 1)):
            if i%len(player_list) == 0:
                select_num = int(
                    input(f"{player_list[i % len(player_list)]['player_name']}이(가) 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨게임? : "))
            else:
                select_num = random.randrange(1, 6)
                print(f"{player_list[i % len(player_list)]['player_name']}이(가) {select_num}번을 선택했다!")
            if select_num == 1:
                russian_roulette()
            elif select_num == 2:
                UpDownGame(player_list[i % len(player_list)]['player_name'])
            elif select_num == 3:
                theGameOfDeath()
            elif select_num == 4:
                good_game()
            elif select_num == 5:
                baeck_game(i)
            else:
                print('다시 입력해주세요!')
                continue
        except ValueError:
            print('다시 입력해주세요!')

        i += 1


def russian_roulette():
    game_title = Figlet(font='slant')
    print(game_title.renderText('russian\n    roulette!'))
    joker = player_list[random.randrange(0, len(player_list))]['player_name']
    player_list_length = len(player_list) - 1

    if joker == player_name:
        pointer = ''
        print('당신은 조커입니다! 조커가 원하는 타이밍에 멈추면\n그때, 지목자가 지목한 사람이 탈락합니다!')
        while (True):
            try:
                pointer = int(input(f'지목할 사람을 지정하세요 (1 ~ {player_list_length}): '))
                if 1 <= pointer <= len(player_list):
                    break
                else:
                    print('다시입력합시다!')
            except:
                print('다시입력합시다!')

        while (True):
            computer_pointer = random.randrange(0, player_list_length + 1)

            try:
                now = int(input(
                    f"두근...두근...{player_list[pointer]['player_name']}(이)가 정한것 같다...지금 멈출까? ( 0 : 지금 멈춘다, 1 : 아니 지금 멈출 순 없다!) : "))
                if now == 0 or now == 1:
                    if now == 1:
                        continue
                    else:
                        next_joker = player_list[computer_pointer]
                        next_joker['player_life'] -= 1
                        next_joker['count'] += 1
                        print(f"짠! {next_joker['player_name']}(이)가 걸렸다!")
                        print("🤑아 누가누가 술을 마셔🤑 👉%s이가👈 술을 마셔 원~~~~ 샷!😛" % (next_joker['player_name']))

                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        for i in player_list:
                            print(f"{i['player_name']}의 치사량까지 {i['player_life']} 남았다! (지금까지 {i['count']} 🍺)")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        break
                else:
                    print('0 아니면 1만 선택하자!')
            except:
                print('0 아니면 1만 선택하자!')
    else:
        print(f"{player_list[random.randrange(1, len(player_list))]['player_name']}님이 조커입니다.\n조커가 멈춘 순간, 지목자가 지목한 사람이 탈락합니다!")

        for i in range(player_list_length + 1):
            print(f"{ i+ 1 }번 : {player_list[i]['player_name']}")

        while (True):
            try:
                next_joker = int(input('지목자로 선정되셨습니다. 누구를 죽일지(?) 골라보세요. '))
                if 1 <= next_joker <= len(player_list):
                    computer_pointer = random.randrange(1, 4)
                    if computer_pointer == 1:
                        print(f"조커가 멈췄습니다! {player_list[next_joker-1]['player_name']}님의 치사량이 '1' 줄어듭니다")
                        print("🤑아 누가누가 술을 마셔🤑 👉%s이가👈 술을 마셔 원~~~~ 샷!😛" % (player_list[next_joker-1]['player_name']))
                        player_list[next_joker-1]['player_life'] -= 1
                        player_list[next_joker-1]['count'] += 1
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        for i in player_list:
                            print(f"{i['player_name']}의 치사량까지 {i['player_life']} 남았다! (지금까지 {i['count']} 🍺)")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        break
                    else:
                        print('조커가 멈추지 않았습니다! 무섭네요 정말!')
                else:
                    print('다시입력합시다!')
            except:
                print('다시입력합시다!')


def UpDownGame(playerName):
    last_title = Figlet(font='slant')
    print(last_title.renderText('PL\n       Up and Down'))

    titles = []
    url = "https://www.premierleague.com/tables"
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    result = soup.select(".league-table__team-name.league-table__team-name--long.long")
    print("23/24 시즌 1월 7일 기준 PL 순위를 맞춰보자 !")
    for i in range(20):
        titles.append(result[i].getText())
    totalNum = 20
    guess_order = 0
    if (playerName == player_name):
        random_numbers = random.sample(range(20), 5)
        for i in range(5):
            print(i + 1, ". " + titles[random_numbers[i]])

        while True:
            try:
                number = int(input("1부터 5까지의 숫자를 통해 팀을 고르세요! : "))
                if number < 1 or number > 5:
                    print("1부터 5까지의 숫자만 입력해주세요.")
                else:
                    break
            except ValueError:
                print("숫자를 입력해주세요.")

        teamName = titles[random_numbers[number - 1]]
        player_num = len(player_list)
        now = 1
        startPoint = 1
        endPoint = 20
        print(teamName + "의 등수를 맞춰보자 !")
        while now < player_num:
            guess_order = random.randint(startPoint, endPoint)
            print("예상하는 등수는? " + str(guess_order))
            now = now + 1
            if (guess_order > titles.index(teamName) + 1):
                print("Up!")
                endPoint = guess_order - 1
            elif guess_order < titles.index(teamName) + 1:
                print("Down!")
                startPoint = guess_order + 1
            else:
                print("정답!")
                break
        if guess_order == titles.index(teamName) + 1 or now < player_num:
            print("정답을 맞췄다 ! 출제자 두 잔 !\n")
            print("🤑아 누가누가 술을 마셔🤑 👉%s이가👈 술을 마셔 원~~~~ 샷!😛" % (playerName))
            for i in player_list:
                if i['player_name'] == playerName:
                    i['player_life'] -= 2
                    i['count'] += 2
        else:
            print("정답을 맞추지 못했다 ! 출제자 제외 한 잔 !\n")
            print("🤑아 누가누가 술을 마셔🤑 👉%s 빼고 다👈 술을 마셔 원~~~~ 샷!😛" % (playerName))
            for i in player_list:
                if i['player_name'] != playerName:
                    i['player_life'] -= 1
                    i['count'] += 1
    else:
        teamName = titles[random.randint(0, totalNum - 1)]
        player_num = len(player_list)

        now = 1
        startPoint = 1
        endPoint = 20
        print(teamName + "의 등수를 맞춰보자 !")
        while now < player_num:
            if now == 1:
                now = now + 1
                guess_order = int(input("예상하는 등수는? "))
                if (guess_order > titles.index(teamName) + 1):
                    print("Up!")
                    endPoint = guess_order - 1
                elif guess_order < titles.index(teamName) + 1:
                    print("Down!")
                    startPoint = guess_order + 1
                else:
                    print("정답!")
                    break
            else:
                guess_order = random.randint(startPoint, endPoint)
                print("예상하는 등수는? " + str(guess_order))
                now = now + 1
                if (guess_order > titles.index(teamName) + 1):
                    print("Up!")
                    endPoint = guess_order - 1
                elif guess_order < titles.index(teamName) + 1:
                    print("Down!")
                    startPoint = guess_order + 1
                else:
                    print("정답!")
                    break
        if guess_order == titles.index(teamName) + 1 or now < player_num:
            print("정답을 맞췄다 ! 출제자 두 잔 !\n")
            print("🤑아 누가누가 술을 마셔🤑 👉%s이가👈 술을 마셔 원~~~~ 샷!😛" % (playerName))

            for i in player_list:
                if i['player_name'] == playerName:
                    i['player_life'] -= 2
                    i['count'] += 2
        else:
            print("정답을 맞추지 못했다 ! 출제자 제외 한 잔 !\n")
            print("🤑아 누가누가 술을 마셔🤑 👉%s 빼고 다👈 술을 마셔 원~~~~ 샷!😛" % (playerName))
            for i in player_list:
                if i['player_name'] != playerName:
                    i['player_life'] -= 1
                    i['count'] += 1

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in player_list:
        print(f"{i['player_name']}의 치사량까지 {i['player_life']} 남았다! (지금까지 {i['count']} 🍺)")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def theGameOfDeath():
    # 타이틀 출력
    deathgame = Figlet(font='slant')
    print(deathgame.renderText('The Game\n of death!'))

    # 숫자 부를 사람 랜덤으로 정하기
    starter = random.randrange(0, len(player_list))
    player_list_length = len(player_list)

    # 각자 한 명 지목하기
    print("더!!!! 게임 오브 데쓰!!!!!")

    player_choice = []

    for index, element in enumerate(player_list):
        if element['player_name'] == player_name:
            print("~~~~~~~~~~~~~~~~~~~~~~지목리스트~~~~~~~~~~~~~~~~~~~~~~")
            for i in range(player_list_length):
                print(f"  {i + 1}번: {player_list[i]['player_name']}")
            while True:
                try:
                    choice = int(input('지목할 사람(위의 리스트 참고): '))
                    if 1 <= choice <= player_list_length:
                        player_choice.append(choice - 1)
                        print(f"당신 --> {player_list[choice - 1]['player_name']}")
                        break
                    else:
                        print('리스트에 있는 숫자를 입력하세요.')
                except ValueError:
                    print('숫자를 입력하세요')
        else:
            while True:
                choice = random.randrange(0, player_list_length)
                if choice != index:
                    player_choice.append(choice)
                    print(f"{element['player_name']} --> {player_list[player_choice[index]]['player_name']}")
                    break

    # 총 쏘는 횟수 정하기
    if player_list[starter]['player_name'] == player_name:
        while True:
            try:
                choice = int(input('총을 몇 번 쏠까요: (30번 이하)'))
                if 1 <= choice <= 30:
                    break
                else:
                    print('0보다 크고 30보다 작은 수를 입력하세요.')
            except:
                print('숫자를 입력하세요: ')
    else:
        choice = random.randrange(1, 30)
        print(f"{player_list[starter]['player_name']}로부터 {choice} 번 쏩니다.🔫🔫🔫")

    # 게임 진행 및 총 쏘는 것 프린트
    turn = starter
    for i in range(choice):
        print(f"{i + 1}번: {player_list[turn]['player_name']}==>{player_list[player_choice[turn]]['player_name']}")
        turn = player_choice[turn]

    # 결과 출력
    print("🤑아 누가누가 술을 마셔🤑 👉%s이가👈 술을 마셔 원~~~~ 샷!😛" % (player_list[turn]['player_name']))

    # 마시는 것 처리
    player_list[turn]['player_life'] -= 1
    player_list[turn]['count'] += 1

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in player_list:
        print(f"{i['player_name']}의 치사량까지 {i['player_life']} 남았다! (지금까지 {i['count']} 🍺)")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def good_game():
    good_title = Figlet(font='slant')
    print(good_title.renderText('Like\n    Game!'))
    names_list = [person['player_name'] for person in player_list]
    goodAnswer = ['캌 퉤', '나도 좋아']
    print('우리 술도 마셨는데 좋아 게임할까?')
    good_score = [0, 0, 0, 0, 0]
    lastGame = True
    while True:
        game_out = False
        if lastGame:
            good_rand = random.randint(0, len(player_list) - 1)
            myTurn = player_list[good_rand]['player_name']
        if myTurn != player_name:
            while True:
                while True:
                    yourTurn = player_list[random.randint(0, len(player_list) - 1)]['player_name']
                    if yourTurn != myTurn:
                        break
                if yourTurn != player_name:
                    print(myTurn, ':', yourTurn, '좋아')
                    myAnswer = goodAnswer[random.randint(0, 1)]
                    print('->', yourTurn, ':', myAnswer)
                    if myAnswer == goodAnswer[0]:
                        lastGame = False
                        for i, member in enumerate(player_list):
                            if member['player_name'] == myTurn:
                                good_score[i] += 1
                                if good_score[i] == 3:
                                    game_out = True
                                break
                    elif myAnswer == goodAnswer[1]:
                        lastGame = True
                        good_score = [0, 0, 0, 0, 0]
                        break
                    if game_out:
                        break
                else:
                    while True:
                        print(myTurn, ':', yourTurn, '좋아')
                        myAnswer = input(f'->{yourTurn}: ')
                        if myAnswer == goodAnswer[0]:
                            lastGame = False
                            for i, member in enumerate(player_list):
                                if member['player_name'] == myTurn:
                                    good_score[i] += 1
                                    if good_score[i] == 3:
                                        game_out = True
                                    break
                        elif myAnswer == goodAnswer[1]:
                            lastGame = True
                            good_score = [0, 0, 0, 0, 0]
                            break
                        else:
                            print("잘못된 대답입니다. '캌 퉤'와 '나도 좋아' 중에서 선택해주세요.")
                        if game_out:
                            break
                if game_out:
                    break
        else:
            while True:
                print(myTurn, ':', end=' ')
                myAnswer = input()
                yourTurn = ''
                for j in range(len(myAnswer)):
                    if myAnswer[j] == ' ':
                        break
                    yourTurn += myAnswer[j]
                if myAnswer != yourTurn + ' 좋아':
                    print("'OO 좋아'의 형태로 다시 작성하세요")
                    continue
                if yourTurn not in names_list:
                    print('리스트에 없는 이름입니다')
                    print(' '.join(names_list), '중 다시 입력해주세요')
                    continue
                elif yourTurn == player_name:
                    print('본인은 선택할 수 없습니다 다시 입력해주세요')
                    break
                myAnswer = goodAnswer[random.randint(0, 1)]
                print('->', yourTurn, ':', myAnswer)
                if myAnswer == goodAnswer[0]:
                    lastGame = False
                    for i, member in enumerate(player_list):
                        if member['player_name'] == myTurn:
                            good_score[i] += 1
                            if good_score[i] == 3:
                                game_out = True
                            break
                elif myAnswer == goodAnswer[1]:
                    lastGame = True
                    good_score = [0, 0, 0, 0, 0]
                    break
                if game_out:
                    break
        if game_out:
            print("🤑아 누가누가 술을 마셔🤑 👉%s이가👈 술을 마셔 원~~~~ 샷!😛" % (player_list[i]['player_name']))
            break

    player_list[i]['player_life'] -= 1
    player_list[i]['count'] += 1

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in player_list:
        print(f"{i['player_name']}의 치사량까지 {i['player_life']} 남았다! (지금까지 {i['count']} 🍺)")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


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

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in player_list:
        print(f"{i['player_name']}의 치사량까지 {i['player_life']} 남았다! (지금까지 {i['count']} 🍺)")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

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

    titles = []
    titles.extend(soup.find_all('div', class_="common_sp_caption_tit line2"))

    links = []
    links.extend(soup.find_all('a', class_="common_sp_link"))

    i = 0

    for title in titles:
        if title.text:
            titlename = title.text
            link_url = "https://www.10000recipe.com/" + links[i].get('href')
            if ("백종원" + food_name) in titlename or ('백종원' in titlename and food_name in titlename):
                print(link_url)
                print(titlename)
                return True
        i += 1


# 함수명 :  baeck_game_start(foods, i)
# 전달인자 : foods (컴퓨터가 쓸 음식 리스트), i (게임을 부른 사람)
# 반환 값 : None
# 기능 : 사용자에게 음식을 입력받고
#       search_food 에 전달하여 bool 값을 전달 받는다.
#       있다면 게임오버, 없다면 다음차례로 넘어간다.
def baeck_game_start(foods, i):
    game_title = Figlet(font='slant')
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
                    print("🤑아 누가누가 술을 마셔🤑 👉%s이가👈 술을 마셔 원~~~~ 샷!😛" % (player_list[turn]["player_name"]))
                    player_list[turn]["player_life"] -= 1  # 해당 순서 플레이어 목숨 하나 제거
                    player_list[turn]["count"] += 1  # 해당 순서 플레이어 카운트 증가
                    return
                else:
                    print("👏👏 백종원 %s 없어!👏👏" % (random_food))
                    i += 1  # 다음 차례로 이동
            else:
                print("이미 누가 %s  했어!" % (random_food))
                print("😝아 병x샷! 아 병x샷!😝")
                player_list[i]["player_life"] -= 1  # 해당 순서 플레이어 목숨 하나 제거
                player_list[i]["count"] += 1  # 해당 순서 플레이어 카운트 증가
                return

        # player 차례일 때
        else:
            # input_answer = input("%s : "%(player.name)).split() # 플레이어 이름 받기
            while True:
                food = input("%s : " % (player_list[0]['player_name']))
                try:
                    if food == "":
                        raise Exception('입력하지 않았습니다. ')
                    if (food not in used_answer):
                        used_answer.append(food)
                        print("🔍 백종원 %s  검색중....." % (food))
                        if search_food(food):
                            print("🌶️🌶️ 백종원 %s 있다!🌶️🌶️" % (food))
                            print("🤑아 누가누가 술을 마셔🤑 👉%s이가👈 술을 마셔 원~~~~ 샷!😛" % (player_list[0]['player_name']))
                            player_list[0]["player_life"] -= 1  # 플레이어 목숨 하나 제거
                            player_list[0]["count"] += 1  # 플레이어 카운트 증가
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


start()
select_game()

last_title = Figlet(font='slant')
print(last_title.renderText('Game\n    over!'))