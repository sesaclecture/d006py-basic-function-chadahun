def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if not b == 0:
        return a / b
    else:
        print('0으로 나눌 수 없슴다')


def power(base, pow):
    return base ** pow


def square(base):
    return power(base, pow=2)


def greet(이름="낯선자", 나이=20):
  
    
    if 나이 == 20:
        return f'안녕하신가 {이름}!'
    elif 나이 == 50:
        return f'안녕하십니까 {이름}!'
    else:
        return f'안녕 {이름}!'