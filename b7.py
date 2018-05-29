def scoresIncreasing(scoresList):

for x in range(len(scoresList) -1):
    if scoresList[x] <= scoresList[x+1]:
      increase_score = True
    else:
      return False
      
  return(increase_score)
  
  print(1,scoresIncreasing([1, 3, 4]))   
print(2,scoresIncreasing([1, 3, 2]))   
print(3,scoresIncreasing([1, 1, 4]))   
print(4,scoresIncreasing([1, 1, 2, 4, 4, 7]))
print(5,scoresIncreasing([1, 1, 2, 4, 3, 7]))
print(6,scoresIncreasing([-5, 4, 11]))
