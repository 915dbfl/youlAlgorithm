#22.11.28
#트리 순회
#class4/실버1
#트리, 재귀

import sys
from collections import defaultdict

n = int(sys.stdin.readline())
tree = defaultdict(list)

def preorder(cur):
  print(cur, end = "")

  left, right = tree[cur]

  if left != ".":
    preorder(left)
  if right != ".":
    preorder(right)

def inorder(cur):
  left, right = tree[cur]

  if left != ".":
    inorder(left)
  print(cur, end = "")
  if right != ".":
    inorder(right)

def postorder(cur):
  left, right = tree[cur]

  if left != ".":
    postorder(left)
  if right != ".":
    postorder(right)
  print(cur, end = "")

for i in range(n):
  main, left, right = sys.stdin.readline().split()
  tree[main] = [left, right]

preorder("A")
print()

inorder("A")
print()

postorder("A")

#클래스 구현
import sys

class Node():
  def __init__(self, root, left, right):
    self.root = root
    self.left = left
    self.right = right

def preorder(cur):
  print(cur.root, end = "")
  if cur.left != ".":
    preorder(tree[cur.left])
  if cur.right != ".":
    preorder(tree[cur.right])

def inorder(cur):
  if cur.left != ".":
    inorder(tree[cur.left])
  print(cur.root, end = "")
  if cur.right != ".":
    inorder(tree[cur.right])

def postorder(cur):
  if cur.left != ".":
    postorder(tree[cur.left])
  if cur.right != ".":
    postorder(tree[cur.right])
  print(cur.root, end = "")

n = int(sys.stdin.readline())
tree = {}

for i in range(n):
  root, left, right = sys.stdin.readline().split()
  tree[root] = Node(root, left, right)

preorder(tree["A"])
print()

inorder(tree["A"])
print()

postorder(tree["A"])