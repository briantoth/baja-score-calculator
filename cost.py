from column_parser import parse_columns

def get_cost_score():
	results = parse_columns("./el_paso_4-27-14/cost.tsv")
	scores = {}
	print results
	for car in results:
		carNum = car['Car Number']
		score = car ['Final Score']
		scores[carNum] = score
	print scores['1']
	return scores

		
if __name__ == "__main__":
    get_cost_score();

