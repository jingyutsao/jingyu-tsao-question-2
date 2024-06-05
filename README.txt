main.py: The functions to process input and return the letter that only appear once.

test.py: The test script for main.py.

test_input_question_2.txt: All inputs that is used to test the functionality of the function.



The instruction for different purpose
instruction = 'first', 
1. Return the 'first' letter that only appear once
2. Treat uppercase and lowercase letters as the different character
3. Include the spaces in the index

instruction = 'all', 
1. Return 'all' letters that only appear once
2. Treat uppercase and lowercase letters as the same character
3. Exclude the spaces in the index


Example:
    abcdefgfedcba, first       # Expected output: "6" (character 'g')
    abcdeffedcba, first        # Expected output: "-1" (no unique character)
    aabbccddeeffg, first       # Expected output: "12" (character 'g')
    abcdabcd, first            # Expected output: "-1" (no unique character)
    a, first                   # Expected output: "0" (character 'a')
    , first                    # Expected output: "-1" (empty string)
    aaabcccdeeef, first        # Expected output: "3" (characters 'b')
    abcdeffghijkl, first       # Expected output: "0" (characters 'a')
    aa B C d Ef F g H H, first # Expected output: "3" (characters'B')
    Level up, first            # Expected output: "0" (characters 'L')
    Cute Cat, first            # Expected output: "1" (characters 'u')
    dog DOG dog, first         # Expected output: "4" (characters 'D')
    abcdefgfedcba, all         # Expected output: "6" (character 'g')
    abcdeffedcba, all          # Expected output: "-1" (no unique character)
    aabbccddeeffg, all         # Expected output: "12" (character 'g')
    abcdabcd, all              # Expected output: "-1" (no unique character)
    a, all                     # Expected output: "0" (character 'a')
    , all                      # Expected output: "-1" (empty string)
    aaabcccdeeef, all          # Expected output: "3,7,11" (characters 'b', 'd', 'f')
    abcdeffghijkl, all         # Expected output: "0,1,2,3,8,9,10,11" (characters 'a', 'b', 'c', 'd', 'h', 'i', 'j', 'k', 'l')
    aa B C d Ef F g H H, all   # Expected output: "2,3,4,5,8" (characters 'a', 'B', 'C', 'd', 'E', 'f', 'g')
    Level up, all              # Expected output: "2,5,6" (characters 'v', 'u', 'p')
    Cute Cat, all              # Expected output: "1,3,5" (characters 'u', 'e', 'a')
    dog DOG dog, all           # Expected output: "-1" (no unique character)

