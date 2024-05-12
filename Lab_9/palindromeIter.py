# Patrick Roscio
# Lab_9 palindromeIter.py
# Description: Tests if user input is a pallindrome by comparing the equal-distant letters.
    # Returns a boolean value to main and prints appropriate statment. 

def palinTest(test_word):
    test_word = test_word.lower()
    start = 0 
    end = len(test_word) -1
    while start < end:
        if test_word[start] != test_word[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

   
    
def main():
    test_word = input("Please enter a word to test if it is a Pallindrome: ")
    if palinTest(test_word):
        print(f"{test_word} is a pallindrome!")
    else: 
        print(f"{test_word} is not a pallindrome!")
main()