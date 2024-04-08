# This import is required to import Jupyter notebooks like regular Python files
from notebook_helper import importer

# This imports the student notebook, but does not yet run all the code cells
# The module name needs to matche the student file name, omitting the .ipynb extension
import Homework_11 as hw
import Homework_11_solution as solution

# This is a library for helping write some tests
import cds_testing

import pytest
import matplotlib
import numpy as np

@pytest.fixture(scope='module', autouse=True)
def run_notebook():
    """This executes the code in the notebook before running the tests."""
    importer.run_cells(hw, raise_on_error=False)

# This executes the code in the student and solution notebooks before running the tests.
load_student_code = pytest.fixture(cds_testing.load_code, params=[hw], scope='module', autouse=True)
load_solution_code = pytest.fixture(cds_testing.load_code, params=[solution], scope='module', autouse=True)


def test_countries_gdf_plot():
    """Test that the 'countries_gdf_plot' variable has been defined 
    correctly in your notebook. 
    """
    
    # Check that the variable exists in the notebook
    assert hasattr(hw, 'countries_gdf_plot'),\
            'We could not find a variable called "countries_gdf_plot" in your file.'

    assert isinstance(hw.countries_gdf_plot, matplotlib.axes.SubplotBase),\
        'Your countries_gdf_plot variable is incorrectly defined. It should be created by calling the plot method'


def test_countries_gdp_gdf_plot():
    """Test that the 'countries_gdp_gdf_plot' variable has been defined 
    correctly in your notebook. 
    """
    
    # Check that the variable exists in the notebook
    assert hasattr(hw, 'countries_gdp_gdf_plot'),\
            'We could not find a variable called "countries_gdp_gdf_plot" in your file.'

    assert isinstance(hw.countries_gdp_gdf_plot, matplotlib.axes.SubplotBase),\
        'Your countries_gdp_gdf_plot variable is incorrectly defined. It should be created by calling the plot method'

    hw_cmap = hw.countries_gdp_gdf_plot.get_children()[0].properties()['cmap'].name
    soln_cmap = solution.countries_gdp_gdf_plot.get_children()[0].properties()['cmap'].name
    assert hw_cmap == soln_cmap, \
            "The cmap argument needs to be set to YlOrRd"
    
    hw_edge_colour = hw.countries_gdp_gdf_plot.get_children()[0].properties()['edgecolor']
    soln_edge_colour = solution.countries_gdp_gdf_plot.get_children()[0].properties()['edgecolor']
    assert np.array_equal(hw_edge_colour, soln_edge_colour), \
            "The edge colour argument needs to be set to black"

    # The 11th index of the children should be the one for the legend definitions 
    hw_legend_title = hw.countries_gdp_gdf_plot.get_children()[11].properties()
    soln_legend_title = solution.countries_gdp_gdf_plot.get_children()[11].properties()['title']
    assert 'title' in hw_legend_title, \
        "The legend argument must be set to True."

    assert hw_legend_title['title'].properties()['text'] == soln_legend_title.properties()['text'], \
            "The legend of the plot has been incorrectly set."

EXPECTED_VARS = {
    # Step 1
    'gdp_data_df': {},
    'gdp_2020': {}, 
    'gdp_2020_df': {},
    # Step 2
    'countries_gdf': {},
    # Step 3
    'countries_gdp_gdf': {},
}

test_variable_names = cds_testing.make_variable_names_test(hw, EXPECTED_VARS)
test_answer_equality = cds_testing.make_answer_equality_test(hw, solution, EXPECTED_VARS)
