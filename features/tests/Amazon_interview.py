''''
4*** Amazon interview question:
Create a fubction that will take a string as an imput and return the 1st non-unique of a string
"Gooogle" =>"l"
"Amazon" => "m"
If there are no unique letters, return an empty string: "xoxoxo" =>
How would you test it? How would you handle edge cases?

How to handle ""? => return EOFError

'''
'''
def unique_letter(string: str):
    if not string:
        raise valueError
    String = String.Lower()
    for l in string: # 0(n)
        if string.count(l) == 1: # 0(n)
if string.count(1) == 1: # 0(n
return ""
# 0(n) == 0(n) = 0(n*2)

print(unique_letter('llajhgjvv'))
'''

''' 
def unique_letter_optimal(string: str):
    if not string:
        raise VakueError

    string = string.lower()
    d = {'g': 2, 'o':2, 'l': 1, 'e': 1}
    # google
    for l in string: # 0(n)
        if l not in d:
            d(l) = 1
        else:
            d(l) += 1

            for k, v in d.items(): # 0(n)
                if v == 1:
'''
