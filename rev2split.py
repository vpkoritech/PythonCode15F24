import re

text = 'Vinde123shwar'

# Split the text into alphabetic and numeric parts
alpha_parts = re.findall('[a-zA-Z]+', text)
numeric_parts = re.findall('[0-9]+', text)

# Combine alphabetic and numeric parts alternately to form the final list
result_list = [val for pair in zip(alpha_parts, numeric_parts) for val in pair]
if len(alpha_parts) > len(numeric_parts):
    result_list.append(alpha_parts[-1])

print(result_list)

#OutPut : ['Vinde', '123', 'shwar']