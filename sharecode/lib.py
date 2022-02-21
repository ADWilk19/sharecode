from unicodedata import name


def input1():
    n = input('Hello, what is your name?')
    j = input('What job do you hope to get once the bootcamp is over?')

    return n, j

def try_me(default=True):
    if default==True:
        n, j = input1()
        return f'Hello, {n}. Best of luck with your career as a {j}'
    else: 
        return 'Hello world'
