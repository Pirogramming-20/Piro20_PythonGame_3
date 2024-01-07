#좋아 게임
import random
myName=input('오늘 거하게 취해볼 당신의 이름은? :')
List=[{'name':myName,'soju':2},
      {'name':'하연','soju':4},
      {'name':'연서','soju':6},
      {'name':'예진','soju':8},
      {'name':'헌도','soju':10}]

def good_game():
    goodAnswer=['캌 퉤','나도 좋아']
    print('우리 술도 마셨는데 좋아 게임할까?')
    good_score=[0,0,0,0,0] #멤버별 거절당한 수
    lastGame=True #지난 답변이 긍정
    while True:
        game_out=False
        if lastGame:
            good_rand=random.randint(0,4)
            myTurn=List[good_rand]['name'] #공격하는 사람
        #컴퓨터가 공격
        if myTurn!=myName:
            while True:
                yourTurn=List[random.randint(0,4)]['name'] #공격받는 사람
                if myTurn!=yourTurn:
                    break
            #컴이 공격받음
            print(myTurn,':',yourTurn,'좋아!')
            if yourTurn!=myName:
                myAnswer=goodAnswer[random.randint(0,1)]
                print('->',yourTurn,':',myAnswer)
                if myAnswer==goodAnswer[0]: #캌 퉤
                    lastGame=False
                    for i, member in enumerate(List):
                        if member['name'] == yourTurn:
                            good_score[i] += 1
                            if good_score[i]==3:
                                game_out=True
                            break
                    break
                elif myAnswer==goodAnswer[1]:
                    lastGame=True
                    good_score=[0,0,0,0,0]

            #사용자가 공격받음
            else:
                while True:
                    myAnswer = input(f'->{yourTurn}: ')
                    if myAnswer==goodAnswer[0]:
                        lastGame=False
                        for i, member in enumerate(List):
                            if member['name'] == yourTurn:
                                good_score[i] += 1
                                if good_score[i]==3:
                                    game_out=True
                                break
                        break
                    elif myAnswer==goodAnswer[1]:
                        lastGame=True
                        good_score=[0,0,0,0,0]
                        break
                    else:
                        print("잘못된 대답입니다. '캌 퉤'와 '나도 좋아' 중에서 선택해주세요.")
                        continue
            if game_out:
                print('아 누가 술을 마셔 %s이(가) 술을 마셔'%List['name'][i])
                break
        #내가 공격하는 사람
        else:
            while True:
                print(myTurn,':')
                myAnswer=input()
                yourTurn=''
                for j in range(len(myAnswer)):
                    if myAnswer[j]==' ':
                        break
                    yourTurn+=myAnswer[j]
                myAnswer = goodAnswer[random.randint(0, 1)]
                print('->', yourTurn, ':', myAnswer)
                if myAnswer == goodAnswer[0]:
                    lastGame = False
                    for i, member in enumerate(List):
                        if member['name'] == yourTurn:
                            good_score[i] += 1
                            if good_score[i] == 3:
                                game_out = True
                            break
                    break
        if game_out:
            print('아 누가 술을 마셔 %s이(가) 술을 마셔'%List['name'][i])
            break
good_game()