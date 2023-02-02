from pathlib import Path
import csv
# Referencing Profit and Loss.csv file from csv_reports folder
fp = Path.cwd()/"csv_reports"/"Profit and Loss.csv"
# read the csv file to append Day, Sales, Trading Prodit,  Operating expense and Net Profit from the  csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    # Skipping the header
    next(reader)
    # create an empty list to store the data
    profit_loss =[]
    # creating a lopp to gather all the data from the Profit and Loss.csv file 
    for column in reader:
      # Storing data using .append()
      profit_loss.append([column[0], column[1], column[2], column [3], column[4]])
# referencing the created file "summary_report.txt" to add information
file_path = Path.cwd()/"summary_report.txt"



def PL_calculation():
    """
    - The function calculates the difference between days' net profit amounts and writes any deficit in the txt file
    - The function has no parameters
    """
    # setting original values for old and new  day variables as local variables 
    old_day = 0
    new_day = 1
    # setting a while loop which ends when all items in the overheads file are covered
    while new_day < len(profit_loss):
        # creating variable to hold old_day's Net Profit amount
        old_day_value = int(profit_loss[old_day][4])
        # creating variable to hold new_day's Net Profit amount
        new_day_value = int(profit_loss[new_day][4])
        # subtracting the variables to find the difference between them, and setting the calue to variable diff
        diff = new_day_value - old_day_value
        # Add 1 to the variable until the loop ends 
        old_day += 1
        # Add 1 to the variable until the loop ends
        new_day += 1
        # setting on condition to check if the value stores in the diff variable is negative
        if diff < 0:
            # if condition is not, use mode = "a" to asdd to ecisting data in file
            with file_path.open(mode = "a", encoding = "UTF-8") as file:
                # text to be written in the file
                file.write(f"\n[PROFIT DEFICIT] DAY: {new_day +39}, AMOUNT: USD{abs(diff)}")
    # Ending the function
    return
# call for the result of the function
PL_calculation()
      
  
