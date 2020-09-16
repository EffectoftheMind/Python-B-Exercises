def numberFun(a, b, c):

num_fam = False
  
  if a + b == c:
    num_fam = True
  elif b - a == c:
    num_fam = True
  elif a - b == c:
    num_fam = True
  elif a / b == c:
    num_fam = True
  elif a * b == c:
    num_fam = True
  else:
    num_fam = False
  return(num_fam)
  
print(1,numberFun(1, 2, 3))	 
print(2,numberFun(4, 5, 1))	   	 
print(3,numberFun(10, 2, 4))	    	
print(4,numberFun(9, 2, 18))	     
print(5,numberFun(9, 5, 14))	   	
print(6,numberFun(90, 25, 65))	   
print(7,numberFun(288, 16, 18))
print(8,numberFun(56, 5, 260))
print(9,numberFun(4, 65, 260))
