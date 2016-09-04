import sys
import os
import runpy
import time

params = sys.argv[1:]
sys.argv = sys.argv[:1]

path = os.path.dirname(sys.modules[__name__].__file__)
path = os.path.join(path, '..')
sys.path.insert(0, path)

all_unit_test_scripts = ['test_board',
                         'test_position',
                         'test_tile',
                         'test_settings',
                         'test_dimension_coordinate_properties']

if not params or params[0] in ['all', 'All', 'ALL']:
    params = all_unit_test_scripts

for param in params:
    try:
        print("Running " + param)
        runpy.run_module('lib.unit_tests.' + param, run_name="__main__", alter_sys=True)
    except SystemExit:
        time.sleep(1/100)  # Allow prints to show correctly
        continue
