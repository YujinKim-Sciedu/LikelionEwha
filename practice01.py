problem1 = {'은진':'이화여대 멋사 대표님', '연주':'이화여대 멋사 회장님', 
            '두희':'멋사 대장','유진':'이화여대 멋사 튜터님'}

for word in problem1.keys() :
    print("다음은 누구에 대한 설명일까요?")
    print('"'+problem1[word]+'"')
    print ("(1)은진 (2)연주 (3)두희 (4)유진 ")
    answer = input()
    if answer == word :
        print("정답입니다!\n")
    else :
        print ("오답입니다!\n")

 