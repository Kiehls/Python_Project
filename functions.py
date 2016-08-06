import ui
from tkinter import *
btnList = ['추가', '삭제', '저장', '열기']
sortList=["No", "name", "scoreAsc", "scoreDesc"]

data = {}

def click(func):
    if func == btnList[0]: # 추가
        ui.display.insert(END, 'wow')
        # name = ui.display.get()
        # score = ui.display1.get()
        #
        # ui.display.delete(0, END)
        # ui.display.insert(END, name + ' ' + score)

    elif func == btnList[1]: # 삭제
        pass

    elif func == btnList[2]: # 저장
        pass

    elif func == btnList[3]: # 열기
        pass

    elif func == sortList[0]: # 번호순
        pass

    elif func == sortList[1]: # 이름순
        pass

    elif func == sortList[2]: # 점수내림차순
        pass

    elif func == sortList[3]: # 점수오름차순
        pass

    else:
        pass
