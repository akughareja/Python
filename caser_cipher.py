import string

def caesar_cipher(plain_text,shift):
    letters=string.ascii_lowercase
    mask=letters[shift:]+letters[:shift]
    table=str.maketrans(letters,mask)
    return plain_text.translate(table)

plain_text=input("Please enter string: ")
shift=int(input("Please enter the shift number: "))
result_text=caesar_cipher(plain_text,shift)
print("caser_cipher text: ",result_text)
