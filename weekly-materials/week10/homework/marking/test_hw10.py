# This import is required to import Jupyter notebooks like regular Python files
from notebook_helper import importer

# This imports the student notebook, but does not yet run all the code cells
# The module name needs to matche the student file name, omitting the .ipynb extension
import Homework_10 as hw
import Homework_10_soln as solution

# This is a library for helping write some tests
import cds_testing

import pytest
import matplotlib
from statsmodels.formula.api import ols

@pytest.fixture(scope='module', autouse=True)
def run_notebook():
    """This executes the code in the notebook before running the tests."""
    importer.run_cells(hw, raise_on_error=False)

# This executes the code in the student and solution notebooks before running the tests.
load_student_code = pytest.fixture(cds_testing.load_code, params=[hw], scope='module', autouse=True)
load_solution_code = pytest.fixture(cds_testing.load_code, params=[solution], scope='module', autouse=True)

def test_regression_fitted():
    """Test that the regression model has been fitted
    """
    
    # Check that the variable exists in the notebook
    assert hasattr(hw, 'reg_mh_fit'),\
        'We could not find a variable called "reg_mh_fit" in your file.'
    
    # Make sure that the variable is a fitted regression model. 
    assert isinstance(hw.reg_mh_fit, type(solution.reg_mh_fit)),\
        'Your variable `reg_mh_fit` should be a fitted regression model.'

def test_regression_summary():
    """Test that the regression summary was correctly generated
    """
    
    # Check that the reg_mh_fit variable exists in the notebook
    assert hasattr(hw, 'reg_mh_fit'),\
        'We could not find a variable called "reg_mh_fit" in your file.'
    
    # Check that the variable exists in the notebook
    assert hasattr(hw, 'reg_mh_summary'),\
        'We could not find a variable called "reg_mh_summary" in your file.'

    # Make sure that the fitted regression model exists before checking the summary
    assert isinstance(hw.reg_mh_fit, type(solution.reg_mh_fit)),\
        'Your variable `reg_mh_fit` should be a fitted regression model.'
    
    assert str(hw.reg_mh_summary) == str(hw.reg_mh_fit.summary()),\
        'Your variable `reg_mh_summary` is not equal to the summary of the fitted model.'

def test_regression_r_squared_value():
    """Test that the r squared value of the regression model exists
    """
    
    # Check that the reg_mh_fit variable exists in the notebook
    assert hasattr(hw, 'reg_mh_fit'),\
        'We could not find a variable called "reg_mh_fit" in your file.'
    
    # Check that the variable exists in the notebook
    assert hasattr(hw, 'reg_rsquared'),\
        'We could not find a variable called "reg_rsquared" in your file.'

    # Make sure that the fitted regression model exists before checking the r squared value
    assert isinstance(hw.reg_mh_fit, type(solution.reg_mh_fit)),\
        'Your variable `reg_mh_fit` should be a fitted regression model.'

    # Make sure that the variable is a fitted regression model. 
    assert isinstance(hw.reg_rsquared, type(solution.reg_rsquared)),\
        'Your variable `reg_rsquared` should be a float.'
    
    assert hw.reg_rsquared == hw.reg_mh_fit.rsquared,\
        'Your variable `reg_rsquared` is not equal to the r-squared of the fitted model.'

EXPECTED_VARS = {
    # Step 1
    'socdem_neighb': {},
    # Step 2
    'socdem_neighb_important': {},
    # Task 1b 
    'mh_neighb': {},
    # Step 2
    'mh_visit_rates' : {},
    # Step 4
    'mh_socdem': {},
}

test_variable_names = cds_testing.make_variable_names_test(hw, EXPECTED_VARS)
test_answer_equality = cds_testing.make_answer_equality_test(hw, solution, EXPECTED_VARS)
