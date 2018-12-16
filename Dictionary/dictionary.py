import json
import difflib
from difflib import get_close_matches
data=json.load(open('data.json'))


while True:

    a=1
    word= input('\nEnter any word to know its meaning:\n')
    w=word.lower()
    tle=word.title()
    u=word.upper()
    if w in data:
        for i in data[w]:
            print(str(a)+". "+i)
            a=a+1
        t = input('\nEnter Y to continue N to exit \n')
        if t not in ['Y','y']:
            break
    elif tle in data:
        for i in data[tle]:
            print(str(a)+". "+i)
            a=a+1
        t = input('\nEnter Y to continue N to exit \n')
        if t not in ['Y','y']:
            break
    elif u in data:
        for i in data[u]:
            print(str(a)+". "+i)
            a=a+1
        t = input('\nEnter Y to continue N to exit \n')
        if t not in ['Y','y']:
            break
    elif len(get_close_matches(word,data.keys())) > 0:
        close=get_close_matches(word,data.keys())[0]
        print('\nDid you mean '+close+' ?' )
        test=input('\n If yes Enter Y else N:\n')
        if test in ['Y','y']:
            for i in data[close]:
                print(str(a) + ". " + i)
                a = a + 1
            t = input('\nEnter Y to continue N to exit \n')
            if t not in ['Y', 'y']:
                break
        else:
            c=0
            for i in get_close_matches(word, data.keys()):
                c=c+1
            b = 1
            while True:
                if c-b == 0:
                    print('\nNo suggestions left\n Your word might not exist')
                    break
                temp=input('\nFor more suggestions enter Y, to exit enter N \n')
                if temp in ['y','Y']:
                    close = get_close_matches(word, data.keys())[b]
                    print('\nDid you mean ' + close + ' ?')
                    b=b+1
                    test = input('\n If yes Enter Y else N:\n')
                    if test in ['Y', 'y']:
                        a=1
                        for i in data[close]:
                            print(str(a) + ". " + i)
                            a = a + 1
                        break

                else:
                    break

            t = input('\nEnter Y to continue N to exit \n')
            if t not in ['Y', 'y']:
                break
    else:
        print("\nword doesn't exist")
        t = input('\nEnter Y to continue N to exit \n')
        if t not in ['Y', 'y']:
            break
