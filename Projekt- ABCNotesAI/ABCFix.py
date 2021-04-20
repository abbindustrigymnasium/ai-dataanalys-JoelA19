abc = open("ABC.txt").read()
abclist = abc.split("\n")

newlist = [line for line in abclist if line and line[0] not in "BNZF%"]

newabc = "\n".join(newlist)

open("newabc.txt", "w").write(newabc)