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


def generateProductImageURLsList(product):
    image_urls = []
    for attr, value in product.items():
        if 'Product Image URL' in str(attr) and str(value).strip() != "":
            image_urls.append(value)
    return ";".join(image_urls)


def generateProductsCollectionsList(product):
    collections_list = []
    for attr, value in product.items():
        if 'Category Name' in str(attr) and str(value).strip() != "":
            collections_list.append(value)
    return ";".join(collections_list)


def generateNewCSVDictionary():
    final_data = []

    for i in range(len(big_sub)):
        if big_sub[i]['Item Type'].strip() == "Product":

            current_product = big_sub[i]
            products_variant = []

            sku_list = []
            rule_list = []
            special_rule_list = []

            for j in range(i + 1, len(big_sub)):

                if j == len(big_sub)-1:
                    if big_sub[j]['Item Type'].strip() == "SKU":
                        sku_list.append(big_sub[j])
                    elif big_sub[j]['Item Type'].strip() == "Rule" and big_sub[j]['Product Name'].strip() != "":
                        special_rule_list.append(big_sub[j])
                    elif big_sub[j]['Item Type'].strip() == "Rule" and big_sub[j]['Product Name'].strip() == "":
                        rule_list.append(big_sub[j])

                if big_sub[j]['Item Type'].strip() == "Product" or j == len(big_sub)-1:

                    if len(sku_list) > 0 and len(rule_list) > 0:
                        for sku in sku_list:
                            products_image = ''
                            for rule in rule_list:
                                if sku['Product SKU'].strip() == rule['Product SKU'].strip():
                                    products_image = rule['Product Image URL - 1'].strip()

                            sku_product_name_description = "".join(
                                re.split(r"[()\[\]]", sku['Product Name'].strip())[::2]).split('=')

                            new_row_obj = {'handleId': sku['Product ID'].strip(), 'fieldType': 'Variant',
                                           'name': '', 'description': '',
                                           'productImageUrl': products_image,
                                           'price': 0, "surcharge": 0.0, 'visible': 'TRUE',
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
                            products_variant.append(json.dumps(new_row_obj))
                    elif len(sku_list) > 0 and len(rule_list) == 0 and len(special_rule_list) == 0:
                        for sku in sku_list:
                            sku_product_name_description = "".join(
                                re.split(r"[()\[\]]", sku['Product Name'].strip())[::2]).split('=')

                            new_row_obj = {'handleId': sku['Product ID'].strip(), 'fieldType': 'Variant',
                                           'name': '', 'description': '',
                                           'productImageUrl': '',
                                           'price': 0, "surcharge": 0.0, 'visible': 'TRUE',
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
                            products_variant.append(json.dumps(new_row_obj))
                    elif len(special_rule_list) > 0:
                        for special_rule in special_rule_list:
                            special_rule_product_name_description = "".join(
                                re.split(r"[()\[\]]", special_rule['Product Name'].strip())[::2]).split('=')

                            price = '0'

                            if '[ADD]' in special_rule['Price']:
                                price = special_rule['Price'].replace('[ADD]', '+')
                            elif '[REMOVE]' in special_rule['Price']:
                                price = special_rule['Price'].replace('[REMOVE]', '-')
                            elif '[FIXED]' in special_rule['Price']:
                                if big_sub[i]['Price'] > special_rule['Price']:
                                    price = "-" + str(float(big_sub[i]['Price']) - float(
                                        special_rule['Price'].replace('[FIXED]', '')))
                                elif big_sub[i]['Price'] < special_rule['Price']:
                                    price = "+" + str(float(big_sub[i]['Price']) - float(
                                        special_rule['Price'].replace('[FIXED]', '')))

                            new_row_obj = {'handleId': special_rule['Product ID'].strip(), 'fieldType': 'Variant',
                                           'name': '', 'description': '',
                                           'productImageUrl': '',
                                           'price': float(price),
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
                            products_variant.append(json.dumps(new_row_obj))

                    break
                else:
                    if big_sub[j]['Item Type'].strip() == "SKU":
                        sku_list.append(big_sub[j])
                    elif big_sub[j]['Item Type'].strip() == "Rule" and big_sub[j]['Product Name'].strip() != "":
                        special_rule_list.append(big_sub[j])
                    elif big_sub[j]['Item Type'].strip() == "Rule" and big_sub[j]['Product Name'].strip() == "":
                        rule_list.append(big_sub[j])

            unique_products_variant_list = list(set(products_variant))
            products_variant = []
            for product in unique_products_variant_list:
                products_variant.append(json.loads(str(product)))

            # Generate images list
            product_image_urls = generateProductImageURLsList(current_product)

            # Generate collections list
            product_collections = generateProductsCollectionsList(current_product)

            # Generate product descriptions
            name1 = ""
            descriptions1 = []
            name2 = ""
            descriptions2 = []
            name3 = ""
            descriptions3 = []
            name4 = ""
            descriptions4 = []

            if products_variant:
                for pv in products_variant:
                    pv = dict(pv)
                    if name1 == "":
                        name1 = pv['productOptionName1']
                        descriptions1.append(pv['productOptionDescription1'])
                    elif name1 != "" and name1 == pv['productOptionName1']:
                        descriptions1.append(pv['productOptionDescription1'])
                    elif name1 != pv['productOptionName1']:
                        name2 = pv['productOptionName1']
                        descriptions2.append(pv['productOptionDescription1'])
                    elif name2 != "" and name2 == pv['productOptionName1']:
                        descriptions2.append(pv['productOptionDescription1'])
                    elif name2 != pv['productOptionName1']:
                        name3 = pv['productOptionName1']
                        descriptions3.append(pv['productOptionDescription1'])
                    elif name3 != "" and name3 == pv['productOptionName1']:
                        descriptions3.append(pv['productOptionDescription1'])
                    elif name4 != pv['productOptionName1']:
                        name4 = pv['productOptionName1']
                        descriptions4.append(pv['productOptionDescription1'])
                    elif name4 != "" and name4 == pv['productOptionName1']:
                        descriptions4.append(pv['productOptionDescription1'])

            descriptions1 = ";".join(descriptions1) if descriptions1 else ''
            descriptions2 = ";".join(descriptions2) if descriptions2 else ''
            descriptions3 = ";".join(descriptions3) if descriptions3 else ''
            descriptions4 = ";".join(descriptions4) if descriptions4 else ''

            new_row_obj = {'handleId': current_product['Product ID'].strip(),
                           'fieldType': 'Product',
                           'name': current_product['Product Name'].strip(),
                           'description': current_product['Description'].strip(),
                           'productImageUrl': product_image_urls,
                           'price': float(current_product['Price'].strip()),
                           "surcharge": 0.0,
                           'visible': 'TRUE',
                           'inventory': 'InStock',
                           'weight': current_product['Weight'].strip(),
                           "collection": product_collections,
                           "sku": '',
                           "ribbon": 'New',
                           "discountMode": '',
                           "discountValue": '',
                           'productOptionName1': name1,
                           'productOptionType1': "DROP_DOWN" if descriptions1 else '',
                           'productOptionDescription1': descriptions1,
                           'productOptionName2': name2,
                           'productOptionType2': "DROP_DOWN" if descriptions2 else '',
                           'productOptionDescription2': descriptions2,
                           "productOptionName3": name3,
                           "productOptionType3": 'DROP_DOWN' if descriptions3 else '',
                           "productOptionDescription3": descriptions3,
                           "productOptionName4": name4,
                           "productOptionType4": 'DROP_DOWN' if descriptions4 else '',
                           "productOptionDescription4": descriptions4,
                           "productOptionName5": '',
                           "productOptionType5": '',
                           "productOptionDescription5": '',
                           "productOptionName6": '',
                           "productOptionType6": '',
                           "productOptionDescription6": '',
                           "additionalInfoTitle1": '',
                           "additionalInfoDescription1": '', "additionalInfoTitle2": '',
                           "additionalInfoDescription2": '', "additionalInfoTitle3": '',
                           "additionalInfoDescription3": '', "additionalInfoTitle4": '',
                           "additionalInfoDescription4": '', "additionalInfoTitle5": '',
                           "additionalInfoDescription5": '', "customTextField1": '',
                           "customTextCharLimit1": '', "customTextMandatory1": '',
                           "brand": current_product['Brand'].strip()}

            final_data.append(new_row_obj)
            final_data.extend(products_variant)

    with open('final-json/final_data.json', 'w') as outfile:
        json.dump(final_data, outfile)

    return final_data


# generateNewCSVDictionary()


def saveCSVFile(file, csv_data):
    csv_columns = ["handleId", "fieldType", "name", "description", "productImageUrl", "price", "surcharge", "visible",
                   "inventory", "weight", "collection", "sku", "ribbon", "discountMode", "discountValue",
                   "productOptionName1", "productOptionType1", "productOptionDescription1", "productOptionName2",
                   "productOptionType2", "productOptionDescription2", "productOptionName3", "productOptionType3",
                   "productOptionDescription3", "productOptionName4", "productOptionType4", "productOptionDescription4",
                   "productOptionName5", "productOptionType5", "productOptionDescription5", "productOptionName6",
                   "productOptionType6", "productOptionDescription6", "additionalInfoTitle1",
                   "additionalInfoDescription1", "additionalInfoTitle2", "additionalInfoDescription2",
                   "additionalInfoTitle3", "additionalInfoDescription3", "additionalInfoTitle4",
                   "additionalInfoDescription4", "additionalInfoTitle5", "additionalInfoDescription5",
                   "additionalInfoTitle6", "additionalInfoDescription6", "additionalInfoTitle7",
                   "additionalInfoDescription7", "additionalInfoTitle8", "additionalInfoDescription8",
                   "customTextField1", "customTextCharLimit1", "customTextMandatory1", "brand"]

    try:
        with open(file, 'w', newline='', encoding="utf8") as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=csv_columns)
            writer.writeheader()
            for data in csv_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")


def dictionaryToCSV():
    final_csv_dictionary = generateNewCSVDictionary()

    csv_file = "final-files/final_data.csv"
    csv_file_p1 = "final-files/final_data_p1.csv"
    csv_file_p2 = "final-files/final_data_p2.csv"
    # csv_file_p3 = "final-files/final_data_p2.csv"

    saveCSVFile(csv_file, final_csv_dictionary)
    saveCSVFile(csv_file_p1, final_csv_dictionary[:5000])
    saveCSVFile(csv_file_p2, final_csv_dictionary[5000:])


dictionaryToCSV()
