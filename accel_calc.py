from column_parser import parse_columns

def get_accel_score(competition_name):
	debug = False
	worst = 0
	best = 1000
	results = parse_columns(competition_name + "/accel.tsv")
	for car in results:
		if float(car['Time']) < best:
			if float(car['Time']) >0:
				best = float(car['Time'])
		if float(car['Time']) > worst:
			worst = float(car['Time'])
	if debug:
		print worst
		print best
	scores = {}

	for car in results:
		carNum = car['Car Number']
		time = float(car['Time'])
		if time > 0:
			score = 75*(worst-time)/(worst-best)
		else: score = 0
		if carNum not in scores or (scores[carNum] < score):
			scores[carNum] = score
	if debug:
		print scores['24']
	return scores


if __name__ == "__main__":
    get_accel_score();

