

def xtest(*argv, a = 10, b = 20):   # 함수의 매개변수 앞에 *가 있으면 가변 매개변수
    print(type(argv))
    print('length: ', len(argv))

    for i in argv:
        print(i)
    print(a, b)

xtest(a = 100, b = 200)
'''
<class 'tuple'>
length:  0
100 200
'''

t = {
    'a' : 300,
    'b' : 400
}
xtest(**t)  # 사전을 펼칠때는 * 2개
'''
<class 'tuple'>
length:  0
300 400
'''

xtest(1, 2, 3, 4, 5)
'''
<class 'tuple'>
length:  5
1
2
3
4
5
'''

xtest(1, 2, 3)   # tuple의 내용이 달라짐
'''
<class 'tuple'>
length:  3
1
2
3
'''

data = [1, 2, 3, 4, 5]
xtest(data) 
'''
<class 'tuple'>
length:  1
[1, 2, 3, 4, 5]
'''

data = [1, 2, 3, 4, 5]
xtest(*data)  # 펼침(spread) 연산자
'''
<class 'tuple'>
length:  5
1
2
3
4
5
'''

data = '1234'
xtest(data)
'''
<class 'tuple'>
length:  1
1234
'''

xtest(*data)
'''
<class 'tuple'>
length:  4
1
2
3
4
'''

data = 'mp4v'
xtest('mp4v')  # 문자열을 넘기겠다
'''
<class 'tuple'>
length:  1
mp4v
'''
xtest(*'mp4v')  # 문자열 컬렉션을 펼쳐서 넘기겠다
'''
<class 'tuple'>
length:  4
m
p
4
v
'''


