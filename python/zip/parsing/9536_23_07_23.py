#여우는 어떻게 울지?

#문자열, 파싱
import sys
t = int(input())

for _ in range(t):
    sounds = list(input().split())

    while 1:
        tmp = list(input().split())
        if len(tmp) > 3:
            for i in range(len(sounds)):
                if i != len(sounds)-1:
                    print(sounds[i], end = " ")
                else:
                    print(sounds[i])
            break
        else:
            sounds = [sound for sound in sounds if sound != tmp[-1]]