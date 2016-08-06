from tkinter import *
import os

window = Tk()
window.title("Kookmin University Computer Science")

name = Frame(window)
name.grid(row=0, column=0, sticky=N)

Label(name,text="이름: ").grid(row=0, column=0, sticky=N)
display = Entry(name, width=20, bg="light green")
display.grid(row=0, column=1, sticky=N)

frame = Frame(window)
frame.grid(row=0, column=1, sticky=E)

infoList = {
    'score':{'title':'점수:', 'width':7, 'color':'light green'},
    'number':{'title':'번호:', 'width':5, 'color':'light green'},
    'files':{'title':'파일이름:', 'width':20, 'color':'light blue'}
}
infoListKey = ['score', 'number', 'files', 'files']
btnList = ['추가', '삭제', '저장', '열기']

sortBtn = Frame(window)
sortBtn.grid(row=1, column=0, columnspan=2)

sortBtnList = {
    "No":{"title":"번호순", "width":5, "func":0},
    "name":{"title":"이름순","width":5, "func":1},
    "scoreAsc":{"title":"점수내림차순", "width":15, "func":2},
    "scoreDesc":{"title":"점수오름차", "width":15, "func":3}
}
sortList=["No", "name", "scoreAsc", "scoreDesc"]

dataField = []
frameList = []
listNum = 1

def is_Number(input):
    try:
        if float(input):
            return True
    except ValueError:
        return False

def clear():
    state.delete("1.0", END)
    dataOut.delete("1.0", END)

