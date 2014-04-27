from column_parser import parse_columns

def get_sales_score():
    results = parse_columns("./el_paso_4-27-14/sales.tsv")
    scores = {}

    for car in results:
        carNum = car['Car Number']
        score = car ['Final Score']
        scores[carNum] = float(score)

    return scores

if __name__ == "__main__":
    get_sales_score();

