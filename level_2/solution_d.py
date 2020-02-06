import array as a

def solution(h, q):
  # solution(h: int, q: List[int]) -> List[int]
  max = (2**h+1) - 1
  nodes = list(reversed([ i for i in range(1, max)]))

  if not nodes:
    return nodes

  t = []

  def btree(p=-1, d=0, c=0):
    if p == -1:
      t.insert(c,[nodes[0]])
      btree(p=0, d=1, c=1)
    elif d < h:
      lc = p + 2**(h-d)
      rc = p + 1
      t.insert(c,[ nodes[lc], nodes[rc] ])
      btree(lc, d + 1, (2*c))
      btree(rc, d + 1, (2*c) + 1)

  btree()
  ans = []

  for i in q:
    if i in t:
      j = t.index(i)
      if j == 0:
        ans.append(-1)
      else:
        p = int((j-1)/2)
        ans.append(t[p])

  return t,ans

test = [1,2,3]
#print(solution(5, [19, 14, 28]))
print(solution(4, test))
print(solution(3, [7, 3, 5, 1]))
#print(solution(2, test))
#print(solution(1, test))
#print(solution(0, test))
#  def ptree(h,t,o,s=0):
#    for d in range(h):
#      n = 2**d
#      o.append([t[i] for i in range(s, n+s)])
#     s += n
#    return o
  #print(nodes)
  #print(ptree(h,t,o=[]))
