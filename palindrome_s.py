def is_palindrome(s):
    s=s.replace(" ","").lower()
    return s == s[::-1]
string1 = "racecar"
string2 = "A man a plan a canal panama"
string3 = "hello"

print(f"'{string1}' is palindrome:{is_palindrome(string1)} ")
print(f"'{string2}' is palindrome:{is_palindrome(string2)} ")
print(f"'{string3}' is palindrome:{is_palindrome(string3)} ")