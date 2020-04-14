permuations = []


def rearrangeWord(word):
    # Write your code here
    pass


def strPermuation(word, perm):
    if len(word) == 0:
        if perm not in permuations:
            return perm

    for i in range(len(word)):
        ch = word[i]
        ros = word[0: i] + word[i + 1:]

        strPermuation(ros, perm + ch)


word = "bcda"
print(strPermuation(word, ""))
