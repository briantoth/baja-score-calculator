from column_parser import parse_columns

def get_cost_score(competition_name):
    debug = False
    results = parse_columns(competition_name + "/cost.tsv")
    scores = {}

    for car in results:
        carNum = car["Car Number"] if "Car Number" in car else car["Car No."]
        score = car ['Final Score']
        scores[carNum] = float(score)

    if debug:
        print scores['1']

    return scores

if __name__ == "__main__":
    get_cost_score();

