import pandas as pd

csv = pd.read_csv("movies_metadata.csv")
csv.info()
print (csv["vote_average"].mean())