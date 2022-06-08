import string

def slow_shift_n(letter,amount):
    table=string.ascii_lowercase[amount:]+string.ascii_lowercase[:amount]
    try:
        index=string.ascii_lowercase.index(letter)
        return table[index]
    except:
        return letter

def slow_caesar(message,amount):
    amount=amount%26
    enc_list=[slow_shift_n(letter,amount) for letter in message]
    return "".join(enc_list)

message=input("Please enter message: ")
amount=int(input("Please enter shift number: "))
result_text=slow_caesar(message,amount)
print("result_text: ", result_text)
