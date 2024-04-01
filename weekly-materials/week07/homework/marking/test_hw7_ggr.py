# This import is required to import Jupyter notebooks like regular Python files
from notebook_helper import importer

# This imports the student notebook, but does not yet run all the code cells
# The module name needs to matche the student file name, omitting the .ipynb extension
import Homework_7 as hw
import Homework_7_solution as solution

# This is a library for helping write some tests
import cds_testing

import numpy as np

import pytest


@pytest.fixture(scope='module', autouse=True)
def run_notebook():
    """This executes the code in the notebook before running the tests."""
    importer.run_cells(hw, raise_on_error=False)

# This executes the code in the student and solution notebooks before running the tests.
load_student_code = pytest.fixture(cds_testing.load_code, params=[hw], scope='module', autouse=True)
load_solution_code = pytest.fixture(cds_testing.load_code, params=[solution], scope='module', autouse=True)


def test_simulate_sample_means_function_exists():

    # Test that the function exists in the student solution and takes in two arguments
    assert "simulate_sample_means" in dir(hw),\
        'The function "simulate_sample_means" is not defined in your notebook.'
    assert hw.simulate_sample_means.__code__.co_argcount == 2, \
        'The function "simulate_sample_means", should have 2 arguments, data (a DataFrame) and N (an integer).'

EXPECTED_VARS = {
    # Data section
    'time_use_data_raw': {},
    'time_use_dur': {},
    'new_column_names': {},
    'time_use_data': {},
    # Computation section
    'clean_nonzero': {},
    'summary_stats': {},
    'empirical_mean_time_spent_cleaning': {},
    'sample_sizes': {},
    'all_sample_means_by_sample_size': {},
    'sample_means_by_sample_size': {},
    'mean_of_sample_means_by_sample_size': {},
    'diff_sample_mean_empirical_means_by_sample_size': {}
}

test_variable_names = cds_testing.make_variable_names_test(hw, EXPECTED_VARS)
test_answer_equality = cds_testing.make_answer_equality_test(hw, solution, EXPECTED_VARS)
