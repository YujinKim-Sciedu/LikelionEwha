class Likelion :
    def __init__(self, task, age, name):
        self.team = "이화여대 멋사 8기 운영진"
        self.task = task
        self.age = age
        self.name = name

    def intro(self):
        print("안녕하세요, %s 에서 %s 을(를) 맡고 있는 %d살 %s 입니다." %(self.team,self.task,self.age,self.name))


ej1 = Likelion("대표",24,"고은진")
yj1 = Likelion("회장",24,"송연주")
tg = Likelion("교육팀",23,"노태경")
ej2 = Likelion("교육팀",24,"이은지")
yj2 = Likelion("교육팀",23,"김유진")

ej1.intro()
yj1.intro()
tg.intro()
ej2.intro()
yj2.intro()

