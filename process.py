import csv
data = []
with open('data.txt') as f:
    data = [line.strip() for line in f.readlines()]
    # col_0 = [line.strip() for i, line in enumerate(lines) if i % 4 == 0]
    # col_1 = [line.strip() for i, line in enumerate(lines) if i % 4 == 1]
    # col_2 = [line.strip() for i, line in enumerate(lines) if i % 4 == 2]
    # col_3 = [line.strip() for i, line in enumerate(lines) if i % 4 == 3]
    # print("col 0", col_0[:4])
    # print("col 1", col_1[:4])
    # print("col 2", col_2[:4])
    # print("col 3", col_3[:4])
        
header = data[:4]
with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    i = 4
    while i < len(data):
        writer.writerow(data[i:i+4])
        i += 4
