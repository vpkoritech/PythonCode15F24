String = "VindesPras123warPRA"
numbers = []
pre_123 = ""
post_123 = ""
print ("Develop 123...")
for char in String:
    if char.isdigit():
        numbers.append(char)
    elif not numbers:
        post_123 += char
    else:
        pre_123 += char

# Reverse the pre_123 and post_123 strings
pre_123 = pre_123[::-1]
post_123 = post_123[::-1]

# Merge pre_123, numbers, and post_123
final_output = pre_123 + ''.join(numbers) + post_123

print("Final Output:", final_output)

#Final Output: ARPraw123sarPsedniV