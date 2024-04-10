import sys
input = sys.stdin.readline

# 연산자 우선순위
# 1. ()
# 2. *, /
# 3. +, -

str = list(input().rstrip())
stack = []

rest = ""
for s in str:
    # 문자 이후 연산자가 나타나기 때문에 바로 추가
    if s.isalpha():
        rest += s
    else:
        if s == "(":
            stack.append(s)
        # 우선순위가 높은 연산자가 먼저 나온다.
        # */의 경우 우선순위가 제일 높으므로 같은 */만 확인
        elif s == "*" or s == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                rest += stack.pop()
            stack.append(s)
        # +-의 경우 우선순위가 가장 낮으므로 (가 아닌 모든 문자 확인
        elif s == "+" or s == "-":
            while stack and stack[-1] != "(":
                rest += stack.pop()
            stack.append(s)
        # ()는 출력되지 않음
        elif s == ")":
            while stack and stack[-1] != "(":
                rest += stack.pop()
            stack.pop()

while stack:
    rest += stack.pop()

print(rest)