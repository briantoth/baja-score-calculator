from column_parser import parse_columns

#We assumed Method C (Fixed-distance, some succeed)
def get_hill_score():
    max_points = 60
    result = {}
    scores = parse_columns("./el_paso_4-27-14/hill.tsv")
    #first figure out the scores of those who made it
    for score in scores:
        if float(score["Time"]) > 0:
            print score

if __name__ == "__main__":
    get_hill_score()

