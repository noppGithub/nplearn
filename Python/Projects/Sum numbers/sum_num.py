from itertools import permutations,product
from random import shuffle

import pandas as pd

if __name__ == "__main__":
    list_a = [n for n in range(11)]
    # output = permutations(list_a, 2)
    output = [p for p in product(list_a, repeat=2)] # Cartesian product
    shuffle(output)
    df = pd.DataFrame(list(output),columns=['val1','val2'])
    df.to_excel('./output.xlsx',index=False,engine='openpyxl')