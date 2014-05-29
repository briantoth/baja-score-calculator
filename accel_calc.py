from column_parser import parse_columns

def get_accel_score(competition_name):
    debug = False
    worst = 0
    best = 1000
    results = parse_columns(competition_name + "/accel.tsv")

    #first make sure that only each car's best results are represented
    corrected_results = {}

    for car in results:
        time = float(car['Time'])
        carNum = car['Car Number']
        if carNum in corrected_results:
            if corrected_results[carNum] > time and time > 0:
                corrected_results[carNum] = time

        elif time > 0:
            corrected_results[carNum] = time

    for time in corrected_results.values():
        if time < best:
            best = time

        if time > worst:
            worst = time

    ##if the slowest car is really slow, there is a floor on the worst time
    #if worst > 1.5 * best:
        #worst = 1.5 * best

    if debug:
        print worst
        print best

    scores = {}

    for carNum in corrected_results.keys():
        time = corrected_results[carNum]
        score = 75 * (worst - time) / (worst - best)
        scores[carNum] = score

    if debug:
        print scores['35']

    return scores

if __name__ == "__main__":
    get_accel_score('el_paso_4-27-14')

