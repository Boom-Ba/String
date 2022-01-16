#find longest substring of s with only k distinct characters
#s='abcbdbdbbdcdabd' ,k=2, longest substr is bdbdbbd, and only contains 2 distinct char 'b','d'
def longest_substring(s,k):
  left,right=0,0
  maxlen=0
  freq= [0]*128
  window =set()
  res=''
  for right in range(len(s)):
    window.add(s[right]) #add char into slide window 
    freq[ord(s[right])]+=1 #update the frequency array
    
    #'abc bdbdbbdcdabd' k=2
    # 012 3456789
    #if window is greater than k, we need to remove the left-most element in the window
    while len(window)>k:
      freq[ord(s[left])]-=1
      if freq[ord(s[left])]==0:
        window.remove(s[left])
      left+=1
    if len(s[left:right+1])> maxlen:
      maxlen=len(s[left:right+1])
      res=s[left:right+1]
  return res
longest_substring('abcbdbdbbdcdabd',2)
