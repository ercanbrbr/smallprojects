MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'}

def smorse(word):
    results=""
    for letter in word:
        results+=MORSE_CODE_DICT[letter.upper()]
    return results

def bonus1():
    dictt={}
    f=open("../kelimelist.txt","r")
    wordlist=f.read().split("\n")
    for i in wordlist:
        if(smorse(i) in dictt):
            dictt[smorse(i)]+=[" "+i]
        else:
            dictt[smorse(i)]=[i]
    for i in dictt.items():
        if len(i[1])==13:
            print(i)




print(smorse("sos"))
print(smorse("daily"))
print(smorse("programmer"))
print(smorse("bits"))
print(smorse("three"))

a=bonus1()

# https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/