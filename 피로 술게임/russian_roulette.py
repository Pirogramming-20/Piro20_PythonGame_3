import random
import requests
from bs4 import BeautifulSoup as bs

player_list = []
player_name = ''

# player_list는 전역변수로 만들어서 어떤 함수에서든 조작이 가능하도록 만듦
# 그래서 모든 참여자가 게임을 선택해야 하는 조건때문에 player_list의 인덱스 수정은 어려움
# player_list는 임의로
# player_list = [{'player_name': '하연', 'player_life': 3, 'record': 0}, {'player_name': '은서', 'player_life': 4, 'record': 0} ...]
# 와 같은 구성으로 되어 있음.

def start():
    global player_list
    global player_name
    while True:
        a = input('게임을 진행할까요? (y/n) : ')
        if a == 'y':
            break
        else:
            print('다음에 봐요~')

    player_name = input('오늘 거하게 취해볼 당신의 이름은? : ')
    player_life = 0
    invite_friend = 0

    print('1. 소주 1잔')
    print('2. 소주 2잔')
    print('3. 소주 3잔')
    print('4. 소주 4잔')
    print('5. 소주 5잔')

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
        {'player_name' : player_name, 'player_life' : player_life, 'record' : 0},
    ]

    for i in range(invite_friend):
        life = random.randrange(1,6)
        print(f"오늘 함께 취할 친구는 {random_list[i]}입니다! (치사량 : {life})")
        player_list.append({'player_name' : random_list[i], 'player_life' : life, 'record' : 0})
    
    for i in player_list:
        print(f"{i['player_name']}은(는) 지금까지 {i['record']} bill! 치사량까지 {i['player_life']}")

    

def select_game():
    global player_list
    i = 0

    while not any(player['player_life'] == 0 for player in player_list):
        print('오늘의 알코올 게임')
        print('1. 러시안룰렛 게임')
        print('2. 업다운 게임')
        print('3. 러시안룰렛 게임')
        print('4. 러시안룰렛 게임')
        print('5. 러시안룰렛 게임')

        
        try:
            if i == (0 % 5):
                select_num = int(input(f"{player_list[i % len(player_list)]['player_name']}이(가) 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨게임? : "))
            else:
                select_num = random.randrange(1, 6)
                print(f"{player_list[i % len(player_list)]['player_name']}이(가) {select_num}번을 선택했다!")
            if select_num == 1:
                russian_roulette()
            elif select_num == 2:
                UpDownGame()
            elif select_num == 3:
                russian_roulette()
            elif select_num == 4:
                russian_roulette()
            elif select_num == 5:
                russian_roulette()
            else:
                print('다시 입력해주세요!')
        except ValueError:
            print('다시 입력해주세요!')

        i += 1




def russian_roulette():
    joker = player_list[random.randrange(0, len(player_list))]['player_name']
    player_list_length = len(player_list) - 1

    if joker == player_name:
        pointer = ''
        print('당신은 조커입니다! 조커가 원하는 타이밍에 멈추면\n그때, 지목자가 지목한 사람이 탈락합니다!')
        while(True):
            try:
                pointer = int(input(f'지목할 사람을 지정하세요 (1 ~ {player_list_length}): '))
                if 1 <= pointer <= player_list_length:
                    break
                else:
                    print('다시입력합시다!')
            except:
                print('다시입력합시다!')

        while(True):
                computer_pointer = random.randrange(0, player_list_length + 1)

                try:
                    now = int(input(f"두근...두근...{player_list[pointer]['player_name']}(이)가 정한것 같다...지금 멈출까? ( 0 : 지금 멈춘다, 1 : 아니 지금 멈출 순 없다!) : "))
                    if now == 0 or now == 1:
                        if now == 1:
                            continue
                        else:
                            next_joker = player_list[computer_pointer]
                            next_joker['player_life'] -=  1
                            print(f"짠! {next_joker['player_name']}(이)가 걸렸다!")
                            
                            for i in player_list:
                                print(f"{i['player_name']}의 치사량까지 {i['player_life']} 남았다!")
                            break
                    else:
                        print('0 아니면 1만 선택하자!')
                except:
                    print('0 아니면 1만 선택하자!')
    else:
        print(f"{player_list[0]['player_name']}님이 조커입니다.\n조커가 멈춘 순간, 지목자가 지목한 사람이 탈락합니다!")

        for i in range(player_list_length + 1):
            print(f"{i}번 : {player_list[i]['player_name']}")
        
        while(True):
            try:
                next_joker = int(input('지목자로 선정되셨습니다. 누구를 죽일지(?) 골라보세요. '))
                if 0 <= next_joker <= player_list_length:
                    computer_pointer = random.randrange(1,4)
                    if computer_pointer == 1:
                        print(f"조커가 멈췄습니다! {player_list[next_joker]['player_name']}님의 치사량이 '1' 줄어듦니다")
                        player_list[next_joker]['player_life'] -= 1
                        for i in player_list:
                            print(f"{i['player_name']}의 치사량까지 {i['player_life']} 남았다!")
                        break
                    else:
                        print('조커가 멈추지 않았습니다! 무섭네요 정말!')
                else:
                    print('다시입력합시다!')
            except:
                print('다시입력합시다!')

def UpDownGame() :
    tester = player_list[random.randrange(0, len(player_list))]
    titles = []
    url = "https://www.premierleague.com/tables"
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    result = soup.select(".league-table__team-name.league-table__team-name--long.long")
    print (f"23/24 시즌 1월 7일 기준 PL 순위를 맞춰보자 ! \n 출제자는 {tester['player_name']}입니다!")
    for i in range(20):
        titles.append(result[i].getText())
    totalNum = 20
    title_answer = titles[random.randint(0,totalNum-1)]
    player_num = 4

    now = 1
    startPoint = 1
    endPoint = 20
    print (title_answer + "의 등수를 맞춰보자 !")
    while now < player_num:
        now = now +1
        guess_order = random.randint(startPoint, endPoint)
        print (startPoint, endPoint)
        print ("예상하는 등수는?" + str(guess_order))
        if (guess_order > titles.index(title_answer)+1):
            print ("Up!")
            endPoint = guess_order-1
        elif guess_order < titles.index(title_answer)+1:
            print ("Down!")
            startPoint = guess_order+1
        else:
            print ("정답!")
            break
            

    if guess_order == titles.index(title_answer)+1 or now < player_num:
        tester['player_life'] -= 1
        for i in player_list:
            print(f"{i['player_name']}의 치사량까지 {i['player_life']} 남았다!")
    else:
        for i in player_list:
            if i['player_name'] != tester['player_name']:
                i['player_life'] -= 1
        for i in player_list:
            print(f"{i['player_name']}의 치사량까지 {i['player_life']} 남았다!")
        #나머지가 마신다


start()
select_game()

print('종료~')