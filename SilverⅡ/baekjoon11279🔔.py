#21.01.18
#11279: 최대 힙
import sys
N = int(input())
heap = [0]

def add(x):
  heap.append(x)
  idx = len(heap)-1
  while 1:
    if idx == 1 or x < heap[idx//2]:
      break
    else:
      heap[idx] = heap[idx//2]
      heap[idx//2] = x
      idx //= 2

def delete():
  print(heap[1])
  lst = heap[-1]
  heap[1] = lst
  del(heap[-1])
  idx = 1
  while 1:
    if len(heap) < idx*2 + 1:
      break
    elif len(heap) >= idx*2 + 2:
      if heap[idx*2] > heap[idx*2 + 1]:
        max = idx*2
      else:
        max = idx*2 + 1
      if lst < heap[max]:
        heap[idx] = heap[max]
        heap[max] = lst
        idx = max
      else:
        break
    elif lst < heap[idx*2 ]:
      heap[idx] = heap[idx*2]
      heap[idx*2] = lst
      idx = idx * 2
    else:
      break

for i in range(N):
  x = int(sys.stdin.readline())
  if x == 0:
    if len(heap) == 1:
      print(0)
    else:
      delete()
  else:
    add(x)