print("BMI calculate")
weight=float(input("input your weight(kg)"))
height=float(input("input your height(m)"))
BMI=weight/(height**2)
print("your BMI is %s" %BMI)
if BMI>=30:
    print("삐빅 비만입니다.")
elif BMI>=25:
    print("삐빅 과체중입니다.")
elif BMI>=20:
    print("삐빅 정상입니다.")
else:
    print("아마도 저체중????????")
