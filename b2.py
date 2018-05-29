emailVerify = True

while emailVerify == True:
  user_email = input("Enter your email: ")
  
  def hasSpace(userInput):
    if " " in userInput:
      spaceIncluded = True
    else:
      spaceIncluded = False
    return(spaceIncluded)
  
  def punctError(userInput):
    if "." in userInput:
      punctIncluded = True
    else:
      punctIncluded = False
    return(punctIncluded)
    
  def atError(userInput):
    if "@" in userInput:
      atIncluded = True
    else:
      atIncluded = False
    return(atIncluded)
    
  hasSpace(user_email)
  punctError(user_email)
  atError(user_email)

  if hasSpace(user_email) == True:
    print("Do Not Include Spaces! Retry!")
  else:
    if punctError(user_email) == False:
      print("Please Add A Period! Retry!")
    else:
      if atError(user_email) == False:
        print("Please Add An @! Retry!")
      else: 
        print("Email Verified.")
        break
