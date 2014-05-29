from column_parser import parse_columns

def get_manuv_score(competition_name, time_column):
    debug = False
    worst = 0
    best = 1000
    results = parse_columns(competition_name + "/manuverability.tsv")
    corrected_results = {}

    for car in results:
        time = float(car[time_column])
        carNum = car['Car Number']
        if carNum in corrected_results:
            if corrected_results[carNum] > time and time > 0:
                corrected_results[carNum] = time

        elif time > 0:
            corrected_results[carNum] = time

    for time in corrected_results.values():
        if time < best and time > 0:
            best = time
        if time > worst:
            worst = time

    if debug:
        print worst
        print best

    scores = {}

    for carNum in corrected_results.keys():
        time = float(car[time_column])
        ratio = (worst-time)/(worst-best)
        scores[carNum] = 75*ratio

    if debug:
        print scores['35']

    return scores

if __name__ == "__main__":
    get_manuv_score('el_paso_4-27-14', 'Adjusted Time');

