import random

name = input ("Whats your name?: ")
print("Hello, " + name +"!")
quest = input ("How are u?: ")
if quest == 'good':
    print("Nice to hear!")
elif quest == 'bad':
    print("Ohh, so sorry")
else:
    print("Please, send siml reply: 'bad, or good'")

quest1 = input ("Let's play a 'eagle and tail' game? (Y/N): ")
if quest1 == 'Y':
    print("Get starded")
    main = ''
    a = input("Choose: 'eagle' - O or 'tail' - T: ")
    if a == 'O':
        main = 'Eagle'
    elif a == 'T':
        main = 'Tail'
    zz=['Eagle', 'Tail']
    g=(random.choice(zz))
    if main == g:
        print(g)
        print("Nice, u won! :)")
    else:
        print (g)
        print("Oh, sorry, u lose :(")
elif quest1 == 'N':
    print("Cmooon...")
    