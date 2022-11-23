import unittest
import sys
sys.path.insert(1, 'f1department')
import f1department_data_join as f1dj

class TestF1DepartmentDataJoin(unittest.TestCase):
	def setUp(self):
		self.f1_data_object = f1dj.F1DepartmentDataJoin()
		self.data = self.f1_data_object.df_f1_data

	def test_class_F1DepartmentDataJoin(self):
		self.assertIsInstance(self.f1_data_object, f1dj.F1DepartmentDataJoin, 'The object is not of class f1dj.F1DepartmentDataJoin!')

	def test_data_not_null(self):
		self.assertFalse(self.data.empty, 'The data is empty')

	def test_save_data_csv(self):
		self.assertFalse(isinstance(self.f1_data_object.save_data_csv(), str), 'CSV file not saved!')

if __name__ == '__main__':
	unittest.main()
