import operator
import functools

problem = open("daytwo.txt")

problist = []
for line in problem:
    data = line.split(sep="x")
    idata = []
    for d in data:
        idata.append(int(d))
    problist.append(idata)

paper = []
ribbon = []
for i in problist:
    l = i[0]
    w = i[1]
    h = i[2]
    if l == w == h:  # life is easy if it's a cube
        smallest_side = l * w
        ribbon_len = (l + h) * 2 + (l * w * h)
    else:
        largest = max(i)
        smallest_side = [j for j in i if j != largest]  # a list [Y,Z] where Y and Z are height & width of smallest side
        if len(smallest_side) != 2:  # if a package is YxYxZ where Y > Z, append Y to extra smallest_side will be only Z
            smallest_side.append(largest)
        ribbon_len = (sum(smallest_side) * 2) + (l * w * h)  # find the ribbon length (smallest perimeter + cubic feet)
        smallest_side = functools.reduce(operator.mul, smallest_side)  # then find the smallest side
    paper_area = (2 * l * w) + (2 * w * h) + (2 * h * l)
    paper.append(paper_area + smallest_side)
    ribbon.append(ribbon_len)

print(sum(paper), "square feet of wrapping paper.")
print(sum(ribbon), "feet of ribbon.")
