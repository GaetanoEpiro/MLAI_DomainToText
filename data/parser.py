file = open("cartoon.txt", "r")
out = open("image_descriptions.json", "w")

lines = file.readlines()

out.write("[\n")

for line in lines:
    line = line.replace("\n", "")
    fields = line.split(" ")

    out.write("\t{\n")
    out.write("\t\t" + "\"image_name\": " + "\"" + fields[0] + "\",\n")
    out.write("\t\t" + "\"descriptions:\": [\n")
    for i in range(8):
        out.write("\t\t\t\"\",\n")
    out.write("\t\t\t\"\"\n")
    out.write("\t\t]\n")
    out.write("\t},\n")


out.write("]")