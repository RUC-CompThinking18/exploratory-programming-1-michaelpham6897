#Input for the function
numlist = [2, 6, 5, 11, 8, -5, -3, 2]
print(numlist)

def half(numlist):
  #Checks if the input is a list
  if type(numlist) != list:
    return "Please enter a list."
  #The for loop will iterate through the list
  for i in numlist:
    numlist / 2 == i
    return i
