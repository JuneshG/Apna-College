def decoder(number):                                     #6. a number is sent to the decoder to read the message corresponding to the number
    with open('newFile.txt') as file:               #7. open the encoded_file as file
        for i in file:                                   #8. For each line in the file, implement a for loop 
            if number in i:                              #9. if the number from the pyramid is in that iterated line, perform the following action:
                a = i.split(' ')[-1].replace('\n','')    #10. split the things into an array and take the last element like in the pyramid function and replace \n with null
                return a                                 #11. Return the values in the pattern required in the question.
                


def pyramid():                                           #1. Firstly, I defined a function called pyramid.                      
    with open('pyramid.txt') as input_file:              #2. I opened a file named pyramid.txt where the numbers are written in a pyramid pattern as input_file
        for i in input_file:                             #3. For each line in the input_file I run a for loop
            number = i.split(" ")[-1].replace('\n', '')  #4. split each line based on a space, take last element, every line has a hidden \n, so, replace \n with null string
            print(decoder(number))                       #5. since a variable "number" has the last element of the pyramid. that is 1,3, and 6, we send it to a function decoder
        
pyramid()      