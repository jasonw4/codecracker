import random
import time

def fact(n):
  if n == 0:
    return True
  else:
    return n * fact(n-1)

def even(num):
  if num % 2 == 0:
    return True
  else: 
    return False


def c_even(password):
  count = 0
  for i in password:
    if even is True:
      count += 1

  
  return count

def sum(password):
  s = 0
  for i in password:
    s += int(i)

  return s

def product(password):
  producty = 1
  for x in password:
    producty *= int(x)
    return producty  


integer = random.randint(2,5)

chars = "1234567890"

password = random.sample(chars, integer)

lives = fact(integer)

sumz = sum(password)

print("LOADING")

time.sleep(random.randint(0,5))

password = ''.join(password)

print("Your code has been generated")

print('it is', integer ,'numbers long')
print('the sum is', sumz)
producty = product(password)
print('the product is', producty)
even = c_even(password)
print('The number of even numbers is', even)
print('The first number is', int(password[0]))
print('The last number is', int(password[-1]))
odd = integer - even
print('The number of odd numbers is', odd)
print('The highest number is', str(max(password)))
print('The lowest number is', str(min(password)))
print('you have', lives, 'lives') 

while lives > 0 :
  answer = input("Guess:")
  if answer == password:
    print("You're correct")
    break
  elif answer != password:
    print("Try again")
    lives -= 1
    if lives<=0:
      print("GGWP")
      break




