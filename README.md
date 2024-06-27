# Overview
This repository contains some testing cases for flexibility design problems and some Python codes for generating new testing cases.
This is intended to provide some benchmarks for testing heuristics proposed for solving general flexibility design problems.
All testing cases are saved in .pkl format.

# Folders
- classical_fdp_test_cases—testing cases from two papers in the literature and the Python codes for generating the cases.
- example - 'example_read_testing_case.py' provides a simple example of reading a testing case.
- original_fctp_test_cases - flexibility design testing cases generated from the Fixed Charge Transportation (FCT) testing cases posted on the "DECISION TREE FOR OPTIMIZATION SOFTWARE" page (http://plato.asu.edu/guide.html). It also contains all of the original FCT testing cases and the ‘mps2input.py’ file, which reads the original mps files and convert into a flexibility design testing case.
- generic_test_cases - some generic flexibility design testing cases where the entries in the profit matrix are all equal to 1, and the fixed costs are all zero. 'inputgeneration.py' provides the code for generating such a testing case.
