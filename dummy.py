# automation_script.py - Contains intentional issues for code review testing

import os
import sys
from collections import *
import re

# Missing docstring for module

def process_data(data):
    # Poor function name and missing docstring
    result=[]
    for item in data:
        if item != None:  # Should use 'is not None'
            result.append(item*2)
    return result

class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.results = []
        
    def validate_email(self, email):
        # Weak email validation - security issue
        if "@" in email:
            return True
        return False
    
    def divide_numbers(self, a, b):
        # No error handling for division by zero
        return a / b
    
    def read_file(self, filename):
        # Poor error handling and file resource management
        try:
            f = open(filename, 'r')
            content = f.read()
            return content
        except:
            print("Error occurred")
            return None
    
    def count_vowels(self,word):
        # Poor spacing and inefficient logic
        vowels=0
        for letter in word:
            if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
                vowels+=1
        return vowels
    
    def find_duplicates(self, lst):
        # Inefficient O(n²) algorithm
        duplicates = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] == lst[j] and lst[i] not in duplicates:
                    duplicates.append(lst[i])
        return duplicates
    
    def calculate_price(self, price, tax_rate=0.1):
        # Mutable default argument issue (not in this case, but similar pattern)
        if price < 0:
            return "Invalid price"  # Inconsistent return types
        total = price * (1 + tax_rate)
        return total

def main():
    # Hardcoded values and poor error handling
    API_KEY = "abc123_secret_key"  # Security issue - hardcoded credential
    
    processor = DataProcessor([1, 2, 3, 4, 5])
    
    # No input validation
    user_input = input("Enter a number: ")
    number = int(user_input)  # Can crash if not a number
    
    # Unused variables
    unused_var = "This is never used"
    temp_data = [1, 2, 3]
    
    result = processor.divide_numbers(10, 0)  # Will cause ZeroDivisionError
    print("Result:", result)
    
    # Poor exception handling
    try:
        risky_operation = 10 / 0
    except:
        pass  # Empty except block
    
    # Long line that violates PEP 8
    long_string = "This is a very long string that exceeds the recommended 79 character limit and should be broken into multiple lines for better readability"
    
    return 0

if __name__ == "__main__":
    main()
