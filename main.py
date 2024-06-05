# -*- coding: utf-8 -*-
"""Return the letter that only appear once

instruction = 'first', 
1. Return the 'first' letter that only appear once
2. Treat uppercase and lowercase letters as the different character
3. Include the spaces in the index

instruction = 'all', 
1. Return 'all' letters that only appear once
2. Treat uppercase and lowercase letters as the same character
3. Exclude the spaces in the index

"""

import pandas as pd
from collections import Counter

def find_unique_char_indices(s, instruction):
    # Normalize the input: convert to lowercase and remove spaces
    normalized_s = s.replace(' ', '').lower()
    
    # Step 1: Count the frequency of each character
    char_count = Counter(s)
    char_count_normalized = Counter(normalized_s)
    
    # Step 2: Depending on the instruction, find the appropriate indices
    if instruction == 'first':
        for index, char in enumerate(s):
            if char != ' ' and char_count[char] == 1:
                return str(index)
        return '-1'
    elif instruction == 'all':
        unique_indices = [
            str(index) for index, char in enumerate(normalized_s)
            if char != ' ' and char_count_normalized[char] == 1
        ]
        return ','.join(unique_indices) if unique_indices else '-1'
    else:
        return 'Invalid instruction'

def process_file(file_path):
    inputs = []
    results = []

    with open(file_path, 'r') as file:
        # Generate outputs
        for line in file:
            input_str, instruction = line.strip().split(', ')
            result = find_unique_char_indices(input_str, instruction)
            
            inputs.append(input_str)
            results.append(result)
            
    # Create a DataFrame
    df = pd.DataFrame({
        'Input': inputs,
        'Output': results
    })
    
    return df
