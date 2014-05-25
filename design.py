from column_parser import parse_columns

def get_design_score(competition_name):
    results = parse_columns(competition_name + "/design.tsv")
    scores = {}

    for car in results:
        carNum = car['Car Number']
        score = car ['Final Score']
        scores[carNum] = float(score)

    return scores

if __name__ == "__main__":
    get_design_score();

