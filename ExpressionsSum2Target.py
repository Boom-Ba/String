##problem is to print all expressions to calculate a string input
#to get integer target
##input: string, target 
##output: list of string_expressions can reach to target
def solve(s_input,curr_pos, n, curr_value,t,curr_expression,res):
  if curr_pos==n:
    if curr_value ==t:
      res.append(curr_expression)
    return 
  
  for i in range(curr_pos, n):
    #remove space
    string_to_digits=s_input[curr_pos:i+1].strip('')
    curr=int(string_to_digits) #1,2,3 
    #first digit
    if curr_pos==0:
      solve(s_input,i+1, n, curr_value+curr,t,curr_expression+str(curr),res)
    else:
      solve(s_input,i+1, n, curr_value+curr,t,curr_expression+'+'+string_to_digits,res) or\
      solve(s_input,i+1, n, curr_value-curr,t,curr_expression+'-'+string_to_digits,res) or \
      solve(s_input,i+1, n, curr_value*curr,t,curr_expression+'*'+string_to_digits,res)or \
      solve(s_input,i+1, n, curr_value//curr,t,curr_expression+'//'+string_to_digits,res)    
if __name__=='__main__':
  s_input= '123'
  t =6
  res=[]
  curr_pos =0 
  n =len(s_input)
  curr_val =0
  curr_expression =''
  solve(s_input,curr_pos, n, 0,t,curr_expression,res)
  #print(res) [1*2*3, 1+2+3] 
