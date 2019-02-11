import pandas as pd

housing = pd.read_csv("./datasets/housing/housing.csv")
housing.describe()
housing.info()
housing['ocean_proximity'].value_counts()
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20,15))