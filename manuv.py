from column_parser import parse_columns

def get_manuv_score(competition_name, time_column):
    debug = False
    worst = 0
    best = 1000
    results = parse_columns(competition_name + "/manuverability.tsv")
    corrected_results = {}

    for car in results:
        time = float(car[time_column])
        carNum = car["Car Number"] if "Car Number" in car else car["Car No."]
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

    if worst > 2.5 * best:
        worst = 2.5 * best

    scores = {}

    for carNum in corrected_results.keys():
        time = float(corrected_results[carNum])
        if time > worst:
            scores[carNum] = 0
        else :
            ratio = (worst-time)/(worst-best)
            scores[carNum] = 75*ratio

    if debug:
        print scores['35']

    return scores

if __name__ == "__main__":
    print get_manuv_score('el_paso_4-27-14', 'Adjusted Time');

