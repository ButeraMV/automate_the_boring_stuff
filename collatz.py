# If number is even, then collatz() should print number // 2 and return this value. 
# If number is odd, then collatz() should print and return 3 * number + 1.
def collatz(number):
  if number % 2 == 0:
    print(number // 2)
    return(number // 2)
  else:
    print(3 * number + 1)
    return(3 * number + 1)

def collatz_sequence():
  print('Enter a number:')

  try:
    start = int(input())
    while start != 1:
      start = collatz(start)
  except:
    print('You have to enter an integer.')
    collatz_sequence()
    
collatz_sequence()