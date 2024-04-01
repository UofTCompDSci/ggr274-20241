# This import is required to import Jupyter notebooks like regular Python files
from notebook_helper import importer

# This imports the student notebook, but does not yet run all the code cells
# The module name needs to matche the student file name, omitting the .ipynb extension
import Homework_8 as hw
import Homework_8_solution as solution

# This is a library for helping write some tests
import cds_testing

import numpy as np
import pandas as pd

import pytest


@pytest.fixture(scope='module', autouse=True)
def run_notebook():
    """This executes the code in the notebook before running the tests."""
    importer.run_cells(hw, raise_on_error=False)
    importer.run_cells(solution, raise_on_error=False)


# This executes the code in the student and solution notebooks before running the tests.
load_student_code = pytest.fixture(cds_testing.load_code, params=[hw], scope='module', autouse=True)
load_solution_code = pytest.fixture(cds_testing.load_code, params=[solution], scope='module', autouse=True)

@pytest.fixture(scope='module', autouse=True)
def expected_shuffled_diffs_10000(run_notebook):
    """
    Since the dataset sample will vary for students based on their student numbers,
    we have to load the shuffled_diffs_10000 for each student number rather than referencing the solution.
    """
    
    student_number = getattr(hw, "student_number", None)

    if student_number is None:
        return None
    
    np.random.seed(hw.student_number)

    return solution.shuffled_diffs(10000)

def test_mhvisitinstab_without_instab_HL_column():
    """Test that the 'mhvisitinstab' dataframe is correctly created in your notebook up to step 3 before creating the `instab_HL` column. 
    """

    # Since the dataframe later gets changed, we verify the correctness for it upto step 3 of the homework.
    # Check that the variable exists in the notebook
    assert hasattr(hw, 'mhvisitinstab'),\
            'We could not find a DataFrame called "mhvisitinstab" in your file.'

    # Make sure that the variable is a pandas dataframe
    assert isinstance(hw.mhvisitinstab, pd.DataFrame),\
        'Your mhvisitinstab variable is incorrectly defined. It should refer to a Pandas dataframe.'


    # Copy the columns required only for task 1c. 
    hw_df_copy = hw.mhvisitinstab.copy()
    soln_df_copy = solution.mhvisitinstab.copy()

    hw_df_copy.drop(columns=['instab_HL'], inplace=True)
    soln_df_copy.drop(columns=['instab_HL'], inplace=True)

    pd.testing.assert_frame_equal(hw_df_copy, soln_df_copy, obj="(Step 3) mhvisitinstab")

def test_student_number():
    """Test that the 'student_number' variable has been defined correctly
    in your notebook.
    """

    assert hasattr(hw, 'student_number'),\
            'We could not find a variable called "student_number" in your file.'

    # Check that the number has been defined as an integer
    assert isinstance(hw.student_number, int),\
        'Your student_number variable should be an integer'


def test_shuffled_diffs_function_exists():

    # Test that the function exists in the student solution and takes in two arguments
    assert "shuffled_diffs" in dir(hw),\
        'The function "shuffled_diffs" is not defined in your notebook.'
    assert hw.shuffled_diffs.__code__.co_argcount == 1, \
        'The function "shuffled_diffs", should have 1 argument, number_of_shuffles (an integer).'

def test_shuffled_diffs_10000(expected_shuffled_diffs_10000):
    """Test that the 'shuffled_diffs_10000' variable has been defined correctly
    in your notebook.
    """

    # To load the data, we need their student number
    # This is just a check. The previous student number test would give them more information about their mistake.
    assert hasattr(hw, 'student_number') and isinstance(hw.student_number, int),\
        'We could not test for the "sub_time_use_data" variable as it is based on the student_number variable, which is incorrectly defined or missing.'


    assert hasattr(hw, 'shuffled_diffs_10000'),\
            'We could not find a variable called "shuffled_diffs_10000" in your file.'

    # Check that the number has been defined as an integer
    assert isinstance(hw.shuffled_diffs_10000, list),\
        'Your shuffled_diffs_10000 variable should be a list.'


    cds_testing.assert_list_equality(student_value=hw.shuffled_diffs_10000, soln_value = expected_shuffled_diffs_10000, var_name='shuffled_diffs_10000')

def test_rightextreme(expected_shuffled_diffs_10000):
    """Test that the 'rightextreme' variable has been defined correctly
    in your notebook.
    """

    # To load the data, we need their student number
    # This is just a check. The previous student number test would give them more information about their mistake.
    assert hasattr(hw, 'student_number') and isinstance(hw.student_number, int),\
        'We could not test for the "rightextreme" variable as it is based on the student_number variable, which is incorrectly defined or missing.'

    assert hasattr(hw, 'rightextreme'),\
            'We could not find a variable called "rightextreme" in your file.'

    # Check that the number has been defined as an integer
    assert isinstance(hw.rightextreme, (int, np.int_)),\
        'Your rightextreme variable should be an integer or a numpy integer.'

    expected_rightextreme = expected_shuffled_diffs_10000 >= solution.median_diff
    expected_rightextreme = expected_rightextreme.sum()

    msg = (
        f"\n"
        f"ISSUE FOUND: The value of your list variable `rightextreme`:\n"
        f"\n"
        f"     {hw.rightextreme}"
        f"\n\n"
        f"is not equal to what we expect:\n"
        f"\n"
        f"     {expected_rightextreme}\n"
    )
    assert hw.rightextreme == expected_rightextreme, msg

