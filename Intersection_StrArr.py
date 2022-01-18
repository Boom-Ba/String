def FindIntersection(strArr):
  # setOne= set((strArr[0]).split(', '))
  # setTwo= set((strArr[1]).split(', '))
  a= map (int, strArr[0].split(', '))
  b= map (int, strArr[1].split(', '))

  res=sorted(list(set(a) & set(b))) 
  return res

# keep this function call here 
print(FindIntersection(input()))
