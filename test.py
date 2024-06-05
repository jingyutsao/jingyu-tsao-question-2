# -*- coding: utf-8 -*-
"""Test script for jingyu_tsao_question_2.py"""

import pandas as pd
from jingyu_tsao_question_2 import process_file

file_path = "./test_input_question_2.txt"

if __name__ == "__main__":
    df = process_file(file_path)
    print(df)
