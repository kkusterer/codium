
to_encode = input("Enter string: ")

encode_key = int(input("Enter a key (number): "))

from_encode = ""
for c in to_encode:
    if c.isupper():
        from_encode += chr((ord(c) - ord('A') + encode_key) % 26 + ord('A'))
    elif c.islower():
        from_encode += chr((ord(c) - ord('a') + encode_key) % 26 + ord('a'))
    else:
        from_encode += c

text = from_encode

from_replace = text.replace(" ", "adhg")

print("string: " , from_replace )
