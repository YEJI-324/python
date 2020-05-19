age = int(input("나이입력 : "))
a = True #파이썬에서는 불린 대문자 시작~~~~~!!!!!!!~~~~~!!!!!!!
while(a): #0이 아닌 숫자는 다 True로 취급, 내용이 있는 문자열
    if(age>=19) :
        print("주류 구입 가능")
        age = int(input("나이입력 : "))
    else:
        print("안됩니다")
        a=False
