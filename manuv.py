from column_parser import parse_columns

def get_manuv_score(competition_name, time_column):
    debug = False
    worst = 0
    best = 1000
    results = parse_columns(competition_name + "/manuverability.tsv")
    for car in results:
        time = float(car[time_column])
        if time < best and time > 0:
            best = time
        if time > worst:
            worst = time

    if debug:
        print worst
        print best

    scores = {}

    for car in results:
        carNum = car['Car Number']
        time = float(car[time_column])
        if time > 0:
            ratio = (worst-time)/(worst-best)
            score = 75*ratio

        else:
            score = 0

        if carNum not in scores or (scores[carNum] < score):
            scores[carNum] = score

    if debug:
        print scores['24']

    return scores


if __name__ == "__main__":
    get_manuv_score();

