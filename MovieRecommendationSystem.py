import numpy as np
import pandas as pd

# reading the dataset using pandas
movie = pd.read_csv('movies.csv')
rating = pd.read_csv('ratings.csv')
movie.head(4)