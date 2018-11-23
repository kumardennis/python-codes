import tkinter as tk
import urllib
import re
import os
import subprocess
import random
import string

window = tk.Tk()
window.title("Link Maker")
window.geometry("600x100")


#----Functions----

def linkMaker():
    link = str(entryLink.get())

    project = str(entryProject.get())

    #Make an empty array to store required links only and store the links in it

    text_file_link = []

    for x in range(10000):
        test = (' '.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(10)))
        text_file_link.append(test.replace(" ",""))

    #Find any duplicates

    if len(text_file_link) != len(set(text_file_link)):
        print("duplicates found")
    else:
        print("no duplicates found")

    ##########################################################################
    ################### ONLY CHANGE THE TWO VARIABLES DOWN BELOW #############
    ##########################################################################

    projectName = project


    baseLink = "https://web.norstatsurveys.com/survey/selfserve/53c/"+link.strip()+"?list=1&source="

    ############################################################################
    ############################################################################
    ############################################################################

    #Create new txt file in project folder to write data in it. Write the required coulumns in it

    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print('Error creating directory. ' + directory)

    createFolder('M:/tlf/'+projectName)

    os.chdir('M:/tlf/'+projectName)
    new_text_file = open("%s.txt" % projectName, "w+")
    new_text_file.write("Link\n")
    for i in text_file_link:
        new_text_file.write(baseLink.strip() + i + "\n")
        # print(baseLink.strip() + i + "\n")

    #Open the folders in explorer

    os.startfile('M:/tlf/'+projectName)

    #Close the files

    new_text_file.close()




#----Widgets----
label1 = tk.Label(text="Just fill in the necessary fields and press the button.")
label1.grid(column=0, row=0)

link = tk.Label(text="Please paste the baseLink")
link.grid(column=0, row=1)

entryLink = tk.Entry()
entryLink.grid(column=1, row=1)

project = tk.Label(text="Please paste the projectID")
project.grid(column=0, row=2)

entryProject = tk.Entry()
entryProject.grid(column=1, row=2)

button = tk.Button(text="Make The Links", command=linkMaker)
button.grid(column=1, row=3)

window.mainloop()
