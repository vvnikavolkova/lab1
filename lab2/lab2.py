import csv, statistics, math


def read_line(reader):
    fields = next(reader)
    line = ('|').join(fields)
    return fields


def slice(coffee_file, start, end):
    coffee_file.seek(0)
    reader = csv.reader(coffee_file, delimiter=",")
    for i in range(end):
        if i >= (start - 1):
            read_line(reader)
        else:
            next(reader)


def find_popular(coffee_file):
    coffee_file.seek(0)
    reader = csv.DictReader(coffee_file)
    drinks = []
    for row in reader:
        drinks.append(row['coffee_name'])
    res = statistics.mode(drinks)
    # counter = { d:0 for d in drinks}
    # for d in drinks:
    #     counter[d] += 1
    # print(counter)
    # res = max(counter, key=lambda k: counter[k]) 


def compute_income(coffee_file):
    month = min(max(int(input('1-12')), 1), 12)
    coffee_file.seek(0)
    reader = csv.DictReader(coffee_file)
    income = 0
    for r in reader:
        if r['Monthsort'] == str(month):
            income ++ float(r['money'])
    income = math.floor(income)
    print(income)
    return income



if __name__ == "__main__":
    with open ("Coffe_sales.csv") as coffee_file:
        slice(coffee_file, 7, 10)
        find_popular(coffee_file)


