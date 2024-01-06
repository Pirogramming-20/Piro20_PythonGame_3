import random

person = [{'name' : '영희', 'life': 4}, {'name': 'p', 'life': 2}, {'name' : '철수', 'life': 3}, {'name' : '민희', 'life': 4}, {'name' : '도겸', 'life': 2}]

random.shuffle(person)

def russian_roulette():
    joker = person[0]['name']
    person_length = len(person) - 1

    if joker == 'p':
        pointer = ''
        print('당신은 조커입니다! 조커가 원하는 타이밍에 멈추면\n그때, 지목자가 지목한 사람이 탈락합니다!')
        while(True):
            pointer = int(input(f'지목할 사람을 지정하세요 (1 ~ {person_length}): '))
            if 1 <= pointer <= person_length:
                break
            else:
                print('다시입력합시다!')

        while(True):
                computer_pointer = random.randrange(0, person_length + 1)

                now = int(input(f'두근...두근...{person[pointer]['name']}(이)가 정한것 같다...지금 멈출까? ( 0 : 지금 멈춘다, 1 : 아니 지금 멈출 순 없다!) : '))
                if now == 0 or now == 1:
                    if now == 1:
                        continue
                    else:
                        next_joker = person[computer_pointer]
                        next_joker['life'] -=  1
                        print(f'짠! {next_joker['name']}(이)가 걸렸다!')
                        
                        for i in person:
                            print(f'{i['name']}의 치사량까지 {i['life']} 남았다!')
                        break
                else:
                    print('0 아니면 1만 선택하자!')
    else:
        print(f'{person[0]['name']}님이 조커입니다.\n조커가 멈춘 순간, 지목자가 지목한 사람이 탈락합니다!')

        for i in range(person_length + 1):
            print(f'{i}번 : {person[i]['name']}')
        
        while(True):
            next_joker = int(input('지목자로 선정되셨습니다. 누구를 죽일지(?) 골라보세요. '))
            if 0 <= next_joker <= person_length:
                computer_pointer = random.randrange(1,4)
                if computer_pointer == 1:
                    print(f'조커가 멈췄습니다! {person[next_joker]['name']}님의 치사량이 "1" 줄어듦니다')
                    person[next_joker]['life'] -= 1
                    for i in person:
                        print(f'{i['name']}의 치사량까지 {i['life']} 남았다!')
                    break
                else:
                    print('조커가 멈추지 않았습니다! 무섭네요 정말!')
            else:
                print('다시입력합시다!')

russian_roulette()