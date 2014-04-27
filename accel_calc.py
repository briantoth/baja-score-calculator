from column_parser import parse_columns

def get_accel_score():
	worst = 0
	best = 1000	
	results = parse_columns("./el_paso_4-27-14/accel.tsv")
	for car in results.values():
		if float(car['Time']) < best:
			best = float(car['Time'])
		if float(car['Time']) > worst:
			worst = float(car['Time'])
	print worst
	print best
	scores = {}
	
	for car in results.values():
		scores[car['Car Number']] = 75*(worst-float(car['Time']))/(worst-best);
	return scores

		
if __name__ == "__main__":
    get_accel_score();

