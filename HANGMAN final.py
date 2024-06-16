import csv
import random
def hangman():
    if c==1:
        print('HANGMAN STATUS:\n','-----')
    if c==2:
        print('HANGMAN STATUS:\n','''|\n|-----\n|\n|\n|\n|\n|''')
    if c==3:
        print('HANGMAN STATUS:\n','''|\n|-----\n|\n|\n|\n|\n|\n------''')
    if c==4:
        print('HANGMAN STATUS:\n','''|\n|-----|\n|     |\n|\n|\n|\n|\n------''')                
    if c==5:
        print('HANGMAN STATUS:\n','''|\n|-----|\n|     |\n|     O\n|\n|\n|\n------''')
    if c==6:
        print('HANGMAN STATUS:\n','''|\n|-----|\n|     |\n|     O\n|     |\n|     |\n|\n------''')
    if c==7:
        print('HANGMAN STATUS:\n','''|\n|-----|\n|     |\n|     O\n|    /|\n|     |\n|\n------''')
    if c==8:
        print('HANGMAN STATUS:\n','''|\n|-----|\n|     |\n|     O\n|    /|\\\n|     |\n|\n------''')
    if c==9:
        print('HANGMAN STATUS:\n','''|\n|-----|\n|     |\n|     O\n|    /|\\\n|    /|\n|\n------''')
    if c==10:
        print('HANGMAN STATUS:\n','''|\n|-----|\n|     |\n|     O\n|    /|\\\n|    /|\\\n|\n------''')
def show(letter,word,sub):
    s1=''
    for i in range(len(word)):
        if word[i]==letter:
            s1+=word[i]
        elif sub[i]=='-':
            s1+='-'
        else:
            s1+=sub[i]
    return s1
t='Y'
while True:
    t=input("Do you wanna Start?(Y/N):")
    if t in 'Yy':
        f=open(r"C:\Users\deyta\Pictures\pokemon.csv",'r',encoding='utf-8')
        read=csv.reader(f)
        r=[]
        for l in read:
            r.append(l)
        i=random.randint(0,600)
        s=(r[i][30]).upper()
        type1=r[i][36]
        type2=r[i][37]
        m='-'*len(s)
        c=0
        print("The name of the given Pokemon has",len(s),"characters:",m)
        print("The type(s) of the Pokemon are",type1,type2)
        
        while m!=s and c<10:
            inp=(input("Guess a letter:")).upper()
            if inp not in s:
                c+=1
                hangman()
                inp=print("Wrong guess!Try again")
                
            else:
                m=show(inp,s,m)
                print("Yes!The Pokemon name consists of the letter",inp,".")
                print(m)
        else:
            if c>=10:
                print("Sorry!You lost:(")
                print("The pokemon was",s)
            if m==s:
                print("Yay!You won:)")
    elif t in 'nN':
        break
    else:
        print("Incorrect Input")
print("See you again")

            

        
