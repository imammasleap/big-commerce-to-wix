import re
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


# saveJson()


def generateNewCSVDictionary():
    final_data = []

    for i in range(len(big_sub)):
        if big_sub[i]['Item Type'] == "Product":

            current_product = big_sub[i]
            products_variant = []

            sku_list = []
            rule_list = []
            special_rule_list = []

            for j in range(i + 1, len(big_sub)):
                if big_sub[j]['Item Type'] == "Product":

                    if len(sku_list) > 0 and len(rule_list) > 0:
                        for sku in sku_list:
                            for rule in rule_list:
                                if sku['Product SKU'].strip() == rule['Product SKU'].strip():
                                    sku_product_name_description = "".join(
                                        re.split(r"[()\[\]]", sku['Product Name'].strip())[::2]).split('=')

                                    new_row_obj = {'handleId': sku['Product ID'].strip(), 'fieldType': 'Variant',
                                                   'name': '', 'description': '',
                                                   'productImageUrl': rule['Product Image URL - 1'].strip(),
                                                   'price': '', "surcharge": 0.0, 'visible': 'TRUE',
                                                   'inventory': 'InStock', 'weight': '', "collection": '',
                                                   "sku": sku['Product SKU'], "ribbon": '', "discountMode": '',
                                                   "discountValue": '',
                                                   'productOptionName1': sku_product_name_description[0],
                                                   'productOptionType1': "DROP_DOWN",
                                                   'productOptionDescription1': sku_product_name_description[1],
                                                   'productOptionName2': '', 'productOptionType2': "",
                                                   'productOptionDescription2': '', "productOptionName3": '',
                                                   "productOptionType3": '', "productOptionDescription3": '',
                                                   "productOptionName4": '', "productOptionType4": '',
                                                   "productOptionDescription4": '', "productOptionName5": '',
                                                   "productOptionType5": '', "productOptionDescription5": '',
                                                   "productOptionName6": '', "productOptionType6": '',
                                                   "productOptionDescription6": '', "additionalInfoTitle1": '',
                                                   "additionalInfoDescription1": '', "additionalInfoTitle2": '',
                                                   "additionalInfoDescription2": '', "additionalInfoTitle3": '',
                                                   "additionalInfoDescription3": '', "additionalInfoTitle4": '',
                                                   "additionalInfoDescription4": '', "additionalInfoTitle5": '',
                                                   "additionalInfoDescription5": '', "customTextField1": '',
                                                   "customTextCharLimit1": '', "customTextMandatory1": '', "brand": ''}
                                    products_variant.append(new_row_obj)

                    if len(sku_list) > len(rule_list):
                        for rule in rule_list:
                            for sku in sku_list:
                                if sku['Product SKU'].strip() != rule['Product SKU'].strip():
                                    sku_product_name_description = "".join(
                                        re.split(r"[()\[\]]", sku['Product Name'].strip())[::2]).split('=')

                                    new_row_obj = {'handleId': sku['Product ID'].strip(), 'fieldType': 'Variant',
                                                   'name': '', 'description': '',
                                                   'productImageUrl': '',
                                                   'price': '', "surcharge": 0.0, 'visible': 'TRUE',
                                                   'inventory': 'InStock', 'weight': '', "collection": '',
                                                   "sku": sku['Product SKU'], "ribbon": '', "discountMode": '',
                                                   "discountValue": '',
                                                   'productOptionName1': sku_product_name_description[0],
                                                   'productOptionType1': "DROP_DOWN",
                                                   'productOptionDescription1': sku_product_name_description[1],
                                                   'productOptionName2': '', 'productOptionType2': "",
                                                   'productOptionDescription2': '', "productOptionName3": '',
                                                   "productOptionType3": '', "productOptionDescription3": '',
                                                   "productOptionName4": '', "productOptionType4": '',
                                                   "productOptionDescription4": '', "productOptionName5": '',
                                                   "productOptionType5": '', "productOptionDescription5": '',
                                                   "productOptionName6": '', "productOptionType6": '',
                                                   "productOptionDescription6": '', "additionalInfoTitle1": '',
                                                   "additionalInfoDescription1": '', "additionalInfoTitle2": '',
                                                   "additionalInfoDescription2": '', "additionalInfoTitle3": '',
                                                   "additionalInfoDescription3": '', "additionalInfoTitle4": '',
                                                   "additionalInfoDescription4": '', "additionalInfoTitle5": '',
                                                   "additionalInfoDescription5": '', "customTextField1": '',
                                                   "customTextCharLimit1": '', "customTextMandatory1": '', "brand": ''}
                                    products_variant.append(new_row_obj)

                    if len(special_rule_list) > 0:
                        for special_rule in special_rule_list:
                            special_rule_product_name_description = "".join(
                                re.split(r"[()\[\]]", special_rule['Product Name'].strip())[::2]).split('=')

                            price = ''

                            if '[ADD]' in special_rule['Price']:
                                price = special_rule['Price'].replace('[ADD]', '+')
                            elif '[REMOVE]' in special_rule['Price']:
                                price = special_rule['Price'].replace('[REMOVE]', '-')
                            elif '[FIXED]' in special_rule['Price']:
                                if big_sub[i]['Price'] > special_rule['Price']:
                                    price = "-" + str(float(big_sub[i]['Price']) - float(special_rule['Price'].replace('[FIXED]', '')))
                                elif big_sub[i]['Price'] < special_rule['Price']:
                                    price = "+" + str(float(big_sub[i]['Price']) - float(special_rule['Price'].replace('[FIXED]', '')))

                            new_row_obj = {'handleId': special_rule['Product ID'].strip(), 'fieldType': 'Variant',
                                           'name': '', 'description': '',
                                           'productImageUrl': '',
                                           'price': price,
                                           "surcharge": 0.0, 'visible': 'TRUE',
                                           'inventory': 'InStock', 'weight': '', "collection": '',
                                           "sku": special_rule['Product SKU'], "ribbon": '', "discountMode": '',
                                           "discountValue": '',
                                           'productOptionName1': special_rule_product_name_description[0],
                                           'productOptionType1': "DROP_DOWN",
                                           'productOptionDescription1': special_rule_product_name_description[1],
                                           'productOptionName2': '', 'productOptionType2': "",
                                           'productOptionDescription2': '', "productOptionName3": '',
                                           "productOptionType3": '', "productOptionDescription3": '',
                                           "productOptionName4": '', "productOptionType4": '',
                                           "productOptionDescription4": '', "productOptionName5": '',
                                           "productOptionType5": '', "productOptionDescription5": '',
                                           "productOptionName6": '', "productOptionType6": '',
                                           "productOptionDescription6": '', "additionalInfoTitle1": '',
                                           "additionalInfoDescription1": '', "additionalInfoTitle2": '',
                                           "additionalInfoDescription2": '', "additionalInfoTitle3": '',
                                           "additionalInfoDescription3": '', "additionalInfoTitle4": '',
                                           "additionalInfoDescription4": '', "additionalInfoTitle5": '',
                                           "additionalInfoDescription5": '', "customTextField1": '',
                                           "customTextCharLimit1": '', "customTextMandatory1": '', "brand": ''}
                            products_variant.append(new_row_obj)

                    break
                else:
                    if big_sub[j]['Item Type'].strip() == "SKU":
                        sku_list.append(big_sub[j])
                    elif big_sub[j]['Item Type'].strip() == "Rule" and big_sub[j]['Product Name'].strip() != "":
                        special_rule_list.append(big_sub[j])
                    elif big_sub[j]['Item Type'].strip() == "Rule" and big_sub[j]['Product Name'].strip() == "":
                        rule_list.append(big_sub[j])

            new_row_obj = {'handleId': current_product['Product ID'].strip(), 'fieldType': 'Variant',
                           'name': current_product['Product Name'].strip(), 'description': current_product['Description'].strip(),
                           'productImageUrl': '',
                           'price': current_product['Price'].strip(), "surcharge": 0.0, 'visible': 'TRUE',
                           'inventory': 'InStock', 'weight': '', "collection": current_product['Brand'],
                           "sku": '', "ribbon": 'New', "discountMode": '',
                           "discountValue": '',
                           'productOptionName1': '',
                           'productOptionType1': "DROP_DOWN",
                           'productOptionDescription1': '',
                           'productOptionName2': '', 'productOptionType2': "",
                           'productOptionDescription2': '', "productOptionName3": '',
                           "productOptionType3": '', "productOptionDescription3": '',
                           "productOptionName4": '', "productOptionType4": '',
                           "productOptionDescription4": '', "productOptionName5": '',
                           "productOptionType5": '', "productOptionDescription5": '',
                           "productOptionName6": '', "productOptionType6": '',
                           "productOptionDescription6": '', "additionalInfoTitle1": '',
                           "additionalInfoDescription1": '', "additionalInfoTitle2": '',
                           "additionalInfoDescription2": '', "additionalInfoTitle3": '',
                           "additionalInfoDescription3": '', "additionalInfoTitle4": '',
                           "additionalInfoDescription4": '', "additionalInfoTitle5": '',
                           "additionalInfoDescription5": '', "customTextField1": '',
                           "customTextCharLimit1": '', "customTextMandatory1": '', "brand": current_product['Brand']}
            products_variant.append(new_row_obj)


    with open('final-json/final_data.json', 'w') as outfile:
        json.dump(final_data, outfile)

    return final_data


generateNewCSVDictionary()

