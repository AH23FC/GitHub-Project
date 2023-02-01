from pathlib import Path
import csv
# Referencing Cash On Hand.csv from csv_report folder
fp = Path(r"C:\csv_reports\Cash on Hand.csv")
# Read the CSV file to append rofit and quantity from the csv
with fp.open(mode = "r", encoding = "UTF-8", newline = "") as file:
    reader = csv.reader(file)
    # Skip header
    next(reader)
    # Create an empty list to store day and cash amount
    cash_on_hand = []
    # Creating a for loop to gather all the data from the Cash on Hand.csv file
    for column in reader:
        # Storing data using .append
        cash_on_hand.append([column[0], column[1]])

# Referencing the created file "Summary_report.txt" to add information
file_path = Path.cwd()/"summary_report.txt"

def COH_calculation():
    """
    - This function calculates the difference between days' cash amounts and writes any deficit in the txt file
    - This function has no parameters
    """
    # Setting original values for old and new day variables as local variables
    old_day = 0
    new_day = 0
    # Setting a while loop which ends when all items in the cash on hand file are covered
    while new_day < len(cash_on_hand):
        # creating variable to hold old_day's cash amount
        old_day_value = int(cash_on_hand[old_day][1])
        # creating variable to hod new_day's cash amount
        new_day_value = int(cash_on_hand[new_day][1])
        # Subtracting the variables to find the difference between them, and setting the value to variable diff
        diff = new_day_value - old_day_value
        # Add 1 to the variable until the loop ends
        old_day += 1
        # Add 1 to the variable until the loop ends
        new_day += 1
        # Setting condition to check if the value set in the diff variable is a negative item
        if diff < 0:
            # If condition is met, use mode = "a" to add data to the existing file
            with file_path.open(mode = "a", encoding = "UTF-8") as file:
                # Text to be written in the file
                file.write(f"\n[CASH DEFICIT] DAY: {new_day + 39} , AMOUNT: USD{abs(diff)}")
#   Ending the function
    return
# Call for the result of the funtion
COH_calculation()
                         
