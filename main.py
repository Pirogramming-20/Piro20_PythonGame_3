import random


# 머지할 때 지우기
my_name='예진'

player_list = [
    {'player_name': my_name, 'player_life': 3, 'record': 0},
    {'player_name': "명수", 'player_life': 2, 'record': 0},
    {'player_name': "재석", 'player_life': 3, 'record': 0},
    {'player_name': "준하", 'player_life': 3, 'record': 0}
]


# 더게임오브데스 함수
def theGameOfDeath():

    # 숫자 부를 사람 랜덤으로 정하기
    starter = random.randrange(0, len(player_list))
    player_list_length=len(player_list)

    # 각자 한 명 지목하기
    print("더!!!! 게임 오브 데쓰!!!!!")

    player_choice=[]

    for index, element in enumerate(player_list):
            if element['player_name']==my_name:
                print("=====지목리스트=====")
                for i in range(player_list_length):
                    print(f"  {i+1}번: {player_list[i]['player_name']}")
                while True:
                    try:
                        choice = int(input('지목할 사람(위의 리스트 참고): '))
                        if 1 <= choice<=player_list_length :
                            player_choice.append(choice-1)
                            print(f"당신 --> {player_list[choice-1]['player_name']}")
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
                        print(f"{element['player_name']} --> {player_choice[index]}")
                        break


    #총 쏘는 횟수 정하기
    if player_list[starter]['player_name']==my_name:
        while True:
                    try:
                        choice = int(input('총을 몇 번 쏠까요: (30번 이하)'))
                        if 1 <= choice<=30 :
                            break
                        else:
                            print('0보다 크고 30보다 작은 수를 입력하세요.')
                    except:
                        print('숫자를 입력하세요: ')
    else:
        choice= random.randrange(1,30)
        print(f"{player_list[starter]['player_name']}로부터 {choice} 번 쏩니다.🔫🔫🔫")

    #게임 진행 및 총 쏘는 것 프린트
    tern=starter
    for i in range(choice):
         print(f"{i+1}번: {player_list[tern]['player_name']}==>{player_list[player_choice[tern]]['player_name']}")
         tern=player_choice[tern]

    #결과 출력    
    print(f"{player_list[tern]['player_name']}이 한 잔 마셔")

    #마시는 것 처리
    player_list[tern]['player_life']-=1
    player_list[tern]['record']+=1

    print(f"{player_list[tern]['player_name']}는 {player_list[tern]['player_life']}잔 남았따")


theGameOfDeath()