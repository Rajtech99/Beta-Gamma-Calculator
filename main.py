# Import Statements
import sympy as sy
import time
import string

# Program Head
print("__Welcome to Beta-Gamma Calculator By Raj__\n")
print("This is a CLI based calculator that will help you to solve the n-th and n-th, m-th both value of Beta-Gamma functions.\nThis calculator is based on the Special form of Integration 0 to ∞ [{e^(-x) * x^(n-1)}dx] for Gamma(n) and 0 to 𝝅/2 [2*{Sin^(2m-1)(x) * Cos^(2n-1)(x)}dx] for Beta(m,n).\n")

time.sleep(2)

print("Default limits-\nFor Beta Function (0 to 𝝅/2)\nFor Gamma Function (0 to ∞)\n")
print("Select Your Work-Space:\n")
print("Enter g or G for use Gamma(n)\nEnter b or B for use Beta(m,n)\nEnter q or Q for Quit!\n")

# Main Body
work_space = input("Enter Option: ")

if work_space.isalpha():
  if work_space == 'g' or work_space == 'G':
    print("You Select Gamma Function\n")
    n = float(input("Enter the value of n: "))
    def f(x, n):
      return sy.exp(-x)*x**(n-1)
    upper_limit = float('inf')
    lower_limit = 0
    x = sy.Symbol('x')
    result = sy.integrate(f(x, n), (x, lower_limit, upper_limit))
    print(f"Ans: Gamma({n}) = {round(result, 3)} (using round 3)\n")
    print("Thanks for using Beta-Gamma Calculator")

  elif work_space == 'b' or work_space == 'B':
    print("You Select Beta Function\n")
    m = float(input("Enter the value of m: "))
    n = float(input("Enter the value of n: "))
    def f(x, m):
      return sy.sin(x)**(2*m-1)
    def g(x, n):
      return sy.cos(x)**(2*n-1)
    upper_limit = sy.pi/2
    lower_limit = 0
    x = sy.Symbol('x')
    result = sy.integrate((2*f(x, m)*g(x, n)), (x, lower_limit, upper_limit))
    print(f"Ans: Beta({m,n}) = {round(result, 3)} (using round 3)\n")
    print("Thanks for using Beta-Gamma Calculator")

  elif work_space == 'q' or work_space == 'Q':
    print("Exit!\nThanks for using Beta-Gamma Calculator\n")
    
  else:
    print(f'Input Error!\nPlease Check Your Input Value...Work-Space: {work_space} does not exist.')
  
else:
  print(f'Input Error!\nPlease Check Your Input Value...Work-Space: {work_space} does not exist.')