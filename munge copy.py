

# Place code below to do the munging part of this assignment.
filenasa = open("/Users/tuesti/database_design /Workshop1/2-data-munging-dtuesta1/data/nasadata.txt","r")

new_file = open("/Users/tuesti/database_design /Workshop1/2-data-munging-dtuesta1/data/clean_data.csv", "w")


def remove(string):
    return string.replace(" ", ",")

listoflines= filenasa.readlines()    # a list of strings with each line of the nasa file
mungefile= open('munged.csv', 'w')   # new csv file
secondy= 0  # variable to count the second time we encounter the character 'Y'
indextocut=0   # variable to hold the index of the second time 'Y' is encountered in the column heading line

for i in listoflines:
    strippedstring= i.strip()   # removing the '\n' and any trailing and leading spaces
    #nospace = remove(strippedstring)  
    if len(strippedstring)==0:   # condition to skip the empty lines
        continue
    elif strippedstring[0] == 'Y' and secondy== 0:   # used only for one time
        for n in strippedstring:
            indextocut +=1
            if n =='Y' and secondy==0:
                mungefile.write(n)
                secondy += 1
            elif n =='Y' and secondy==1:
                break
            else:
                mungefile.write(n)
   
    elif strippedstring[0] =='1' or strippedstring[0]=='2':   # condition for all the lines with the required data
        for n in range(0,indextocut-1):
            if strippedstring[n].isspace() == True:    #condition to check for space and add ','
                if strippedstring[n + 1].isalnum == True:
                    print('if')
                    mungefile.write(',')
                else:
                    print('else')
                    continue
            else:
                print('numbers')
                mungefile.write(strippedstring[n])
    else:       #condition to skip any line that doest start with 'y' or numbers 1 and 2                
        continue
    mungefile.write('\n')    # adding a new line at the end of each string(line of data) that is parsed
