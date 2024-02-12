# Part 3 - Coding Exercise: Decoding a Message from a Text File
# In this exercise, you will develop a function named decode(message_file). This function should read an encoded message from a .txt file and return its decoded version as a string.

# Note that you can write your code using any language and IDE you want (Python is preferred if possible, but not mandatory).

# Your function must be able to process an input file with the following format:

# 3 love
# 6 computers
# 2 dogs
# 4 cats
# 1 I
# 5 you
# In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the arrangement of these numbers into a "pyramid" structure. The pyramid increases by one number per line, like so:

#   1
#  2 3
# 4 5 6
# The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6). You should ignore all the other words. So for the example input file above, the message words are:

# 1: I
# 3: love
# 6: computers
# and your function should return the string "I love computers".

# def read_file (number):                                                 # read main file         
#     with open ('your_file.txt') as input_file:                          # once the file is opened, the memory is allocated for that opened file. By using "with" command, once file is opened, it closes automatically freeing the memory that had been allocated for that purpose. 
#         for line in input_file:                                         # operate on each line:
#             if number in line:                                          
#                 return (line.split (" ")[1].replace('\n',''))
            
# def read_pyramid():
#     string = ''
#     with open('pyramid.txt') as file:
#         for i in file:
#             a = i.split (" ") [-1].replace('\n','')
#             print(a+":"+read_file(a))

# read_pyramid()

            





def decoder(number):                                     #6. a number is sent to the decoder to read the message corresponding to the number
    with open('encoded_file.txt') as file:               #7. open the encoded_file as file
        for i in file:                                   #8. For each line in the file, implement a for loop 
            if number in i:                              #9. if the number from the pyramid is in that iterated line, perform the following action:
                a = i.split(' ')[-1].replace('\n','')    #10. split the things into an array and take the last element like in the pyramid function and replace \n with null
                return a                                 #11. Return the values in the pattern required in the question.
                


def pyramid():                                           #1. Firstly, I defined a function called pyramid.                      
    with open('pyramid.txt') as input_file:              #2. I opened a file named pyramid.txt where the numbers are written in a pyramid pattern as input_file
        for i in input_file:                             #3. For each line in the input_file I run a for loop
            number = i.split(" ")[-1].replace('\n', '')  #4. split each line based on a space, take last element, every line has a hidden \n, so, replace \n with null string
            print(decoder(number))                       #5. since a variable "number" has the last element of the pyramid. that is 1,3, and 6, we send it to a function decoder
        
pyramid()                                                #12. Call the function and it prints the value from the pyramid as it already has a print function inside of the pyramid function.













