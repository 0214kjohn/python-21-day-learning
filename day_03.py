# day_03.py
"""Practices string manipulation with methods."""

# Input strings with inconsistent formatting.
full_name = "  aLeX tHe cOdEr  "
email_address = "  ALEX.THE.CODER@EXAMPLE.COM  "

# Use string methods to clean and format the data.
#.strip() removes leading/trailing whitespace.
#.title() capitalizes the first letter of each word.
formatted_name = full_name.strip().title()

#.lower() converts the entire string to lowercase.
formatted_email = email_address.strip().lower()

# Print the results to verify.
# print(f"Original Name: '{full_name}'")
# print(f"Formatted Name: '{formatted_name}'")
# print(f"Original Email: '{email_address}'")
# print(f"Formatted Email: '{formatted_email}'")

print(f"Original Name : '{full_name}'")
print(f"Formatted Name: '{full_name.strip().title()}'")
print(f"Original Email: '{email_address}'")
print(f"Formatted Email: '{email_address.strip().lower()}'")