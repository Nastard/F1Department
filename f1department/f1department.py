import pandas as pd
import numpy as np
import f1department_data_join as f1dj

class F1Department:
	f1_data = pd.DataFrame()

	def __init__(self):
		f1_data_object = f1dj.F1DepartmentDataJoin()
		self.f1_data = f1_data_object.df_f1_data

	def driver_most_wins(self):
		return 0;

	def driver_most_poles(self):
		return 0;

	def nationality_most_wins(self):
		return 0;

	def constructor_most_laps_led(self):
		return 0;
