import pandas as pd
import numpy as np

class F1DepartmentDataJoin:
	df_f1_data = pd.DataFrame()

	def __init__(self):
		folder = './data/'
		df_circuits = pd.read_csv(folder+'circuits.csv')
		df_constructors = pd.read_csv(folder+'constructors.csv')
		df_drivers = pd.read_csv(folder+'drivers.csv')
		df_races = pd.read_csv(folder+'races.csv')
		df_results= pd.read_csv(folder+'results.csv')

		df_results_drivers = pd.merge(df_results, df_drivers, on='driverId', how='left')
		df_results_drivers_constructors = pd.merge(df_results_drivers, df_constructors, on='constructorId', how='left')
		df_races_circuits = pd.merge(df_races, df_circuits, on='circuitId', how='left')
		self.df_f1_data = pd.merge(df_results_drivers_constructors, df_races_circuits, on='raceId', how='left')

	def save_data_csv(self):
		return 0;
