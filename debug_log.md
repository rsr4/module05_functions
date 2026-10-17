# debug_log.md
# Author: [Your Name]

## Bug 1
Error type: KeyError: 'amount'

File + line: File "/Users/rahim/ism3232/module05_functions/week8_buggy.py", line 21
  File "/Users/rahim/ism3232/module05_functions/week8_buggy.py", line 12
What the error means: The error usually means the key doesn't exist which usually means a typo

What I told the duck: I told the duck that a dictionary is a list of key:value pairs to store data. Then a function is used to get the total amount value that is stored with the keys named 'amount'. there also is an empty variable called total that will accumulate the values of 'amount' by going through each dictionary. 

What I tried: I tried to look through the function to see if it was called properly, then I looked through the dictionary. 

How I fixed it: I fixed it by fixing the typo in line one of the dictionary. 

## Bug 2
Error type: TypeError
File + line: File "/Users/rahim/ism3232/module05_functions/week8_buggy.py", line 23
File "/Users/rahim/ism3232/module05_functions/week8_buggy.py", line 16,

What the error means: The error means when python can't combine two data types, which would cause an error

How I fixed it: I fixed it by tracing back the lines and seeing that the arguements listed in the function was comparing an int to a str, which causes an issue. So I removed the '' around the numbers to make it an int. 

## After Fixing Both Bugs
Final output: Total: $5150.00 across 3 records
True
Did pytest pass? Yes

## AI Literacy Reflection
Did I use AI? No, I did not need AI because I was able to read what each error prompted me with, after reading the modules given by the professor I can recognize what each error signifies. Through reading the modules I was able to avoid the need of AI to help me finish this task. 
If yes -- exact prompt I used: N/A
What AI explained: N/A
What I changed myself: I changed the typo that came from the KeyError, which I was able to traceback through debugging methods. I also changed the TypeError issue which arose from python not being able to operate two different data types for an operation in a function. 
Can I explain every fixed line? Yes

## What I learned
I learned how to traceback a bug, starting by reading the error from bottom-up. This is able to help break down the infromation of the bug easiser, first by seeing which type of error it is. FInally I was able to learn how to document the bugs that I encountered through an given template. 