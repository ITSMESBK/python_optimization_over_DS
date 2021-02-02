# =========================================================================================
# !/usr/bin/env python3
# Filename: search_string_data.py
# Description: Get Data from text file and find out financial terms 
# Author: Bharathkumar Sivakumar <BHARATH SBK @ITSMESBK>
# Python Environment - Python3
# Usage: Search a data from a document in more efficient way
# ===========================================================================================

# GENERIC PACKAGES
import sys,os

# Add Path in machine bash profile 
sys.path.append('C:/Users/kamal/Documents/sbk_repositories/python_utility/')# sys.path is a list of absolute path strings

# IN-HOUSE PACKAGES 
from constants import *
from common_helpers import *
from traversal_into_binary_tree import *
from traversal_into_doubly_linkedlist import *  

#File Open
file_rd = open(FINANCIAL_TXT_FILE,'r')
file_data = file_rd.read()
file_rd.close()

#GET DATA 
data_list = file_data.split(" ")
print(data_list)

