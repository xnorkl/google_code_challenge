##
#
# Example Solutions:
#  -- Python cases --
#Input:
#solution.solution("abcabcabcabc")
#Output:
#    4
#
#Input:
#solution.solution("abccbaabccba")
#Output:
#    2
import string
import random
from typing import List
class TooBiGofaSliceError(Exception):
  pass

def solution(s):
  #str -> int:
  if len(s) > 1:
      i = (s+s).find(s,1,-1)
  else:
      i = 0
  pattern = s[:i]
  return s[1:-1], i, pattern, s.count(pattern)

def solution_b(s):
  if len(s) > 1:
    i = (s+s).find(s,1,-1)
  else:
    i = 0
  ans = [s, i, s[:i]]
  return ans

def make_test() -> str:
  strsize = random.randint(0,10)
  subsize = random.randint(0,10)
  sub = ''.join(random.choice(string.ascii_lowercase) for x in range(subsize))
  pattern = ''.join(sub for x in range(strsize))
  return pattern

#test_casesA: List[str] = []
test_casesB: List[str] = ['abcabc','abccbaabccba','nma','','aaaaaa']
#solutionsA = []
#for x in range(10):
#  test_casesA.append(make_test())
#  solutionsA.append(solution_b(str(test_casesA[x])))
#
#solutionsB = [solution_b(x) for x in test_casesB]
#print("Solutions A \n\t{}\n".format(solutionsA))
#print("Solutions B \n\t{}\n".format(solutionsB))
#
#solutionsA = []
#for x in range(10):
#  solutionsA.append(solution(str(test_casesA[x])))
#
solutionsB = [solution(x) for x in test_casesB]
#print("Solutions A \n\t{}\n".format(solutionsA))
print("Test Cases \n\t{}\n Solutions \n\t{}\n".format(test_casesB,solutionsB))
