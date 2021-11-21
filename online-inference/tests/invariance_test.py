
import json
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests
import time
import unittest

from app.main import predict

example_path_dir = '../wine-examples'
test_examples = os.listdir(example_path_dir)
print(test_examples)

class E2eInvarianceTest(unittest.TestCase):
  def setUp(self) -> None:
      self.elapsed_time = 0

  def tearDown(self) -> None:
    print(f"Total analysis elapsed time: %.5f s" % self.elapsed_time)

  def test_result_is_equal_to_snapshot(self):
    for test_example in test_examples:
      with self.subTest(msg=test_example):
        with open(os.path.join(example_path_dir, test_example)) as f:
          data = json.load(f)
          actual_result = os.path.splitext(test_example)[0]
          
          start_time = time.time()
          expected_result = predict(data)
          analysis_time = time.time() - start_time
          self.elapsed_time += analysis_time
          print(f"Analysis elapsed time: %.5f s" % analysis_time)

          self.assertEqual(actual_result, expected_result)

  def test_result_is_equal_to_snapshot2(self, mock_post):
    for test_example in test_examples:
      with self.subTest(msg=test_example):
        with open(os.path.join(example_path_dir, test_example)) as f:
          data = json.load(f)
          actual_result = os.path.splitext(test_example)[0]
          
          start_time = time.time()
          expected_result = requests.post("http://localhost/predict", data=data, headers={'Content-Type: application/json'})
          analysis_time = time.time() - start_time
          self.elapsed_time += analysis_time
          print(f"Analysis elapsed time: %.5f s" % analysis_time)

          self.assertEqual(actual_result, expected_result)
          
          
          
