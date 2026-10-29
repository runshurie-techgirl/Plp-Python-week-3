count = 1
total = 0

# BUG: The while line was missing a colon (:) at the end, so Python gave a SyntaxError. I added the colon.
# BUG: The loop used count < 5, so it stopped before adding 5 and printed 10 instead of 15 with no error. I changed it to count <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: I was adding text and a number with +, which gave a TypeError. I used str(total) to turn the number into text.
print("Sum of 1 to 5 is: " + str(total))