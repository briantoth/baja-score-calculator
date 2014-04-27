from column_parser import parse_columns

def get_manuv_score():
	debug = False
	worst = 0
	best = 1000	
	results = parse_columns("./el_paso_4-27-14/manuverability.tsv")
	for car in results:
		time = float(car['Adjusted Time'])
		if time < best and time > 0:
			best = time
		if time > worst:
			worst = time
	if debug: 
		print worst
		print best
	scores = {}
		
	for car in results:
		carNum = car['Car Number']
		time = float(car['Adjusted Time'])
		if time > 0:
			ratio = (worst-time)/(worst-best)			
			score = 75*ratio
			print ratio
		else:
			score = 0		
		if carNum not in scores or (scores[carNum] < score):
			scores[carNum] = score
	if debug:
		print scores['24']	
	return scores

		
if __name__ == "__main__":
    get_manuv_score();

