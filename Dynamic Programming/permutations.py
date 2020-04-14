# def getPermutations(array, curPerm=[], permuatations=[]):
#     # Write your code here.
#     if len(array) == 0 and len(curPerm):
#         permuatations.append(curPerm)
#         return
#
#     for idx in range(len(array)):
#         no = array[idx]
#         newPerm = [no] + curPerm
#         getPermutations(array[0:idx] + array[idx + 1:], newPerm, permuatations)
#         # permutations.append([no] + getPermutations(array[0:idx] + array[idx+1:]))
#
#     return permuatations


def getPermutations(array, curPerm=[], permuatations=[]):
    # Write your code here.
    if len(array) == 0 and len(curPerm):
        permuatations.append(curPerm)
        return

    for idx in range(len(array)):
        no = array[idx]
        newPerm = [no] + curPerm
        getPermutations(array[0:idx] + array[idx + 1:], newPerm, permuatations)
        # permutations.append([no] + getPermutations(array[0:idx] + array[idx+1:]))
    print(permuatations)
    return permuatations


print(getPermutations([1, 2]))
