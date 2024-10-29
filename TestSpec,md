Test Specification Document
This document outlines the test cases designed to validate the implementation of the StringCalculator function. The StringCalculator function parses strings of numbers separated by delimiters (commas, new lines, or custom delimiters) and returns their sum. It handles both functional and edge case scenarios to ensure the function works as expected.

Features to be Tested
Basic Summation

Summing numbers separated by commas.
Handling Different Delimiters

Supporting both commas and newlines as delimiters.
Supporting custom delimiters provided at the beginning of the string.
Edge Cases

Handling empty strings.
Ignoring numbers larger than 1000.
Throwing an exception when encountering negative numbers.
Handling multiple negative numbers in the exception message.

Test Cases
Test Case 1: Empty String Input
Test Case ID: TC1
Objective: Verify that the function returns 0 when provided an empty string.
Input: ""
Expected Output: 0
Rationale: An empty string should return 0 as there are no numbers to sum.

Test Case 2: Single Number Input
Test Case ID: TC2
Objective: Verify that the function correctly returns a single number when provided.
Input: "0"
Expected Output: 0
Rationale: A single number should be returned as the sum of itself.

Test Case 3: Two Numbers Input
Test Case ID: TC3
Objective: Verify that the function correctly sums two numbers separated by a comma.
Input: "1,2"
Expected Output: 3
Rationale: The sum of 1 and 2 should be 3.

Test Case 4: Ignoring Numbers Greater Than 1000
Test Case ID: TC4
Objective: Verify that the function ignores numbers greater than 1000.
Input: "1,1001"
Expected Output: 1
Rationale: Numbers greater than 1000 should be ignored in the sum.

Test Case 5: Sum with Custom Delimiter
Test Case ID: TC5
Objective: Ensure that the function can handle custom delimiters specified in the input string.
Input: "//;\n1;2"
Expected Output: 3
Rationale: The custom delimiter ; is used to separate numbers, and the sum of 1 and 2 should be 3.

Test Case 6: Sum with Newline Delimiter
Test Case ID: TC6
Objective: Verify that the function can sum numbers separated by newline characters as delimiters.
Input: "1\n2,3"
Expected Output: 6
Rationale: The sum of 1, 2, and 3 is 6, and newlines should be treated as valid delimiters.

Test Case 7: Negative Number Throws Exception
Test Case ID: TC7
Objective: Ensure that the function throws an exception when encountering negative numbers.
Input: "1,-2,3"
Expected Output: Exception: "Negatives not allowed: -2"
Rationale: Negative numbers are not allowed, and an exception should be thrown indicating the negative number.

Test Case 8: Multiple Negatives in Exception
Test Case ID: TC8
Objective: Verify that the function handles multiple negative numbers by including all of them in the exception message.
Input: "1,-2,-3"
Expected Output: Exception: "Negatives not allowed: -2, -3"
Rationale: All negative numbers encountered should be listed in the exception message.

Test Case 9: Handling Large Custom Delimiters
Test Case ID: TC9
Objective: Ensure the function can handle delimiters of any length.
Input: "//[***]\n1***2***3"
Expected Output: 6
Rationale: The custom delimiter *** should be used to separate the numbers, resulting in the sum of 6.

Test Case 10: Multiple Delimiters
Test Case ID: TC10
Objective: Ensure that the function can handle multiple delimiters in the input string.
Input: "1\n2,3"
Expected Output: 6
Rationale: The function should correctly sum numbers separated by both commas and newlines.

Conclusion
The test cases outlined in this document ensure that the StringCalculator function adheres to the specified requirements. The test cases cover basic functionality, various types of delimiters, and edge cases like negative numbers and large values. By thoroughly testing these scenarios, we can ensure that the function is robust and behaves as expected under different conditions.
