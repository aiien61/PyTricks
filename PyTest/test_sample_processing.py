from sample_processing import my_processing, OutsideAPI
from unittest.mock import patch, MagicMock
import unittest

class TestMyClass(unittest.TestCase):
    # 使用修飾器並以 APIMOCK 取代 OutsideAPI
    @patch('sample_processing.OutsideAPI')
    def test_my_processing(self, APIMock):
        api = APIMock()
        api.do_something.return_value = "result by simulated replacement"

        # 以模擬取代相依處理後執行 my_processing() 的處理
        # do_something() => "result by simulated replacement"
        # my_processing() => do_something() + " returning something"
        assert my_processing() == "result by simulated replacement returning something"

class TestMyClass2(unittest.TestCase):
    # 使用上下文管理器並以 APIMock 取代 OutsideAPI
    def test_my_processing(self):
        with patch('sample_processing.OutsideAPI') as APIMock:
            api = APIMock()
            api.do_something.return_value = "result by simulated replacement"

            # 以模擬取代相依處理後執行 my_processing() 的處理
            # do_something() => "result by simulated replacement"
            # my_processing() => do_something() + " returning something"
            assert my_processing() == "result by simulated replacement returning something"
        
        # 離開 with 語法後不適用 patch
        assert my_processing() == "API execution result returning something"

class TestMyClass3(unittest.TestCase):
    def test_my_processing(self):
        api = OutsideAPI()
        api.do_something = MagicMock()
        api.do_something.return_value = "result by simulated replacement"

        # Check if api has been called once or more
        # If not be called yet, raise AssertionError
        try:
            api.do_something.assert_called_with()
        except AssertionError as e:
            print(e)

        # api has been called twice
        # raise exception if api has been called more than once
        try:
            api.do_something()
            api.do_something.assert_called_once_with()
            api.do_something()
            api.do_something.assert_called_once_with()
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    unittest.main()
