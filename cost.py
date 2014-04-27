from column_parser import parse_columns

def get_cost_score():
	debug = False
	results = parse_columns("./el_paso_4-27-14/cost.tsv")
	scores = {}
	
	for car in results:
		carNum = car['Car Number']
		score = car ['Final Score']
		scores[carNum] = score
	if debug:
		print scores['1']
	return scores

		
if __name__ == "__main__":
    get_cost_score();

