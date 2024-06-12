# Create a secret code language using python
'''
rule 1
If the word has more than 3 letters then append first letter to last

rule bonus
reverse the word

rule 2 
add random 3 letters infront and at last of the word
'''
def Check(word):
    if (word.islower() == True ):#and word.isalnum()==False or word.isalpha()==True):
        return 0
    else:
        raise ValueError ("Follow the rules")
def Encode():
    encoded_word=''
    # let the list of random letters be
    random=['bui','jdn','jvn','kjd','hfk','inc','JFv','HJF','Hfi','DuD','NCj','jcn','ksh','dhd','bui','jdn','jvn','kjd','hfk','inc','JFv','HJF','Hfi','DuD','NCj','jcn']
    word=input("Input a word to encode in secret code :-")
    Check(word)
    # rule 1
    if len(word)>=3:
        word=word+word[0]
        word=word[1:]
    # rule bonus
    for i in range(len(word)):
        encoded_word=encoded_word+word[len(word)-i-1]
    word=encoded_word
    # rule 2
    l = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    try:    
        num=l.index(word[1])
    except ValueError:
        print("Follow the Rules")
    encoded_word=random[num]+word+random[26-num]


    print(f'Here\'s the encoded word => {encoded_word}')
def Decode():
    decoded_word=''
    word=input("Input a word to decode in secret code :-")
    Check(word)
    word= word[3:-3]
    print(word)
    for i in range(len(word)):
        decoded_word=decoded_word+word[len(word)-i-1]
    print(decoded_word)

    if len(word)>=3:
        decoded_word=decoded_word[-1]+decoded_word
        decoded_word=decoded_word[:-1]
    
    print(f'Here\'s the decoded word => {decoded_word}')

try:
    process=int(input('''(Rule = only input in small letters and numbers not allowed)
What do you want to do
Encode (1)
Decode (2)
Ans = '''))
    match process:
        case 1:
            print("Lets encode the code")
            Encode()
        case 2:
            print("Lets Decode the code")
            Decode()
        case _:
            print ("Enter a number infront of the required case")
        

finally:
    print('Program Finished Successfully')
