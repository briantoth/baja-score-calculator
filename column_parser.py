def parse_columns(filename):
    with open(filename, 'r') as f:
        first = True
        columns = []
        result = []
        for line in f:
            if first:
                first = False
                columns = line.split("\t")
            else:
                car = {}
                stats = line.split("\t")
                for i in range(len(columns)):
                    car[columns[i].strip()] = stats[i].strip()

                #map from car number to that car's results
                result.append(car)

        return result

if __name__ == "__main__":
    print(parse_columns("./el_paso_4-27-14/sales.tsv"))
