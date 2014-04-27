from column_parser import parse_columns
from accel_calc import get_accel_score
from cost import get_cost_score
from design import get_design_score
from hill import get_hill_score
from manuv import get_manuv_score
from sales import get_sales_score
from st import get_st_score

def get_compiled_score():
	accelScores = get_accel_score()
	costScores = get_cost_score()
	designScores = get_design_score()
	hillScores = get_hill_score()
	manuvScores = get_manuv_score()
	salesScores = get_sales_score()
	stScores = get_st_score()

	overallScores = {}
	for num in range(1,100):
		carNum = str(num)
		accel = accelScores[carNum]
		cost = costScores[carNum]
		design = designScores[carNum]
		hill = hillScores[carNum]
		manuv = manuvScores[carNum]
		sales = salesScores[carNum]
		st = stScores[carNum]
		overall = accel + cost + design + hill + manuv + sales + st
		
		overallScores[carNum] = {'accel':accel, 'cost':cost, 'design':design, 'hill':hill, 'manuv':manuv,'sales':sales, 'st':st, 'overall':overall}

		print overallScores
	
	
		
if __name__ == "__main__":
    get_compiled_score();
 
