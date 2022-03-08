import csv
import json


big_bulk_in = "files/big_bulk_edit.csv"
big_default_in = "files/big_default.csv"
big_ez_in = "files/big_ez.csv"
big_sub_in = "files/big_sub_item.csv"

big_bulk_out = "json/big_bulk_edit.json"
big_default_out = "json/big_default.json"
big_ez_out = "json/big_ez.json"
big_sub_out = "json/big_sub_item.json"


def saveJson():
    with open(big_bulk_out, 'w') as outfile:
        json.dump(big_bulk, outfile)
    with open(big_default_out, 'w') as outfile:
        json.dump(bid_default, outfile)
    with open(big_ez_out, 'w') as outfile:
        json.dump(big_ez, outfile)
    with open(big_sub_out, 'w') as outfile:
        json.dump(big_sub, outfile)


def read_csv(filename):
    with open(filename, encoding="utf8") as f:
        file_data = csv.reader(f)
        headers = next(file_data)
        return [dict(zip(headers, i)) for i in file_data]


big_bulk = read_csv(big_bulk_in)
bid_default = read_csv(big_default_in)
big_ez = read_csv(big_ez_in)
big_sub = read_csv(big_sub_in)


saveJson()

