import random

# 1~46까지 랜덤으로 생성된 숫자를 lotto_num에 저장
lotto_num = range(1, 46)

#for문 변수 i에 6자리 난수를 5번 반복하여 저장한다.
for i in range(5) :
    #print문 lotto_num에 저장된 숫자를 출력한다!
    print(random.sample(lotto_num, 6))