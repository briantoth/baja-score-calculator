from column_parser import parse_columns
import os.path

def get_endurance_score(competition_name):
    debug = False
    path_name = competition_name + "/endurance.tsv"
    if not os.path.isfile(path_name):
        return {}

    results = parse_columns(path_name)
    scores = {}
    max_laps = 0
    min_laps = float("inf")
    carsOnLeadLap = 0
    for car in results:
        laps = int(car['# of Laps'])
        if laps > max_laps:
            max_laps = laps
        if laps < min_laps and laps > 0:
            min_laps = laps

    #figure out bonus points
    for car in results:
        laps = int(car['# of Laps'])
        if laps == max_laps:
            carsOnLeadLap += 1

    if debug:
        print("Number of cars on lead lap: " + str(carsOnLeadLap))

    for car in results:
        carNum = car["Car Number"] if "Car Number" in car else car["Car No."]
        laps = float(car['# of Laps'])
        if laps < min_laps:
            scores[carNum] = 0
        else:
            scores[carNum] = 400 * (laps - min_laps) / (max_laps - min_laps) + calc_bonus(car, carsOnLeadLap)

    return scores


def calc_bonus(car, carsOnLeadLap):
    max_bonus = 10
    min_bonus = 0
    my_bonus = 0
    if carsOnLeadLap == 1:
        return 0

    position = int(car["Current Position"])
    if carsOnLeadLap <= max_bonus:
        my_bonus = carsOnLeadLap - (position - 1)
    else:
        my_bonus = max_bonus - (position - 1)

    if my_bonus > min_bonus:
        return my_bonus
    else:
        return min_bonus

if __name__ == "__main__":
    print(get_endurance_score('kansas_5-24-14')["45"])

