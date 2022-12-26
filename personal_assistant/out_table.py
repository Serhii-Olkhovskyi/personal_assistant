from tabulate import tabulate


def show_out_table(data, headers='firstrow', format='pipe'):
    print(tabulate(data, headers=headers, tablefmt=format, showindex='always'))
