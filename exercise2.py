def list_avg(numlist) :
    sum=0
    for x in numlist :
        sum += x
    return sum/len(numlist)

input_score = input()
scores = input_score.split()
scorelist = []
for x in scores :
    scorelist.append(int(x))
    
print("평균 = ",list_avg(scorelist))