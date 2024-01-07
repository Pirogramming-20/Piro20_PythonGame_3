import random
myName = input('오늘 거하게 취해볼 당신의 이름은? :')
List = [{'name': myName, 'soju': 2},
        {'name': '하연', 'soju': 4},
        {'name': '연서', 'soju': 6},
        {'name': '예진', 'soju': 8},
        {'name': '헌도', 'soju': 10}]
names_list = [person['name'] for person in List]

def good_game():
    goodAnswer = ['캌 퉤', '나도 좋아']
    print('우리 술도 마셨는데 좋아 게임할까?')
    good_score = [0, 0, 0, 0, 0]
    lastGame = True
    while True:
        game_out = False
        if lastGame:
            good_rand = random.randint(0, 4)
            myTurn = List[good_rand]['name']
        if myTurn != myName:
            while True:
                while True:
                    yourTurn = List[random.randint(0, 4)]['name']
                    if yourTurn != myTurn:
                        break
                if yourTurn != myName:
                    print(myTurn, ':', yourTurn, '좋아')
                    myAnswer = goodAnswer[random.randint(0, 1)]
                    print('->', yourTurn, ':', myAnswer)
                    if myAnswer == goodAnswer[0]:
                        lastGame = False
                        for i, member in enumerate(List):
                            if member['name'] == myTurn:
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
                            for i, member in enumerate(List):
                                if member['name'] == myTurn:
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
                if myAnswer!=yourTurn+' 좋아':
                    print("'OO 좋아'의 형태로 다시 작성하세요")
                    continue
                if yourTurn not in names_list:
                    print('리스트에 없는 이름입니다')
                    print(' '.join(names_list), '중 다시 입력해주세요')
                    continue
                elif yourTurn==myName:
                    print('본인은 선택할 수 없습니다 다시 입력해주세요')
                    break
                myAnswer = goodAnswer[random.randint(0, 1)]
                print('->', yourTurn, ':', myAnswer)
                if myAnswer == goodAnswer[0]:
                    lastGame = False
                    for i, member in enumerate(List):
                        if member['name'] == myTurn:
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
            print('아 누가 술을 마셔 %s(이)가 술을 마셔' % List[i]['name'])
            break
    # 결과 출력

good_game()