def click(func):
    global listNum
    global dataField
    if func == btnList[0]: # 추가
        exist = 0
        state.delete("1.0", END)
        disName = display.get()
        disScore = frameList[0].get()

        if not disName == '' and is_Number(disScore):
            if dataField == []:
                dataOut.insert(END, '%d\t%s\t%s\n' % (listNum, disName, disScore))
                state.insert(END, '성공적으로 추가하였습니다.')
                temp = []
                temp.extend([listNum, disName, disScore])
                dataField.append(temp)

                display.delete(0, END)
                frameList[0].delete(0, END)
                listNum += 1
                print(dataField)
                print(listNum)
            else:
                for i in range(0, listNum-1):
                    if disName == dataField[i][1]:
                        exist += 1
                        print(dataField[i][1])
                if not exist > 0:
                    dataOut.insert(END, '%d\t%s\t%s\n' % (listNum, disName, disScore))
                    state.insert(END, '성공적으로 추가하였습니다.')
                    temp = []
                    temp.extend([listNum, disName, disScore])
                    dataField.append(temp)

                    display.delete(0, END)
                    frameList[0].delete(0, END)
                    listNum += 1
                    print(dataField)
                else:
                    state.insert(END, '[추가 실패] 동일한 이름이 이미 존재합니다.')
        else:
            state.insert(END, '[추가 실패] 이름이 공백 또는 점수가 숫자입니다.')

    elif func == btnList[1]: #삭제
        state.delete("1.0", END)
        indexNum = frameList[1].get()
        exist = 0
        if is_Number(indexNum) and eval(indexNum) < listNum:
            for i in range(0, listNum-1):
                print(dataField[i][0])
                if indexNum == str(dataField[i][0]):
                    exist = 1

            if exist == 1:
                dataOut.delete("1.0", END)
                del dataField[eval(indexNum)-1]
                for i in dataField:
                    dataOut.insert(END, '%d\t%s\t%s\n' % (i[0], i[1], i[2]))
                state.insert(END, '성공적으로 삭제하였습니다.')
                frameList[1].delete(0, END)
                print(dataField)
            else:
                state.insert(END, '삭제에 실패하였습니다.')
        else:
            state.insert(END, '올바른 번호로 입력해주세요')

    elif func == btnList[2]: # 저장
        state.delete("1.0", END)
        filename = frameList[2].get()
        if not filename == '':
            file = open('%s.txt' % filename, 'w')
            file.write(dataOut.get("1.0", END))
            state.insert(END, '성공적으로 저장하였습니다. (파일이름: %s)' % filename)
            frameList[2].delete(0, END)
        else:
            state.insert(END, '파일 저장에 실패하였습니다.')

        file.close()

    elif func == btnList[3]: # 열기
        clear()
        filename = frameList[3].get()
        if not filename == '' and os.path.exists('%s.txt' % filename):
            file = open('%s.txt' % filename, 'r')
            dataOut.delete("1.0", END)

            line = file.readline()
            tokline = line.split('\t')

            while tokline != ['\n']:
                numScore = tokline[2].split('\n')
                realScore = numScore[0]
                dataOut.insert(END, line)
                dataField.append([listNum, tokline[1], realScore])
                listNum = int(tokline[0]) + 1
                line = file.readline()

                if not line:
                    break

                tokline = line.split('\t')
            print(dataField); print(listNum)
            frameList[3].delete(0, END)
            state.insert(END, '성공적으로 파일을 읽었습니다.(파일 이름: %s)' % filename)
        else:
            state.insert(END, '파일 불러오기에 실패하였습니다.')

    elif func == sortList[0]: # 번호순
        clear()

        sortedField = sorted(dataField)
        print(sortedField)
        for i in range(0, listNum-1):
            dataOut.insert(END, '%s\t%s\t%s\n' % (sortedField[i][0], sortedField[i][1], sortedField[i][2]))

    elif func == sortList[1]: # 이름순
        clear()

        def sortName(index):
            return index[1]

        sortedField = sorted(dataField, key = sortName)
        print(sortedField)
        for i in range(0, listNum-1):
            dataOut.insert(END, '%s\t%s\t%s\n' % (sortedField[i][0], sortedField[i][1], sortedField[i][2]))

    elif func == sortList[2]: # 점수내림차순 / 높은 점수 우선
        clear()

        def sortScore(index):
            return index[2]

        sortedField = sorted(dataField, key = sortScore, reverse = True)
        print(sortedField)
        for i in range(0, listNum-1):
            dataOut.insert(END, '%s\t%s\t%s\n' % (sortedField[i][0], sortedField[i][1], sortedField[i][2]))

    elif func == sortList[3]: # 점수오름차순 / 낮은 점수 우선
        clear()

        def sortScore(index):
            return index[2]

        sortedField = sorted(dataField, key = sortScore)
        print(sortedField)
        for i in range(0, listNum-1):
            dataOut.insert(END, '%s\t%s\t%s\n' % (sortedField[i][0], sortedField[i][1], sortedField[i][2]))

    else:
        pass

# Generating Frames
rowNum = 0
for key in infoListKey:
    Label(frame, text = infoList[key]['title'])\
        .grid(row=rowNum, column=0, sticky=E)
    frameList.append(Entry(frame, width=infoList[key]['width'], bg=infoList[key]['color']))
    frameList[rowNum].grid(row=rowNum, column=1, sticky=W)
    rowNum += 1

# Generating Buttons
rowNum = 0
for buttons in btnList:
    def cmd(x = buttons):
        click(x)

    Button(frame, text = buttons, width = 10, command=cmd)\
        .grid(row=rowNum, column=3)
    rowNum += 1


# Generating SortButtons
colNum = 0
for key in sortList:
    def cmd(x = key):
        click(x)

    Button(sortBtn, text = sortBtnList[key]['title'], width = sortBtnList[key]['width'], command=cmd)\
        .grid(row=0, column=colNum, sticky=E)
    colNum += 1

# Generating Text Frames
data=Frame(window, width=750,height=10,bg="light yellow")
data.grid(row=2,column=0,columnspan=2)

dataOut=Text(data,width=75,height=10,wrap=WORD,background="light yellow")
dataOut.grid(row=0,column=0)

state=Text(data,width=75,height=1,bg="pink")
state.grid(row=1,column=0)