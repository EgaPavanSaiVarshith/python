def move_to_end(s):
    letter=""
    digit=""
    for ch in s:
        if ch.isdigit():
            digit+=ch
        else:
            letter+=ch
    return letter+digit 
s=input()
print(move_to_end(s))
