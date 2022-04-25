def isPalindrome(n):
    """
    This function check if a non-negative number is a palindrome
    """
    temp = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if temp == rev:
        print("The number is a palindrome!")
    else:
        print("The number isn not a palindrome!")


number = int(input("Whats your number? \n"))
isPalindrome(number)
