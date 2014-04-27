from column_parser import parse_columns

#We assumed Method C (Fixed-distance, some succeed)
def get_st_score():
    debug = False
    max_points = 75
    result = {}
    scores = parse_columns("./el_paso_4-27-14/suspTraction.tsv")
    #first figure out the scores of those who made it
    fastest_complete_time = float("inf")
    max_distance = 0
    for score in scores:
        time= float(score["Adjusted Time"])
        if time > 0 and time < fastest_complete_time:
            max_distance = get_distance(score)
            fastest_complete_time = time

    if(debug):
        print("Fastest complete time: " + str(fastest_complete_time))
        print("Max distance: " + str(max_distance))

    for score in scores:
        time= float(score["Adjusted Time"])
        if time > 0:
            car_number = score["Car Number"]
            points = max_points * fastest_complete_time / time
            add_better_score(result, points, car_number)

    lowest_full_complete_score = float("inf")
    for current_points in result.values():
        if current_points < lowest_full_complete_score:
            lowest_full_complete_score = current_points

    if(debug):
        print("Lowest complete score: " + str(lowest_full_complete_score))

    #now do everyone else
    for score in scores:
        car_number = score["Car Number"]
        points = lowest_full_complete_score * get_distance(score)  / max_distance
        add_better_score(result, points, car_number)

    return result

def get_distance(score):
    return int(score["Distance"].split()[0])

def add_better_score(result, new_score, car_number):
    if car_number not in result or new_score > result[car_number]:
        result[car_number] = new_score

if __name__ == "__main__":
    print(get_st_score())

