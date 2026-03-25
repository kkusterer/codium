
to_decode = input("Enter string to decode: ")

decode_key = int(input("Enter the key (number): "))

to_decode = to_decode.replace("adhg",".")

from_decode = 
for c in to_decode:
    if c.isupper():
        from_decode += chr((ord(c) - ord('A') - decode_key) % 26 + ord('A'))
    elif c.islower():
        from_decode += chr((ord(c) - ord('a') - decode_key) % 26 + ord('a'))
    else:
        from_decode += c

text = from_decode

from_replace = text.replace(".", " ")

print("string: " , from_replace )