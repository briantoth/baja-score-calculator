from column_parser import parse_columns
import os

def get_design_score(competition_name):
    scores = {}
    path_name = competition_name + "/design.tsv"
    if not os.path.isfile(path_name):
        return scores

    results = parse_columns(path_name)

    for car in results:
        carNum = score["Car Number"] if "Car Number" in score else score["Car No."]
        score = car ['Final Score']
        scores[carNum] = float(score)

    return scores

if __name__ == "__main__":
    get_design_score();

