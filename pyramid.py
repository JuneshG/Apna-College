def print_pyramid(rows, filename):
    num = 1
    with open(filename, 'w') as file:
        for i in range(1, rows + 1):
            # Add spaces before the numbers to align them
            line = " " * (rows - i)
            print(line)
            
            # Add numbers in each row to the line
            for k in range(1, i + 1):
                line += str(num) + " "
                print(line)
                num += 1
            
            # Write the line to the file
            file.write(line.strip() + '\n')

# Specify the number of rows in the pyramid and the filename
rows = 10
output_filename = 'pyramid.txt'

# Call the function to print and save the pyramid
print_pyramid(rows, output_filename)
