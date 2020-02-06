import itertools
def solution(h, q):
  # solution(h: int, q: List[int]) -> List[int]

  def pair_siblings(p=-1, d=0, c=0):
    if p == -1:
      siblings.insert(c,[nodes[0]])
      pair_siblings(p=0, d=1, c=1)
    elif d < h:
      lc = p + 2**(h-d)
      rc = p + 1
      siblings.insert(c,[ nodes[lc], nodes[rc] ])
      pair_siblings(lc, d + 1, (2*c))
      pair_siblings(rc, d + 1, (2*c) + 1)

  def find_parents(q, siblings,parents=[]):
    btree = list(itertools.chain.from_iterable(siblings))
    for i in q:
      if i in btree:
        j = btree.index(i)
        if j == 0:
          parents.append(-1)
        else:
          p = int((j-1)/2)
          parents.append(btree[p])
    return parents

  max = (2**h+1) - 1
  nodes = list(reversed([ i for i in range(1, max)]))

  if not nodes:
    return [-1]

  # Create a list of siblings
  siblings=[]
  pair_siblings()

  return find_parents(q, siblings)

test = [1,2,3]
print(solution(5, [19, 14, 28]))
#print(solution(4, test))
print(solution(3, [7, 3, 5, 1]))
#print(solution(2, test))
print(solution(1, test))
print(solution(0, test))
#  def ptree(h,t,o,s=0):
#    for d in range(h):
#      n = 2**d
#      o.append([t[i] for i in range(s, n+s)])
#     s += n
#    return o
  #print(nodes)
  #print(ptree(h,t,o=[]))
