
def isPangram(string):
    a = set('abcdefghijklmnopqrstuvwxyz')
    lstring = set(string.lower())
    
    return a <= lstring
string = input("Enter a string:")
print(isPangram(string))
