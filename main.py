import random
import requests
from bs4 import BeautifulSoup as bs
player_turn = 1
def UpDownGame(playerName) :
    titles = []
    url = "https://www.premierleague.com/tables"
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    result = soup.select(".league-table__team-name.league-table__team-name--long.long")
    print ("23/24 시즌 1월 7일 기준 PL 순위를 맞춰보자 !")
    for i in range(20):
        titles.append(result[i].getText())
    totalNum = 20
    guess_order = 0
    if (playerName == "Player"):
        teamName = ""
        while teamName not in titles:  # 올바른 팀 이름이 입력될 때까지 반복
            teamName = input("순위를 맞출 팀을 말하세요!: ")
            if teamName not in titles:
                print("잘못된 팀 이름입니다! 다시 입력해주세요.")
        player_num = 4
        now = 1
        startPoint = 1
        endPoint = 20
        print (teamName + "의 등수를 맞춰보자 !")
        while now < player_num:
            now = now +1
            guess_order = random.randint(startPoint, endPoint)
            print (startPoint, endPoint)
            print ("예상하는 등수는?" + str(guess_order))
            if (guess_order > titles.index(teamName)+1):
                print ("Up!")
                endPoint = guess_order-1
            elif guess_order < titles.index(teamName)+1:
                print ("Down!")
                startPoint = guess_order+1
            else:
                print ("정답!")
                break
        if guess_order == titles.index(teamName)+1 or now < player_num:
            #출제자가 마신다
            print(1)
        else:
            print(2)
            #나머지가 마신다
    else:
        teamName = titles[random.randint(0,totalNum-1)]
        player_num = 4

        now = 1
        startPoint = 1
        endPoint = 20
        print (teamName + "의 등수를 맞춰보자 !")
        while now < player_num:
            if now==player_turn:
                now = now + 1
                guess_order = int(input("예상하는 등수는? "))
                if (guess_order > titles.index(teamName)+1):
                    print ("Up!")
                    endPoint = guess_order-1
                elif guess_order < titles.index(teamName)+1:
                    print ("Down!")
                    startPoint = guess_order+1
                else:
                    print ("정답!")
                    break
            else:  
                now = now +1
                guess_order = random.randint(startPoint, endPoint)
                print (startPoint, endPoint)
                print ("예상하는 등수는?" + str(guess_order))
                if (guess_order > titles.index(teamName)+1):
                    print ("Up!")
                    endPoint = guess_order-1
                elif guess_order < titles.index(teamName)+1:
                    print ("Down!")
                    startPoint = guess_order+1
                else:
                    print ("정답!")
                    break
        if guess_order == titles.index(teamName)+1 or now < player_num:
            #출제자가 마신다
            print(1)
        else:
            print(2)
            #나머지가 마신다

    


UpDownGame("Players")

#player_num, player_turn, player이름만 적절히 변경해주면 될 듯 !