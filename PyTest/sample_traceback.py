import traceback
import logging

def hoge():
    tuple()[0]

try:
    hoge()
except IndexError:
    print('--- Exception occurred ---')
    traceback.print_exc(limit=None)

try:
    hoge()
except IndexError:
    print('--- Exception occurred ---')
    traceback.print_exc(limit=1)

logging.basicConfig(filename='example.log', 
                    format='%(asctime)s %(levelname)s %(message)s')

try:
    tuple()[0]
except IndexError as e:
    logging.error(traceback.format_exc())
    print(e)