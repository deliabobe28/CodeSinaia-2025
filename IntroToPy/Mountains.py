import ast
import pandas as pd
def load_randoms(randoms_file):
    randoms_map = {}
    count = 0
    df = pd.read_csv(randoms_file, sep='\t')
    # with open(randoms_file, "r") as data_file:
    #     for line in data_file.readlines():
    #         line_parts = line.split("\t", 1)
    #         print(line_parts[0])
            # random_value = int(line_parts[0])
            # random_indexes = ast.literal_eval(line_parts[1])
            # randoms_map[random_value] = random_indexes
            # count += len(random_indexes)
    # return randoms_map, count

if __name__ == "__main__":
  load_randoms("mountains_db.tsv")
#   print(f"Loaded {len(randoms_map.keys())} unique random generated in a sequence of {count} iterations")