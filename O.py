from pathlib import Path
import.csv
# Referencing Overheads.csv file from csv_reports folder
fp = Path(r"C:\csv_reports\Overheads.csv")
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
