'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    th = list(word)
    if len(th) < 2:
        return 0
    elif th[0] == 't' and th[1] == 'h':
        count += 1
    return count + count_th(th[1:])



    
    
