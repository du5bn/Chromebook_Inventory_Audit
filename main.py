import csv

# Open the CSV files
with open('inventory-export.csv', 'r') as inventory, open('ECFCBSN.csv', 'r') as ecfcbsn, open('ecfcbInventory.csv', 'w', newline='') as output:
    # Create CSV readers and writer
    inventory_reader = csv.DictReader(inventory)
    ecfcbsn_reader = csv.DictReader(ecfcbsn)
    fieldnames = inventory_reader.fieldnames
    output_writer = csv.DictWriter(output, fieldnames=fieldnames)
    output_writer.writeheader()
    # Get the purchased serial numbers from the ECFCBSN file
    purchased_serial_numbers = [row['ECFSN'] for row in ecfcbsn_reader]
    # Iterate through the rows in the inventory file and output to the ecfcbInventory.csv file.
    for row in inventory_reader:
        if row['Serial Number'] in purchased_serial_numbers:
            output_writer.writerow(row)