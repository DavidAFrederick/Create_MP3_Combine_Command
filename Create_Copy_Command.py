# Python code to
# demonstrate readlines()

# dir /b /od disc1_*.mp3 > mp3_filename.txt


input_path = "C:\\temp\\Expanse_Nemisis_Disc1\\"
output_path = "C:\\temp\\Expanse_Nemisis\\"
bookname = "Expanse_Nemisis"

command = "copy /b "

# Using readlines()
#file1 = open('C:\\temp\\list_of_Files.txt', 'r')
file1 = open(input_path + 'mp3_filename.txt', 'r')
Lines = file1.readlines()

# Strips the newline character
for line in Lines:
    # print("Line{}: {}".format(line.strip()))
    line = line[:-1]
    command = command + "\""  + line + "\" + "
    underscore_position = line.find("_")
    diskname = line[0:underscore_position]

print ("Output file: " , diskname)
command = command[:-2]
command = command + output_path + bookname + "_" + diskname + ".mp3"

print (command)

# writing to file
file1 = open(input_path + 'Create_combine_File_Command.bat', 'w')
file1.writelines(command)
file1.close()
