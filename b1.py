print('''Enter your new password:
  
Must contain:
1. At least eight characters long
2. Has lower case and upper case letters.
3. Has numbers and letters.
''')
  
pass_verify = True
passReady = False

while pass_verify == True:
  enter_pass = input('New Password:        ')
  repass = input('Enter password again:')

  pass_match = True
  
  if enter_pass == repass:
    pass_match = True
  
  
  def hasNumbers(stringInput):
    return any(char.isdigit for char in stringInput)
  def hasUppers(stringInput):
    return any(char.isupper for char in stringInput)
  def passStrength(stringInput):
    return (len(stringInput))
  
  if hasNumbers(enter_pass) == True:
    if hasUppers(enter_pass) == True:
      if passStrength(enter_pass) > 8:
        if pass_match == True:
          passReady = True
  
  if passReady == True:
    print("Ready to Go!")
    break
  else:
    print("Invalid")
