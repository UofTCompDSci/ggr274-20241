"""Automated tests for GGR274 Homework 4

Installation instructions (if running locally)
==============================================

This test script requires a few different libraries, which you can install with:

$ pip install pytest
$ pip install 'git+https://github.com/MarkUsProject/autotest-helpers.git#subdirectory=notebook_helper'
$ pip install 'git+https://github.com/UofTCompDSci/cds-testing'

After installing the libraries, you can run the tests in this file from the command line using:

$ pytest test_hw3.py
"""
# This import is required to import Jupyter notebooks like regular Python files
from notebook_helper import importer

# This imports the student notebook, but does not yet run all the code cells
# The module name needs to matche the student file name, omitting the .ipynb extension
import Homework_4 as hw
import Homework_4_solution as solution

# This is a library for helping write some tests
import cds_testing

import pytest


@pytest.fixture(scope='module', autouse=True)
def run_notebook():
    """This executes the code in the notebook before running the tests."""
    importer.run_cells(hw, raise_on_error=False)

# This executes the code in the student and solution notebooks before running the tests.
load_student_code = pytest.fixture(cds_testing.load_code, params=[hw], scope='module', autouse=True)
load_solution_code = pytest.fixture(cds_testing.load_code, params=[solution], scope='module', autouse=True)


# Check for the exact values of the variables
TASK_VARS = {'time_use_data_raw': {},                 # Task 1a
             'time_use_data': {},                     # Task 1b
             'new_column_names': {},                  # Task 1c
             'clean_time_use_data': {},               # Task 1d
             'transit_yes': {},                       # Start of Task 2a
             'transit_no': {},
             'rural': {},
             'transit_col_type': {},                  # Start of Task 2b
             'transit_data_type': {},
             'total_rural': {},                       # Task 3a
             'rural_rush_transit': {},                # Task 3b
             'rural_rush_transit_num': {},            # Task 3b
             'rural_rush_transit_prop': {},           # Task 3c
             'rural_rush_notransit': {},              # Task 3e
             'rural_rush_notransit': {},              # Task 3e
             'rural_rush_monthly_prop': {}}           # Task 3f

test_variable_names = cds_testing.make_variable_names_test(hw, TASK_VARS)
test_expected_value = cds_testing.make_answer_equality_test(hw, solution, TASK_VARS)
