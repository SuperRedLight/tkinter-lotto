import tkinter
import tkinter.font
import random

# 1~46까지 랜덤으로 생성된 숫자를 lotto_num에 저장
lotto_num = range(1, 46)

# 버튼 옵션(버튼을 클릭하면 6자리수 난수를 생성)
def buttonClick() :
    print(random.sample(lotto_num, 6))

# tkinter 윈도우 창을 생성한다.
window = tkinter.Tk()
# 이 윈도우 창의 이름은 lotto
window.title("lotto")
# 이 윈도우 창의 크기는 400 x 200 이다.
window.geometry("400x200")
# 이 윈도우 창은 크기를 변경할 수 없다.
window.resizable(False, False)

# 윈도우 창 안에 버튼을 생성 한다, 버튼의 그림자 효과를 넣는다, 버튼안에 들어갈 문자는 "번호확인", 버튼 높이는 15, 버튼을 클릭하는 명령어, 문자 생성 딜레이 1000, 문자 생성 간격 100)
button = tkinter.Button(window, overrelief = "solid", text = "번호확인", width = 15, command = buttonClick, repeatdelay = 1000, repeatinterval = 100)
# 버튼을 생성한다.
button.pack()

#윈도우 창이 꺼지지 않게 계속 루프한다.
window.mainloop()