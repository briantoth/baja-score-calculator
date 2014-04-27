from column_parser import parse_columns

def get_endurance_score():
    debug = True
    results = parse_columns("./el_paso_4-27-14/endurance.tsv")
    scores = {}
    max_laps = 0
    min_laps = float("inf")
    carsOnLeadLap = 0
    for car in results:
        laps = int(car['# of Laps'])
        if laps > max_laps:
            max_laps = laps
        if laps < min_laps:
            min_laps = laps

    #figure out bonus points
    for car in results:
        laps = int(car['# of Laps'])
        if laps == max_laps:
            carsOnLeadLap += 1

    if debug:
        print("Number of cars on lead lap: " + str(carsOnLeadLap))

    for car in results:
        carNum = car['Car Number']
        laps = float(car['# of Laps'])
        scores[carNum] = 400 * (laps - min_laps) / (max_laps - min_laps) + calc_bonus(car, carsOnLeadLap)

    return scores


def calc_bonus(car, carsOnLeadLap):
    max_bonus = 10
    min_bonus = 0
    my_bonus = 0
    if carsOnLeadLap <= max_bonus:
        my_bonus = carsOnLeadLap - int(car["Current Position"])
    else:
        my_bonus = max_bonus - (int(car["Current Position"]) - 1)

    if my_bonus > min_bonus:
        return my_bonus
    else:
        return min_bonus

if __name__ == "__main__":
    print(get_endurance_score()["24"])