def test_leftextreme(expected_shuffled_diffs_10000):
    """Test that the 'leftextreme' variable has been defined correctly
    in your notebook.
    """
    # To load the data, we need their student number
    # This is just a check. The previous student number test would give them more information about their mistake.
    assert hasattr(hw, 'student_number') and isinstance(hw.student_number, int),\
        'We could not test for the "leftextreme" variable as it is based on the student_number variable, which is incorrectly defined or missing.'

    assert hasattr(hw, 'leftextreme'),\
            'We could not find a variable called "leftextreme" in your file.'

    assert isinstance(hw.leftextreme, (int, np.int_)),\
        'Your leftextreme variable should be an integer or a numpy integer.'

    expected_leftextreme = expected_shuffled_diffs_10000 < -1*solution.median_diff
    expected_leftextreme = expected_leftextreme.sum()

    msg = (
        f"\n"
        f"ISSUE FOUND: The value of your list variable `leftextreme`:\n"
        f"\n"
        f"     {hw.leftextreme}"
        f"\n\n"
        f"is not equal to what we expect:\n"
        f"\n"
        f"     {expected_leftextreme}\n"
    )
    assert hw.leftextreme == expected_leftextreme, msg


def test_pvalue(expected_shuffled_diffs_10000):
    """Test that the 'pvalue' variable has been defined correctly
    in your notebook.
    """

    # To load the data, we need their student number
    # This is just a check. The previous student number test would give them more information about their mistake.
    assert hasattr(hw, 'student_number') and isinstance(hw.student_number, int),\
        'We could not test for the "pvalue" variable as it is based on the student_number variable, which is incorrectly defined or missing.'


    assert hasattr(hw, 'pvalue'),\
            'We could not find a variable called "pvalue" in your file.'

    # Check that the number has been defined as an integer
    assert isinstance(hw.pvalue, (float, np.float_)),\
        'Your pvalue variable should be a float or a numpy float.'


    expected_rightextreme = expected_shuffled_diffs_10000 >= solution.median_diff
    expected_rightextreme = expected_rightextreme.sum()
    expected_leftextreme = expected_shuffled_diffs_10000 < -1*solution.median_diff
    expected_leftextreme = expected_leftextreme.sum()
    expected_pvalue = (expected_leftextreme + expected_rightextreme)/10000

    msg = (
        f"\n"
        f"ISSUE FOUND: The value of your list variable `pvalue`:\n"
        f"\n"
        f"     {hw.pvalue}"
        f"\n\n"
        f"is not equal to what we expect:\n"
        f"\n"
        f"     {expected_pvalue}\n"
    )
    assert hw.pvalue == expected_pvalue, msg


def test_nullhypothesis_distribution_plot(expected_shuffled_diffs_10000):
    """Test that the 'nullhypothesis_distribution_plot' plot has been created correctly
    in your notebook.
    """

    # To load the data, we need their student number
    # This is just a check. The previous student number test would give them more information about their mistake.
    assert hasattr(hw, 'student_number') and isinstance(hw.student_number, int),\
        'We could not test for the "pvalue" variable as it is based on the student_number variable, which is incorrectly defined or missing.'


    assert hasattr(hw, 'pvalue'),\
            'We could not find a variable called "pvalue" in your file.'

    # Check that the number has been defined as an integer
    assert isinstance(hw.pvalue, (float, np.float_)),\
        'Your pvalue variable should be a float or a numpy float.'

    expected_rightextreme = expected_shuffled_diffs_10000 >= solution.median_diff
    expected_rightextreme = expected_rightextreme.sum()
    expected_leftextreme = expected_shuffled_diffs_10000 < -1*solution.median_diff
    expected_leftextreme = expected_leftextreme.sum()
    expected_pvalue = (expected_leftextreme + expected_rightextreme)/10000

    msg = (
        f"\n"
        f"ISSUE FOUND: The value of your list variable `pvalue`:\n"
        f"\n"
        f"     {hw.pvalue}"
        f"\n\n"
        f"is not equal to what we expect:\n"
        f"\n"
        f"     {expected_pvalue}\n"
    )
    assert hw.pvalue == expected_pvalue, msg

EXPECTED_VARS = {
    # Step 1
    'marg_neighb': {},
    'instability_df': {},
    # Step 2
    'mentalhealth_neighb': {},
    'mhvisitrates': {},
    # Step 4
    'mhvisitinstab': {},
    'instab_HL_frequencies': {},
    # Step 5
    'median_table': {},
    'median_diff': {}
}

test_variable_names = cds_testing.make_variable_names_test(hw, EXPECTED_VARS)
test_answer_equality = cds_testing.make_answer_equality_test(hw, solution, EXPECTED_VARS)
