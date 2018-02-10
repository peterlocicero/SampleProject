import urllib.request,re

def search():
    getObj = input("Enter an object you would like to see: ")
    lowObj = getObj.lower() #make all inputs lowercase
 
#the website I am trying to acess splits up the ascii pictures by the first letter
 
    subfolder = {'a': 'ab', 'b': 'ab', 'c': 'c', 'd': 'def',
             'e': 'def', 'f': 'def', 'g': 'ghi', 'h': 'ghi', 'i': 'ghi','j': 'jkl','k':'jkl',
             'l': 'jkl','m':'mno','n': 'mno', 'o': 'mno','p': 'pqr','q': 'pqr', 'r': 'pqr',
             's': 's','t': 't','u':'uvw','v':'uvw','w': 'uvw','x': 'xyz','y':'xyz','z':'xyz'}
    baseurl = 'http://www.ascii-art.de/ascii/{}/{}.txt'

    if lowObj[:1] in subfolder:
        f = urllib.request.urlopen(baseurl.format(subfolder[lowObj[:1]], getObj))
        print(baseurl.format(subfolder[lowObj[:1]], getObj))
    else:
        print("Error, {} starts with an invalid character".format(obj))


    art = str(f.read()).split('\\n')
    for line in art:
        print(line)


while True:
    search()
    restart = input('do you want to see something else?(y/n): \n').lower()
    if restart == ('n'):
        exit()
    elif restart == ('y'):
        continue
