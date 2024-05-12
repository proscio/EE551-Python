# Patrick Roscio
# Lab_9 palindromeRec.py
# Description: By breaking the word into two letters based on the variables A and B, we clal a recursie function to test if A = B
# By returning a Boolean variable, we are able to include it in the while loop determinig if the word is not a pallindrome at any 
# comparison point. Our Base case is when X == 1, hence no more splitting and no more need to call the recursive function exists. 

def letter_test(A , B):
    if A == B:
        return True
    else: 
        return False

def word_break(test_word):
    x = int(0.5*len(test_word))
    A = test_word[x]
    B = test_word[-(x+1)]
    while x > 1 and letter_test(A,B):
        x -= 1
        A = test_word[x]
        B = test_word[-(x+1)]
    if x == 1: 
        return True
    else:     
        return False

def main():
    test_word = input("Please enter a word to test if it is a Pallindrome: ")
    if word_break(test_word):
        print(f"{test_word} is a pallindrome!")
    else: 
        print(f"{test_word} is not a pallindrome!")
main()