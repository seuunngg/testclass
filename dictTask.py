#%% dict test
numdict = {'even': [2,4,6],'odd':[1,3,5]}
for i in numdict['even']:
    print(i)
    
numlistdict = {'1학년':[[30,40,50],[80,90,100]]}
for i in numlistdict['1학년']:
    for j in i:
        print(j)
    print('============')
#%% dict task 학생 관리
# 학생 이름과 학생 점수를 입력받고
# 추가, 수정, 삭제, 목록

title = '학생 성적 관리 프로그램\n'
msg = '1.추가\n2.수정\n3.삭제\n4.목록\n5.나가기\n'
errMsg = '다시 시도해주세요.'

studentDict = {}
subjectlist = {'국어','영어','수학'}

while True:
    choice = int(input(title + msg))
    #추가
    if choice == 1:
        name = input('학생 이름: ')
        if name not in studentDict:
            studentDict[name] = input('다음과 같이 각 점수를 입력하세요.\n예)국어,영어,수학').split(",")
        else:
            print('이미 등록된 학생입니다.')
    
    #수정
    elif choice == 2:
        choice = int(input('1.학생명\n2.점수\n'))
        name = input('수정할 학생명: ')
        if choice == 1:
        if name in studentDict:
            new = input('새로운 학생명: ')
            #기존 학생을 삭제하기 전
            #점수를 임시로 담아 놓는다.
            scorelist = studentDict[name]
            #기존학생 삭제후 새롭게 추가될 학생 추가(점수는 그대로)
            del studentDict[name]
            studentDict[new] = scorelist
        else:
            print('존재하지 않는 학생입니다.')
        elif choice == 2:
            choice = int(input('1.국어점수\n2.영어점수\n3.수학점수'))
            studentDict[name][choice-1] = int(input('새로운 점수: '))
    
    #삭제
    elif choice == 3:
        name = input('삭제할 학생명: ')
        if name in studentDict:
            del studentDict[name]
        else:
            print('존재하지 않는 학생입니다.')
    
    #목록
    elif choice == 4:
        for i in studentDict.keys():
            print('[' + i + ']'])
            for j in studentDict[i]:
                print(subjectlist[] + ':' + str(j) + '점')
                cnt += 1
    
    #나가기
    elif choice == 5:
        break
    
    #에러
    else:
        print(errMsg)



















