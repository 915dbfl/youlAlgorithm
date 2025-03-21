# 30
import sys
input = sys.stdin.readline

class Country:
    def __init__(self, win, draw, lose):
        self.win = win
        self.draw = draw
        self.lose = lose

play = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],
        [1, 2], [1, 3], [1, 4], [1, 5],
        [2, 3], [2, 4], [2, 5],
        [3, 4], [3, 5],
        [4, 5]]

def game(countries, play_index):
    global correct
    if play_index > 14:
        correct = True
        return

    a, b = play[play_index]
    countryA = countries[a]
    countryB = countries[b]

    if countryA.win > 0 and countryB.lose > 0:
        countryA.win -= 1
        countryB.lose -= 1
        game(countries, play_index + 1)
        countryA.win += 1
        countryB.lose += 1
    
    if countryA.draw > 0 and countryB.draw > 0:
        countryA.draw -= 1
        countryB.draw -= 1
        game(countries, play_index + 1)
        countryA.draw += 1
        countryB.draw += 1
    
    if countryA.lose > 0 and countryB.win > 0:
        countryA.lose -= 1
        countryB.win -= 1
        game(countries, play_index + 1)
        countryA.lose += 1
        countryB.win += 1

correct = False
answer = []
for _ in range(4):
    result = list(map(int, input().split()))
    countries = []
    correct = False

    for i in range(6):
        base = 3 * i
        cwin = result[base]
        cdraw = result[base + 1]
        close = result[base + 2]
        if cwin + cdraw + close > 5:
            answer.append(0)
            break
        countries.append(Country(cwin, cdraw, close))
    else:
        game(countries, 0)
        answer.append(1 if correct else 0)

print(*answer)