# We leave the closing of the file to be done automatically by with open
with open("poem.txt") as f:
    for line in f:
        print(line, end='')

# What happens behind the scenes is that there is a protocol used by the with statement. 
# It fetches the object returned by the open statement, let's call it "thefile" in this case

# It always calls the thefile.__enter__ function before starting the block of code under it 
# and always calls thefile.__exit__ after finishing the block of code.

# So the code that we would have written in a finally block 
# should be taken care of automatically by the __exit__ method.

# More discussion on this topic is beyond scope of this book, 
# so please refer PEP 343 for a comprehensive explanation.