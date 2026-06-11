def reverseWords( s):
    words=s.split()
    rev_words=words[::-1]
    result=" ".join(rev_words)
    return result
