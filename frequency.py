"""
Input : "which is better python 2 or python 3"
Output: [("2", 1), ("3",2), ("better", 1), ("is",1), ("or",1), ("python",2), ("which",1)]
"""

def compute_frequency(data):
    """
    Computes the frequency of words 
    Args:
        data (str): Text
    """
    words = data.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    words_sorted = sorted(word_count)
    result = [(i, word_count[i]) for i in words_sorted]
    return result
