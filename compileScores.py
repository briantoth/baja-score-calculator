import sys
from accel_calc import get_accel_score
from cost import get_cost_score
from design import get_design_score
from hill import get_hill_score
from manuv import get_manuv_score
from sales import get_sales_score
from st import get_st_score
from endurance import get_endurance_score

def get_compiled_score(competition_name, time_column):
    accelScores = get_accel_score(competition_name)
    costScores = get_cost_score(competition_name)
    designScores = get_design_score(competition_name)
    hillScores = get_hill_score(competition_name)
    manuvScores = get_manuv_score(competition_name, time_column)
    salesScores = get_sales_score(competition_name)
    stScores = get_st_score(competition_name, time_column)
    enduranceScores = get_endurance_score(competition_name)
    schools = {}
    with open(competition_name + "/schools.tsv", 'r') as f:
        for line in f:
            data = line.split("\t")
            schools[data[0].strip()] = data[1].strip()

    overallScores = {}
    for num in range(1,117):
        carNum = str(num)
        accel = get_score(accelScores, carNum)
        cost = get_score(costScores, carNum)
        design = get_score(designScores, carNum)
        hill = get_score(hillScores, carNum)
        manuv = get_score(manuvScores, carNum)
        sales = get_score(salesScores, carNum)
        st = get_score(stScores, carNum)
        endurance = get_score(enduranceScores, carNum)
        overall = accel + cost + design + hill + manuv + sales + st + endurance
        school = ""
        if carNum in schools:
            school = schools[carNum]

        overallScores[carNum] = {'school': school ,'accel':accel, 'cost':cost, 'design':design, 'hill':hill, 'manuv':manuv,'sales':sales, 'st':st, 'endurance': endurance, 'overall':overall}

    return overallScores

def get_score(scores, carNum):
    if carNum in scores:
        return scores[carNum]

    return 0

if __name__ == "__main__":
   output = get_compiled_score(sys.argv[1], sys.argv[2])
   print("School Name, Car Number, Acceleration, Cost, Design, Hill, Maneuverability, Sales, Susp&Traction, Endurance, Overall")
   for num in output.keys():
       car = output[num]
       if car['school'] != "":
           print(car['school'] + ", " + num + ", " + str(car['accel']) + ", " + str(car['cost']) + ", " + str(car['design']) +
                 ", "+ str(car['hill']) + ", "+ str(car['manuv']) + ", "+ str(car['sales']) +
                 ", "+ str(car['st']) + ", "+ str(car['endurance']) + ", " + str(car['overall']))
