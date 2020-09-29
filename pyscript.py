
def find_match(func, filename):
    lst=[]
    with open(filename, 'r') as file:
        for word in file.readlines(): 
            if func(word.rstrip("\n").lower()):
                lst.append((word.rstrip("\n"),"true"))     
        file.close()
    return lst


def is_match(word):
    if len(word) == 5:
        if word.find('a') == 0 and word.find('t') == 4:
            return True
    return False


lst = find_match(is_match,'words.txt')
print (lst)

def is_palindrome(word):
    "Is the word a palindrome?"
    left_pos = 0
    right_pos = len(word) - 1
    word = word.lower()
    while right_pos >= left_pos:
        if not word[left_pos] == word[right_pos]:    # if left does not = right, false
            return False
        left_pos += 1        # if left pos. = right pos., True
        right_pos -= 1
    return True

lst = find_match(is_palindrome,'words.txt')
print (lst)

def is_all_vowels(word):
    "Is every character in word a vowel?"
    for c in word.lower().rstrip("\n"):
        if c !="a" and c !="e" and c !="i" and c !="o" and c !="u":
            return False
        
    return True

lst = find_match(is_all_vowels,'words.txt')
print (lst)
