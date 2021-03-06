from column_parser import parse_columns

def get_sales_score(competition_name):
    results = parse_columns(competition_name + "/sales.tsv")
    scores = {}

    for car in results:
        carNum = car["Car Number"] if "Car Number" in car else car["Car No."]
        score = car ['Final Score']
        if carNum not in scores or scores[carNum] < float(score):
            scores[carNum] = float(score)

    return scores

if __name__ == "__main__":
    get_sales_score();

