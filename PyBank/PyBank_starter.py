# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0 #month count
total_net = 0 #net total of profits

# Add more variables to track other necessary financial data
net_changes = [] #track monthly changes in profit or loss
prior_month_value = 0 #store prior month's profit or loss value
greatest_inc = ("", 0) #store greatest increase month and value
greatest_dec = ("", 0) #store greatest decrease month and value


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
  

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1   #calc of total months

        profit_loss = int(row[1])   #Monthly profit or loss column
        total_net += profit_loss    #calc of total Profit or loss

        # Track the net change
        if total_months > 1:                                    #use row's total month count to start calc from 2nd row of data due to headers
            monthly_change = profit_loss - prior_month_value    #calc for change month to month
            net_changes.append(monthly_change)                  #add monthly change to net_changes list         

        # Calculate the greatest increase in profits (month and amount)
            if monthly_change > greatest_inc[1]:                     #if monthly change is greater than the current greatest inc
                greatest_inc = (row[0], monthly_change)              #update date and amount with current monthly change

        # Calculate the greatest decrease in losses (month and amount)
            if monthly_change < greatest_dec[1]:                
                greatest_dec = (row[0], monthly_change)

        #change prior_month_value to last profit_loss value analyzed
        prior_month_value = profit_loss

# Calculate the average net change across the months
Average_Change = sum(net_changes) / len(net_changes)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${Average_Change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_inc[0]} ${greatest_inc[1]}\n"
    f"Greatest Decrease in Profits: {greatest_dec[0]} ${greatest_dec[1]}\n" )

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
