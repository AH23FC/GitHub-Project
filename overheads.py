from pathlib import Path
import csv
# Referencing Overheads.csv file from csv_reports folder

fp = Path.cwd()/"csv_reports"/"Overheads.csv"
# read the csv file to append Category and Overheads from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    # Skip the header
    next(reader)
    # create an empty list to store data from the csv file 
    overheads = []
    # Creating a for loop to gather all the data from the Overheads.csv file
    for column in reader:
        # Storing data using .append()
        overheads.append([column[0], column[1]])
# creating a new file_path and creating a new file "summary_report.txt"
file_path = Path.cwd()/"summary_report.txt"
# creating the new file "summary_report.txt" using .touch()
file_path.touch()

def OH_calculation():
    """
    - This function finds which overhead is the highest among all of them, and writes the category name in the txt file
    - This function has no parameters 
    """
    #Setting original values for varibales as local variables
    day_counter= 0
    NP_new= 0
    NP_high= 0
    #Setting a while loop which ends when all items in the overheads file are covered
    while day_counter < len(overheads):
        # Creating varibale capturing the Overheads' values which changes when the day_counter variable changes
        NP_new = float(overheads[day_counter][1])
        #Setting condition to check which variable is larger in numeric value
        if NP_new > NP_high:
            # If the condition is met, replace the value of NP_new with NP_high
            NP_high = NP_new
            # NP_cat variable is the highest overheads category
            NP_cat= overheads[day_counter][0]
            # Using mode "w" to write data in the file
            with file_path.open(mode = "w", encoding = "UTF-8") as file:
                # text to be written in the file
                file.write(f"[HIGHEST OVERHEADS] {NP_cat}: {NP_high}%")
        # Add 1 to the variable until the loop ends
        day_counter += 1
    # Ending the function
    return
# call for the result of the function
OH_calculation()