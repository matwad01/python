import datetime
r"""
this script creates an empty files.
"""

filename = datetime.datetime.now()

#Create empty file
def create_file():
    """This function creates an empty file"""
    with open(filename.strftime("%Y-%m-%d-%h" + ".txt"), "w") as file:
        file.write("") #Writing empty string

create_file()
