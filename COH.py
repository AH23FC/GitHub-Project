from pathlib import Path
import csv
# Referencing Cash On Hand.csv from csv_report folder
fp = Path(r"C:\csv_reports\Cash on Hand.csv")
# Read the CSV file to append rofit and quantity from the csv
with fp.open(
