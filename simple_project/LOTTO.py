import random as r

lotto = []
for i in range(7):
        x = r.randint(1,45)
        if x in lotto == True:
            i -= 1

        else:
            lotto.append(x)

print(lotto[:6], "보너스 숫자 : ",lotto[-1:])
