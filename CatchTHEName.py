#Hangman

import random
import re
def hollywood():
    x=random.choice(z)
    x = x.lower()
    x = x.replace(' ','/')
    main = ''
    chance = 5
    guessword= ''
    i = len(x)
    for item in range(i):
        if x[item] in 'aeiou/':
             main = main + x[item]
        else:
             main = main + " _ " 
    print('Guess the movie\n',main)
    p=1
    while(p):
        print('\n---------------------------')
        main=''
        z = input('Enter small letter or number in movie\t')        
        if z in 'qwrtypsdfghjklzxcvbnm7410852963':
            if z in guessword:
                print('Keyword used already')
                continue
            else:
                guessword = guessword + z
        else:
            print('Invalid input')
            continue
        for letter in x:
            if letter in guessword:
                main = main + letter
            elif letter in "aeiou/":
                main = main + letter
            else:
                main = main + " _ "


            
        if z not in x:
            print('WRONG!')
            chance = chance - 1
            if chance == 1:
                print(chance,"life remain")
            elif chance == 0:
                print('You lost')
                print('---------')
                print('|       |')
                print('| 0   0 |')
                print('|   0   |')
                print('|   __  |')
                print('|  |  | |')
                print('---------')
                print('Correct answer is',x)
                p = 0
            else:
                print(chance,"lives remains")
        if main == x:
            print(main)
            print('CONGRATS Oldsport')
            print('---------')
            print('|       |')
            print('| 0   0 |')
            print('|   0   |')
            print('|       |')
            print('|  |__| |')
            print('---------')
            print('You win with score of',chance)
            break
        print(main)
    return 0

user=input('Enter your name\n')
print('Welcome! to hollywood',user.title(),'\n---------------------------')
rule=input('Press 0 for rules and 1 to skip\t')
while(1):
    if '0' in rule:
        print('1. You have to guess the movie name.\n2. Vowels will be mentioned already.')
        print('3. If you type a vowel then one chance is deducted.\n4. You can go for HitnTrial if you do not know name.')
        print('5. You have only five chances if you put wrong alphabet.')
        input('Press any key to START the game\t')
    elif rule != '0' and rule != '1' :
        print('You entered invalid key')
        rule=input('Press 0 for rules and 1 to skip\t')
        continue
    break

print('HANGMAN tell me the movie name\nOr ready for execution\n')
s = 1
f = open("C:/Users/Ajay/Desktop/harsh/IOT/Ud_cours/names.txt", "r")
k=[]
k= re.split('\n|,',f.read())
z=[]
for word in k:
    if len(word)>0:
        z.append(word)
print(z)
    
while(s):
    hollywood()
    while(1):
        s = input('Press 1 to play again or 0 to exit\t')
        if s == '0':
            s = int(s)
            break
        elif s  == '1':
            s = int(s)
            print('+--------+')
            print('|        |')
            print('|NEW GAME|')
            print('|        |')
            print('+--------+')
            break
        else:
            print('Invalid key')
            continue
        
    




        

  
            
