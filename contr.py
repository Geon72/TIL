# 조건문 가지고 놀기
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 다양한 조건을 걸고 싶을 때 elseif인데 여긴 elif
pocket=['paper','cellphone']
card=True
if 'money' in pocket:
    print("택시 ㄱㄱ")
elif card:
    print("택시 ㄱㄱ")
else:
    print("걸어가쇼")

# while문 쓰기
treeHit = 0
while treeHit < 10:
     treeHit += 1
     print("나무를 %d번 찍었습니다." % treeHit)
     if treeHit == 10:
         print("나무 넘어갑니다.")

# while문 쓰기2
prompt="""
1.add
2.del
3.list
4.quit
enter number: """
number=0
while number !=4:
    print(prompt)
    number=int(input()) #사용자의 숫자 입력을 받아들이기/뒤에 내장함수에서 공부합시다

