def fill_product_name(line):
    product_max_len = 60
    product_len = len(line['product_name'])
    product_name = line['product_name']
    first_part = ''
    second_part = ''
    if product_len > product_max_len:
        first_part = product_name[0:60]
        if len(product_name) > 120:
            second_part = product_name[61:120]
        else:
            second_part = product_name[61:product_len]
            if len(second_part) < 60:
                second_part.ljust(60 - len(second_part))
        product_name = first_part + second_part
    if len(product_name) < 60:
        product_name = product_name.ljust(60)

    return product_name


def fill_product_code(line):
    code_max_len = 13
    code_len = len(line['product_code'])
    code = ''
    if code_len > code_max_len:
        code = line['product_code'][0:13]
    else:
        code = line['product_code'].ljust(13)
    return code


def fill_product_tax(line):
    if line['tax'] > 0:
        return f"{line['tax']:.1f}"
    else:
        return 0.00
