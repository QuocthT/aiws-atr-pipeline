import csv

input_file = "C:\\Users\\dawid\\Documents\\GitHub\\aiws-atr-pipeline\\results\\atr_raw_scores.csv"  # change to your filename

rows = []
with open(input_file, newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        if row['model_name'] == 'ChatGPT':
            row['date_tested'] = '05/14/2026'
        rows.append(row)

with open(input_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)