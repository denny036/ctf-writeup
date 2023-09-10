import re

# Open the rockyou.txt file for reading
with open("rockyou.txt", "r") as file:
    # Initialize line number
    line_number = 0

    # Loop through each line in the file
    for line in file:
        line_number += 1

        # Use regular expression to match the phone number format
        match = re.search(r'\((\d{3})\)\s(\d{3}-\d{4})', line)

        # If a match is found, extract the phone number
        if match:
            area_code = match.group(1)
            phone_digits = match.group(2)

            # Create the flag
            flag = f"PCTF{{{line_number}_{area_code}{phone_digits}}}"

            # Print the flag
            print("Found phone number on line", line_number)
            print("Flag:", flag)
