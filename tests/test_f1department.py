import unittest
import sys
sys.path.insert(1, 'f1department')
import f1department as f1

class TestF1Department(unittest.TestCase):
	def setUp(self):
		self.f1_data_object = f1.F1Department()
		self.data = self.f1_data_object.f1_data

	def test_class_F1DepartmentDataJoin(self):
		self.assertIsInstance(self.f1_data_object, f1.F1Department, 'The object is not of class f1.F1Department!')

	def test_data_not_null(self):
		self.assertFalse(self.data.empty, 'The data is empty!')

	def test_driver_most_wins(self):
		self.assertNotEqual(self.f1_data_object.driver_most_wins(), None, 'The method driver_most_wins is null!')

	def test_driver_most_poles(self):
		self.assertNotEqual(self.f1_data_object.driver_most_poles(), None, 'The method driver_most_poles is null!')

	def test_nationality_most_wins(self):
		self.assertNotEqual(self.f1_data_object.nationality_most_wins(), None, 'The method nationality_most_wins is null!')

	def test_constructor_most_laps_led(self):
		self.assertEqual(self.f1_data_object.constructor_most_laps_led(), 0, 'The method constructor_most_laps_led do not return 0!')

	def test_constructor_most_points(self):
		self.assertEqual(self.f1_data_object.constructor_most_points(), 0, 'The method constructor_most_points do not return 0!')

if __name__ == '__main__':
	unittest.main()
