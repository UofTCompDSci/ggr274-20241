# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 12:22:03 2022

@author: Amar
"""

import numpy as np
import pandas as pd

data = pd.read_csv("covid_sex_raw.csv")

# Filter out any rows that have missing values
data = data.loc[data.notnull().all(axis=1),:]

# Fix the formatting of total_cases, total_deaths, male_case_rates, female_case_rates
# From mix of string and int/float to all float

# split out any unwanted delimiters 
def parse_commas(series):
    return pd.to_numeric(series.str.split(",").str.join(""),
                         errors="coerce")

# not the best, but not sure how i can use apply to mutate in-place?
data[["Total_cases", 
      "Male_cases_rate", 
      "Female_cases_rate", 
      "Total_deaths"]] = data[[
          "Total_cases", 
          "Male_cases_rate", 
          "Female_cases_rate",
          "Total_deaths"]].apply( 
    parse_commas, axis=1)
              
data.to_csv('../covid_raw_w2.csv')
              

#test2=data["Male_case_rate"].str.split(",").str.join("")