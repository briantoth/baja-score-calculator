from column_parser import parse_columns

def get_sales_score():
    results = parse_columns("./el_paso_4-27-14/sales.tsv")
    for result in results.values():
        print result

if __name__ == "__main__":
    get_sales_score()

