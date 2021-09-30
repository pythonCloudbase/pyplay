
try:
    import winsound
except ImportError:
    import os
    def playsound(frequency,duration):
        #apt-get install beep
        #os.system('beep -f %s -l %s' % (frequency,duration))
        #install sox to use this
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, frequency))
else:
    def playsound(frequency,duration):
        winsound.Beep(frequency,duration)

import time

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


file1 = open('new_input.txt', 'r+')
content = file1.readlines()

output_text = ""

for f in content:
    for w in f:
        if w.upper() in MORSE_CODE_DICT.keys():
            print(MORSE_CODE_DICT[w.upper()])
            output_text += MORSE_CODE_DICT[w.upper()]

print(output_text)

for i in output_text:
    if (i=='.'):
        print(i)
        playsound(600,1000)
    else :
        print(i)
        playsound(500,2000)
    time.sleep(0.1)
