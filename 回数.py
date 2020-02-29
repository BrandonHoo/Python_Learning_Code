#方案一:
def is_palindrome(n):
    nn = str(n) #转成字符串
    return nn == nn[::-1] #反转字符串并对比原字符串返回true/false
print (list(filter(is_palindrome,range(1,1000))))
'''
#方案二:
print (list(filter(lambda n : str(n)==str(n)[::-1],range(1,1000)))) #str(n),同上

#方案三：
def is_palindrome(n):
      s = str(n)
      h = list(range((len(s))//2))
      for i in h:
          if s[i] != s[-(i+1)]:
             return False
      return True

#测试:
N = list(filter(is_palindrome,[1231, 121, 22, 1134341, 13431]))
'''