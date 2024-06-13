import sys
import re
input = sys.stdin.readline

html = input().rstrip()
divisions = list(html.split("<div "))
for i in range(1, len(divisions)):
    division = divisions[i]
    title = re.findall('title="([\s|\S]+)"', division)[0]
    print("title :", title)
    
    paras = list(division.split("<p>"))
    for j in range(1, len(paras)):
        para = re.sub('</?[\w ]*>', "", paras[j])
        para = re.sub('[\s]+', " ", para).strip()
        print(para)

# 정답 풀이
import re
html = input()

# main 제거
html = re.sub('<main>|</main>', "", html)
# 제목 처리, \1을 통해 첫 번째 그룹 활용
html = re.sub(r'<div title="([\w ]*)">', r'title : \1\n', html)
# </div> 제거
html = re.sub(r'</div>', '', html)

# <p> 제거
html = re.sub(r'<p>', "", html)
# </p> 제거
html = re.sub(r'</p>', '\n', html)

# 본문 속 태그들 제거
html = re.sub(r'</?[\w ]*>', '', html)
# 문장 처음과 끝 빈칸 제거
html = re.sub(r' ?\n ?', '\n', html)
html = re.sub(r' {2,}', ' ', html)

print(html)