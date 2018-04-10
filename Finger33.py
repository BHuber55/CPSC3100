# Brennan Huber
# Finger Exercise pg 33
# Comparing Newton-Raphson and Bisection

def main():
    user = 25

    NR(user)
    Bisection(user)

def NR(user):
    count = 0
    epsilon = 0.01
    guess = user/2.0
    while abs(guess*guess - user) >= epsilon:
        guess = guess - (((guess**2) - user)/(2*guess))
        count += 1

    print 'Square root of ', user, ' is about ', guess
    print count, ' iterations to find the answer'

def Bisection(user):
    count = 0
    epsilon = 0.01
    step = epsilon**2
    guess = 0.0

    while abs(guess**2 - user) >= epsilon and guess <= user:
        guess += step
        count += 1

    if abs(guess**2 - user) >= epsilon:
        print 'failed'
    else:
        print 'Square root of ', user, ' is about ', guess
        print count, 'iterations to find the answer'

main()