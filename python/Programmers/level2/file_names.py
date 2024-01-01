#2022.06.18
#[3차] 파일명 정렬

import re

def solution(files):
    lst = []
    for i, file in enumerate(files):
        header = re.split('[0-9]+', file)[0].upper()
        number = int(re.findall('[0-9]+', file)[0])
        lst.append((header, number, file))
    lst.sort(key = lambda x: (x[0], x[1]))
    return list(i[2] for i in lst)

# best 풀이
import re

def solution(files):

    def key_function(file):
        header, number = re.match(r"([a-z-. ]+)([0-9]{,5})", file).groups()
        return [header, int(number)]

    return sorted(files, key = lambda file: key_function(file.lower()))
    

    