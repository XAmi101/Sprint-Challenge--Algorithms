'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#PLAN
    #base case-since there can't be matches
        # return 0
    #if "th" is in the first 2 letters of the word
        # return the index a  adds 1 
    #else it doesn't match so move on


def count_th(word):

    if len(word) == 0 or len(word) < 2:
        return 0
    # print(word[0], word[1], word[1:] )  

    # if word[0] == 't' and word[1] == 'h':
    if word[:2] == "th":
        return count_th(word[1:]) + 1    

    else:
        return count_th(word[1:])
    # print(count_th("thwosiothhtthth"))


