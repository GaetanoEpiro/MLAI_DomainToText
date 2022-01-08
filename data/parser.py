
file = open("photo.txt", "r")
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
        if i == 0:
            out.write("\t\t\t\"high-level\",\n")
        elif i == 3:
            out.write("\t\t\t\"yes, colorful\",\n")
        elif i == 5:
            out.write("\t\t\t\"yes\",\n")
        elif i == 6:
            out.write("\t\t\t\"no\",\n")
        elif i == 7:
            out.write("\t\t\t\"yes, photo\",\n")
        else:
            out.write("\t\t\t\"\",\n")
    out.write("\t\t\t\"yes, realistic\"\n")
    out.write("\t\t]\n")
    out.write("\t},\n")


out.write("]")