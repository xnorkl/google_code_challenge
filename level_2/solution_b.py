import array as a

def solution(h, q):
  # solution(h: int, q: List[int]) -> List[int]
  max = (2**h+1) - 1
  nodes = list(reversed([ i for i in range(1, max)]))
  l_nodes = (max + 1)/2
  i_nodes = l_nodes - 1
  t = [nodes[0]]
  print(nodes)
  def btree(p, d):
    if d > 1:
      lc = (p + d) + (1 - c)
      rc = (p + d) + (c - 2)
      for i in [lc,rc]:
        t.append(nodes[i])
      btree(lc, d - 1, c + 1)
      btree(rc, d - 1, c + 1)
    else:
      return t



  btree(0,h,0)

  return t


print(solution(3,[1,2,3]))

