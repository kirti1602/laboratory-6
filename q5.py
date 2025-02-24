# Count the number of strings where the string length is 2 or more and the first and last character are the same
strings = ['abc', 'xyz', 'aba', '1221']
count = 0
for string in strings:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1
print("Number of strings where the first and last characters are the same:", count)
