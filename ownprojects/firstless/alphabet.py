alfavit = 'abcdefghigklmnopqrstuvwxyz'
users = int(input('put the amount of letters you want to change: '))
textuser = input('Enter your text that you want to convert into your changed alphabet: ')
def shifr(users,textuser):
    newalpha = alfavit[users:] + alfavit[:users]
    result = ''
    for i in textuser:
        if i in alfavit:
            index = alfavit.index(i)
            readyi = newalpha[index]
            result += readyi
    return result

def reshifr(users,textuser):
    newalpha = alfavit[users:] + alfavit[:users]
    result = ''
    for i in textuser:
        if i in alfavit:
            index = newalpha.index(i)
            readyi = alfavit[index]
            result += readyi
    return result

print('result', reshifr(users,textuser))
# 
