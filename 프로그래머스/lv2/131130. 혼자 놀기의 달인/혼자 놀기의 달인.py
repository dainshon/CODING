def solution(cards):
    answer = 0
    new_card = []
    length = []
    count = 0
    
    for card in cards:
        new_card.append([card, 0])
    
    def open(idx):
        nonlocal count
        if(new_card[idx][1]==0):
            new_card[idx][1]=1
            count+=1
            open(new_card[idx][0]-1)
    
        length.append(count)
        count = 0

    
    
    for i in range(len(cards)):
        if(new_card[i][1]==0):
            open(i)  # 인덱스가 인자로 들어감

    length.sort(reverse=True)
    answer = length[0]*length[1]
    
    return answer