import csv
import os

# Define the file path for the clean data CSV file
filepath = os.path.join('data', 'clean_data.csv')
clean_data = open(filepath,'r')

# Use csv.DictReader to read the CSV file into a dictionary
data_dict = csv.DictReader(clean_data)

# Initialize variables
count = 0 
decade_yrs= []
dec_yrs_avg = []

# Print the average temperature anomaly for each decade
print("Average temperature anomaly for the decades:")
for line in data_dict:
    
     # Extract the 'Year' and 'J-D' values from each line
    decade_yrs += [line['Year']]
    dec_yrs_avg += [float(line['J-D'])]

    count += 1

    # Calculate and print the average for every 10 years (decade)
    if count == 10: 
        yrs_range = str(decade_yrs[0])+" to "+ str(decade_yrs[len(decade_yrs)-1])
        decade_avg = sum(dec_yrs_avg)/len(dec_yrs_avg)
        print(yrs_range +": "+ '{:.1f}'.format(decade_avg))

        # Reset variables for the next decade
        decade_yrs = []
        dec_yrs_avg = []
        count = 0

# Close the file
clean_data.close()  
    

