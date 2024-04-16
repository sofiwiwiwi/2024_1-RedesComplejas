file = open("06.net", "r")
lines = []
for line in file:
    line = line.strip()
    if "Vertices" not in line and len(line.split(" ")) == 2:
        x = line.split(" ")[0]
        line = x + f' "{x}"'
    lines.append(line)
file.close()
file = open("06_mod.net", "w")
for line in lines:
    file.write(line)
    file.write("\n")
file.close()