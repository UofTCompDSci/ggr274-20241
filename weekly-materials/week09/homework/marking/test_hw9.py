# This import is required to import Jupyter notebooks like regular Python files
from notebook_helper import importer

# This imports the student notebook, but does not yet run all the code cells
# The module name needs to matche the student file name, omitting the .ipynb extension
import Homework_9 as hw
import Homework_9_solution as solution

# This is a library for helping write some tests
import cds_testing

import pytest
import matplotlib


@pytest.fixture(scope='module', autouse=True)
def run_notebook():
    """This executes the code in the notebook before running the tests."""
    importer.run_cells(hw, raise_on_error=False)

# This executes the code in the student and solution notebooks before running the tests.
load_student_code = pytest.fixture(cds_testing.load_code, params=[hw], scope='module', autouse=True)
load_solution_code = pytest.fixture(cds_testing.load_code, params=[solution], scope='module', autouse=True)

def test_one_bs_mean_function_exists():
    # Test that the function exists in the student solution and takes in two arguments
    assert "one_bs_mean" in dir(hw),\
        'The function "one_bs_mean" is not defined in your notebook.'

def test_bootstrap_means_histogram():
    """Test that the 'bootstrap_means_histogram' variable has been defined 
    correctly in your notebook. 
    """
    
    # Check that the variable exists in the notebook
    assert hasattr(hw, 'bootstrap_means_histogram'),\
            'We could not find a variable called "bootstrap_means_histogram" in your file.'

    # Make sure that the variable is string
    assert isinstance(hw.bootstrap_means_histogram, tuple) and len(hw.bootstrap_means_histogram) == 3 \
           and isinstance(hw.bootstrap_means_histogram, type(solution.bootstrap_means_histogram)), \
        'Your bootstrap_means_histogram variable is incorrectly defined. It should be created by using the matplotlib library with the "hist" function.'

    hw_rectangles = hw.bootstrap_means_histogram[2].patches
    soln_edge_col = solution.bootstrap_means_histogram[2].patches[0].get_edgecolor()
    soln_face_col = solution.bootstrap_means_histogram[2].patches[0].get_facecolor()

    for rec in hw_rectangles:
        assert rec.get_edgecolor() == soln_edge_col, \
            "The edge colour of the histogram should be red."
        assert rec.get_facecolor() == soln_face_col, \
            "The colour of the histogram should be cyan."

EXPECTED_VARS = {
    # Step 1
    'time_use_df': {},
    'drive_time_df': {},
    # Step 2
    'driver': {},
    'subset_drive_time_df': {},
    # Step 3
    'drive_time_avg': {},
    # Step 5
    'bootstrap_means': {},
    # Step 6
    'bootstrap_means_2p5_percentile': {},
    'bootstrap_means_97p5_percentile': {}
}

test_variable_names = cds_testing.make_variable_names_test(hw, EXPECTED_VARS)
test_answer_equality = cds_testing.make_answer_equality_test(hw, solution, EXPECTED_VARS)
