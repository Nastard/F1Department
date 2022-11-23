import pandas as pd
import numpy as np
import f1department_data_join as f1dj

class F1Department:
	f1_data = pd.DataFrame()

	def __init__(self):
		f1_data_object = f1dj.F1DepartmentDataJoin()
		self.f1_data = f1_data_object.df_f1_data

	def driver_most_wins(self):
		folder = './data/'
		df_drivers = pd.read_csv(folder+'drivers.csv')

		total_wins = []
		for i in df_drivers.index:
			total_wins.append(0)
		df_drivers['total_wins'] = total_wins

		for i in df_drivers.index:
			wins = len(self.f1_data[(self.f1_data['driverId']==df_drivers['driverId'][i])&(self.f1_data['position']=='1')])
			df_drivers.at[i, 'total_wins'] = wins
			wins = 0

		driver_most_wins = df_drivers.query('total_wins == total_wins.max()')
		result = driver_most_wins.to_json(orient="records")
		return result

	def driver_most_poles(self):
		folder = './data/'
		df_drivers = pd.read_csv(folder+'drivers.csv')

		total_poles = []
		for i in df_drivers.index:
			total_poles.append(0)
		df_drivers['total_poles'] = total_poles

		for i in df_drivers.index:
			poles = len(self.f1_data[(self.f1_data['driverId']==df_drivers['driverId'][i])&(self.f1_data['grid']==1)])
			df_drivers.at[i, 'total_poles'] = poles
			poles = 0

		driver_most_poles = df_drivers.query('total_poles == total_poles.max()')
		result = driver_most_poles.to_json(orient="records")
		return result

	def nationality_most_wins(self):
		folder = './data/'
		df_drivers = pd.read_csv(folder+'drivers.csv')

		total_wins = []
		for i in df_drivers.index:
			total_wins.append(0)
		df_drivers['total_wins'] = total_wins

		for i in df_drivers.index:
			wins = len(self.f1_data[(self.f1_data['driverId']==df_drivers['driverId'][i])&(self.f1_data['position']=='1')])
			df_drivers.at[i, 'total_wins'] = wins
			wins = 0

		nationalities = df_drivers['nationality'].value_counts()
		df_nationalities = pd.DataFrame(nationalities)
		df_nationalities = df_nationalities.reset_index()
		del df_nationalities['nationality']
		df_nationalities.columns = ['nationality']

		total_nationality_wins = []
		for i in df_nationalities.index:
			total_nationality_wins.append(0)
		df_nationalities['total_nationality_wins'] = total_nationality_wins

		for i in df_nationalities.index:
			wins = len(self.f1_data[(self.f1_data['nationality_x']==df_nationalities['nationality'][i])&(self.f1_data['position']=='1')])
			df_nationalities.at[i, 'total_nationality_wins'] = wins
			wins = 0

		nationality_most_wins = df_nationalities.query('total_nationality_wins == total_nationality_wins.max()')
		result = nationality_most_wins.to_json(orient="records")
		return result

	def constructor_most_laps_led(self):
		return 0;

	def constructor_most_points(self):
		return 0;
