# Write a function that takes a list value as an argument and 
# returns a string with all the items separated by a comma and a space, 
# with and inserted before the last item. 
# For example, passing the previous spam list to the function would 
# return 'apples, bananas, tofu, and cats'. But your function should be able 
# to work with any list value passed to it.

def commaCode(listParam):
  returnString = ''

  for i in range(len(listParam) - 1):
    returnString += listParam[i] + ', '
    
  returnString += 'and ' + listParam[-1]

  print(returnString)

spam = ['apples', 'bananas', 'tofu', 'cats', 'cats']
commaCode(spam)