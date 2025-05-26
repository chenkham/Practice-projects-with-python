
def is_palindrome(palin):
    orginal=palin
    rev_palindrome=0
    while palin>0:
        x = palin % 10
        rev_palindrome = x + 10 * rev_palindrome
        palin //= 10
    return rev_palindrome==orginal

if __name__ == '__main__':
  palin=int(input("Enter a number is palindrome or not: "))

  if is_palindrome(palin):
      print("IT is a palindrome number")
  else:
      print("IT is not a palindrome number")