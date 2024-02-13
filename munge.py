# Place code below to do the munging part of this assignment.
import os

# Define file paths for the input raw data and the output clean data
filepathn = os.path.join('data', 'nasadata.txt')
file_obj = open(filepathn,'r')

filepathc = os.path.join('data', 'clean_data.csv')
new_file = open(filepathc,'w')


# convert celsius data value into fahrenheit
def fahrenheit_conversion(celsius):
    
    # use formula 
    temp = int(celsius)*1.8 /100
    return temp

# Function to process each line of the raw data and convert it into CSV format
def process(line):

    new_line = ""   # starting a new string to collect the processed data to write 

    split_str = line.split()    # convert string into a list
    
    count_com = 0
    for i in split_str:     # iterating through new list to convert them into a csv format

        # add column headings and years without alteration
        if len(i) == 4 and i.isnumeric() or i.isalpha() or i in ['J-D','D-N']:
            new_line += i 
        
        # convert temp and handle missing data "***"
        else:
            neg = False     # no negative sign
            num_str = ""    # collecting the number str to then convert to a int
            for char in i:  # iterate each character in line
                
                if char == "*":
                    new_line += ""  # replaces * with an empty line
                elif char.isnumeric():  # character is a pure number
                    num_str += char 
                elif char == "-":   # dealing with negative numbers
                    new_line += "-"
                    neg = True
                elif neg == True and char.isnumeric():
                    num_str += char

            if len(num_str)>0:  # adding the formatted number
                new_line += '{:.1f}'.format(fahrenheit_conversion(int(num_str)))

        if count_com < len(split_str)-1:    # ensure we're adding the correct number of commas 
            new_line += ","
            count_com+= 1

    return new_line +"\n"   

count = 0 

# Loop through each line in the raw data file
for line in file_obj:
    a = line[0]     # collects the first value in the data 
    striped_line = line.strip() # converting line into a list

    if a .isnumeric():  
        new_file.write(process(striped_line))
       
    elif a == "Y" and count ==0 :   # only writing the column heading once 
        new_file.write(process(striped_line))
        count += 1 

new_file.close()
