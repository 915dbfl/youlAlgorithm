#2022.03.07
#오픈채팅방

#내 풀이
def solution(record):
  answer = []
  result = []
  members = {}

  for str in record:
    words = str.split()
    if words[0] == "Enter":
      result.append([words[1], "들어왔습니다."])
      members[words[1]] = words[2]
    elif words[0] == "Leave":
      result.append([words[1], "나갔습니다."])
    else:
      members[words[1]] = words[2]
  for i in result:
    answer.append(members[i[0]] + "님이 " + i[1])
  return answer

#best 풀이
def solution(record):
  answer = []
  namespace = {}
  printer = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}

  for r in record:
    rr = r.split()
    if rr[0] in ['Enter', 'Change']:
      namespace[rr[1]] = rr[2]
  
  for r in record:
    if r.split()[0] != 'Change':
      answer.append(namespace[r.split()[1]] + printer[r.split()[0]])

  return answer