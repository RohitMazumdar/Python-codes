s = input("Enter a string:")

print("No of characters in the string:")
print(len(s))

print(f"String repeated 10 times:")
for i in range(10):
    print(s)

print("First character of string: ")
print(s[0])

print("First three characters of string: ")
print(s[:3])

print("Last three characters of the string: ")
print(s[-3:])

print(f"String backwards: ")
print(s[::-1])

if 's[6]' in s:
    print(s[6])
else:
    print("Seventh character not in string")
    
print("String with 1st and last character removed:")
print(s[1:len(s)-1])

print("String in UpperCase: ")
print(s.upper())

print("String with every 'a' replaced with 'e': ")
if 'a' in s:
    print(s.replace('a','e'))
else:
    print("'a' not in s!!")

print("String with every letter replaced by a space: ")
for i in range(len(s)):
    new_string = ' '.join(s)
print(new_string)