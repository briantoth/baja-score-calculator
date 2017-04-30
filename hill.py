from column_parser import parse_columns

#We assumed Method C (Fixed-distance, some succeed)
def get_hill_score(competition_name):
    max_points = 75
    result = {}
    scores = parse_columns(competition_name + "/hill.tsv")
    #first figure out the scores of those who made it
    fastest_complete_time = float("inf")
    max_distance = 0
    max_distance_no_finish = 0
    min_distance_no_finish = float("inf")
    for score in scores:
        time= float(score["Time"])
        if get_distance(score) > max_distance_no_finish:
            max_distance_no_finish = get_distance(score)

        if get_distance(score) < min_distance_no_finish:
            min_distance_no_finish = get_distance(score)

        if time > 0 and time < fastest_complete_time:
            max_distance = get_distance(score)
            fastest_complete_time = time

    for score in scores:
        time= float(score["Time"])
        if time > 0:
            car_number = score["Car Number"] if "Car Number" in score else score["Car No."]
            points = max_points * fastest_complete_time / time
            add_better_score(result, points, car_number)

    lowest_full_complete_score = float("inf")
    for current_points in result.values():
        if current_points < lowest_full_complete_score:
            lowest_full_complete_score = current_points

    #now do everyone else
    for score in scores:
        car_number = score["Car Number"] if "Car Number" in score else score["Car No."]
        if max_distance is 0:
            points = 75 * (get_distance(score) - min_distance_no_finish) / (max_distance_no_finish - min_distance_no_finish)
        else:
            points = lowest_full_complete_score * get_distance(score)  / max_distance

        add_better_score(result, points, car_number)

    return result

def get_distance(score):
    return float(score["Distance"].split()[0])

def add_better_score(result, new_score, car_number):
    if car_number not in result or new_score > result[car_number]:
        result[car_number] = new_score



if __name__ == "__main__":
    print(get_hill_score())

