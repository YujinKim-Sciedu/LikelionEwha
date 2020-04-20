class Grade :
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def s_grade(self) :
        if self.score >= 90 :
            self.grade = "A"
        elif self.score >= 80 :
            self.grade = "B"
        elif self.score >= 70 :
            self.grade = "C"
        else :
            self.grade = "D"
    def __str__(self) :
        return "%s : %c 등급" %(self.name,self.grade)

yujin = Grade("유진", 89)
yujin.s_grade()
print(yujin)