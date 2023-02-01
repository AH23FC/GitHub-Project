from pathlib import Path
import csv
# Referencing Cash on Hand.csv file from csv_reports folder
fp = Path(r"C:\csv_reports\Cash on Hand.csv")
# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    # Skipping the header
    next(reader)
    # create an empty list to store day and cash amount
    cash_on_hand = []
    # Creating a for loop to gather all the data from the Cash on Hand.csv file
    for column in reader:
        # Storing data using .append()
        cash_on_hand.append([column[0], column[1]])
# referencing the created file "summary_report.txt" to add information
file_path = Path.cwd()/"summary_report.txt"

def COH_calculation():
    """
    - The function calculates the difference between days' cash amounts and writes any deficit in the txt file
    - This function has no parameters
    """
    # Setting original values for old and new day variables as local variables
    old_day = 0
    new_day = 1
    # Setting a while loop which ends when all items in the overheads file are covered
    while new_day < len(cash_on_hand):
        # Creating variable to hold old_day's cash amount
        old_day_value = int(cash_on_hand[old_day][1])
        # Creating variable to hold new_day's cash amount
        new_day_value = int(cash_on_hand[new_day][1])
        # subtracting the variables to find the difference between them, and setting the value to variable diff
        diff = new_day_value - old_day_value
        # Add 1 to the variable until the loop ends
        old_day += 1
        # Add 1 to the variable until the loop ends
        new_day += 1
        # Setting condition to check if the value set in diff variable is a negative value
        if diff < 0:
            # If condition is met, use mode = "a" to add to existing data in file
            with file_path.open(mode = "a", encoding = "UTF-8") as file:
                # Text to be written in the file
                file.write(f"\n[CASH DEFICIT] DAY: {new_day + 39}, AMOUNT: USD{abs(diff)}")
    # Ending the function
    return
# Call for the result of the function
COH_calculation()
