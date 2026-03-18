from sample_processing import OutsideAPI
from unittest.mock import MagicMock
from icecream import ic

api = OutsideAPI()
api.do_something = MagicMock()
ic(api.do_something)

api.do_something.return_value = "result by simulated replacement"
ic(api.do_something())

api.do_something.side_effect = Exception("Set Exception")
try:
    api.do_something()
except Exception as e:
    ic(e)
