def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]


print(maskify(input()))