from column_parser import parse_columns

def get_design_score():
    results = parse_columns("./el_paso_4-27-14/design.tsv")
    scores = {}

    for car in results:
        carNum = car['Car Number']
        score = car ['Final Score']
        scores[carNum] = float(score)

    return scores

if __name__ == "__main__":
    get_design_score();

