"""

Note that the solution given in EPI assumes that a celebrity IS always present.
If a celebrity is present it WILL find him/her. But if the celebrity is not present we need to return -1.
So in each step we eliminate one person who for sure cant be celebrity. the last person who is standing may or may not be the celeb.
We need to check his rows and colums also. that is wht the last for loop is for.

"""
def findCelebrity(knows_relations):
    i = 0
    j = 1

    while(j < len(knows_relations[0])):
        if knows_relations[i][j]:
            i = j
            j += 1
        else:
            j += 1
    for x in range(len(knows_relations[0])):
        if x!= i and (knows_relations[i][x] or not knows_relations[x][i]):
            return -1
    return i