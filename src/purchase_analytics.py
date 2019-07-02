import csv
import sys
import os

orders = sys.argv[1]
products = sys.argv[2]
report = sys.argv[3]

with open(products) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    product_department = {}
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            product_department[row[0]] = row[3]
            print((line_count))
            line_count += 1
    print(product_department)
    print(f'Processed {line_count} lines.')

with open(orders) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    order_department = {}
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            department_id = product_department.get(row[1])
            if order_department.get(department_id) is None:
                new_prod = 1 if int(row[3]) == 0 else 0
                order_department[department_id] = [1, new_prod]
            else:
                new_prod = (order_department[department_id][1] + 1) if int(row[3]) == 0 \
                    else order_department[department_id][1]
                order_department[department_id] = [order_department.get(department_id)[0] + 1, new_prod]

            line_count += 1
            print(line_count)
list = [int(i) for i in order_department.keys()]
with open(report, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['department_id','number_of_orders','number_of_first_orders','percentage'])
    for row in sorted(list):
        all_orders = order_department[str(row)][0]
        new_orders = order_department[str(row)][1]
        percent = float(new_orders) / float(all_orders)
        writer.writerow([row, all_orders, new_orders, format(percent, '.2f')])
print('END')
