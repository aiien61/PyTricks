from icecream import ic

def manipulate_csv():
    import csv

    # read csv files
    with open("sample.csv", mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            ic(row)

    # write tsv files
    with open("sample.csv", mode='r', encoding="utf-8") as read_file:
        reader = csv.reader(read_file)

        next(reader)
        with open("result.tsv", mode='w', encoding='utf-8') as write_file:
            writer = csv.writer(write_file, delimiter='\t')

            # write header
            writer.writerow(['product', 'unit_price'])

            for row in reader:
                unit_price = float(row[3]) / float(row[2])
                writer.writerow([row[1], int(unit_price)])

    # read csv files in dictionary format for each row
    with open('sample.csv', mode='r', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            ic(row)

def manipulate_json():
    import json
    from decimal import Decimal

    data = [{'id': 123, 'entities': {'url': 'python.org', 'hashtags': ['#python', '#pythontw']}}]
    ic(data)

    ic(json.dumps(data, indent=2))

    json_str = '["ham", 1.0, {"a":false, "b":null}]'
    ic(json.loads(json_str))

    ic(json.loads(json_str, parse_float=Decimal))

    with open('dump.json', mode='w') as f:
        json.dump(data, f, indent=2)

    with open('dump.json', mode='r') as f:
        json_string = json.load(f)
    
    ic(json.dumps(json_string, indent=2))
    json_string[0]['entities']['hashtags'].append('#pydata')
    ic(json_string)

if __name__ == "__main__":
    # manipulate_csv()
    manipulate_json()
