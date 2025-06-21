# reverese  string

def Reverse_string(string: str)-> str:

# Initialize an empty string to store the reversed characters
    revers_str = ""

# Start from the last character of the string
    right_index = len(string) - 1

# Loop from the end of the string to the beginning
    while right_index >= 0:

# Append each character from end to start into the new string

        revers_str += string[right_index]
        
 # Move to the previous character
        right_index -= 1

    return revers_str

def invoke_reverse_string():

    input = 'abcd'

    result  = Reverse_string(input)

    print(f"Reversed string: {result}")

# print output

invoke_reverse_string()



        