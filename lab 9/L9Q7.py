
def isPalindrome(string):
    nstring = string.lower().strip()
    rstring = nstring[::-1] 
    if rstring == nstring:
        return True
    else:
        return False
string = input("Enter a string:")
print(isPalindrome(string))
