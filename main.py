# Ultima V Trainer/hacker program by Aryan Sanyal
# Made for CECS 378 Section 1 with Anthony Giacalone
# I had quite some fun with this so I hope you enjoy the little jokes here and there!

import tkinter as tk
from tkinter import filedialog, Text, END
import os
import numpy as np
import re

np.set_printoptions(threshold=np.inf)

# These three arrays hold the exact locations of different stats based on grouping.
statLocations=['0e','0f','10',
               '2e','2f','30',
               '4e','4f','50',
               '6e','6f','70',
               '8e','8f','90',
               'ae','af','b0',
               'ce','cf','d0',
               'ee','ef','f0',
               '10e','10f','110',
               '12e','12f','130',
               '14e','14f','150',
               '16e','16f','170',
               '18e','18f','190',
               '1ae','1af','1b0',
               '1ce','1cf','1d0',
               '1ee','1ef','1f0',]
hpStatLocations=['12','13','14','15',
                 '32','33','34','35',
                 '52','53','54','55',
                 '72','73','74','75',
                 '92','93','94','95',
                 'b2','b3','b4','b5',
                 'd2','d3','d4','d5',
                 'f2','f3','f4','f5',
                 '112','113','114','115',
                 '132','133','134','135',
                 '152','153','154','155',
                 '172','173','174','175',
                 '192','193','194','195',
                 '1b2','1b3','1b4','1b5',
                 '1d2','1d3','1d4','1d5',
                 '1f2','1f3','1f4','1f5',]
expStatLocations=['16','17',
                  '36','37',
                  '56','57',
                  '76','77',
                  '96','97',
                  'b6','b7',
                  'd6','d7',
                  'f6','f7',
                  '116','117',
                  '136','137',
                  '156','157',
                  '176','177',
                  '196','197',
                  '1b6','1b7',
                  '1d6','1d7',
                  '1f6','1f7',]

# The most basic max stat hack. iterates through the above arrays and assigns values accordingly to the save file.
def maxStatHack():
    rootMenu = tk.Tk() # makes a new window specifically for the max stat hack
    rootMenu.title("UltimaV-Trainer Max Stat Hack")
    canvasNew = tk.Canvas(rootMenu, height=0, width=400, bg="White")
    canvasNew.pack()
    maxHackLabel = tk.Label(rootMenu, text="Starting Max Hack")
    maxHackLabel.pack()

    tempstr = ''.join(G_hexFile) # joins the file together into a single string to prep for chunking
    tempSplicing = re.findall('..',tempstr) # utilizing Regex to chunk the file into 2 character strings to spearate it out like in a hex editor
    mainFileArr = np.array(tempSplicing) # converts the newly chunked list into a numpy array for easier data handling.

    for i in statLocations: # sets all values for Str, Dex, and Int to 99 for ALL characters
        temp = int(i, 16)
        mainFileArr[temp] = '63'
    for j in range(len(hpStatLocations)): # sets hp and max hp to 999 for ALL characters
        if(j%2==0):
            temp = int(hpStatLocations[j],16)
            mainFileArr[temp]='e7'
        if(j%2==1):
            temp = int(hpStatLocations[j], 16)
            mainFileArr[temp] = '03'
    for k in range(len(expStatLocations)): # sets exp to 9999 for ALL characters
        if(k%2==0):
            temp = int(expStatLocations[k], 16)
            mainFileArr[temp] = '0f'
        if (k%2==1):
            temp = int(expStatLocations[k], 16)
            mainFileArr[temp] = '27'

    # converts the hex value location to a decimal to be used as indexes to each item.
    keysInt = int('206',16)
    skullKeysInt = int('20b',16)
    gemsInt = int('207', 16)
    blackBadgeInt = int('218', 16)
    carpetInt = int('20a', 16)
    axesInt = int('240', 16)
    goldIntLeft = int('204',16)
    goldIntRingt = int('205',16)
    # sets the given amounts for each item based on the given assignment description
    mainFileArr[keysInt] = '64'
    mainFileArr[skullKeysInt] = '64'
    mainFileArr[gemsInt] = '64'
    mainFileArr[blackBadgeInt] = 'FF'
    mainFileArr[carpetInt] = '02'
    mainFileArr[axesInt] = '0A'
    mainFileArr[goldIntLeft] = '0f'
    mainFileArr[goldIntRingt] ='27'

    # joins the finished numpy list into a single string then converts the string of hex values into bytes.
    mainFileString = ''.join(mainFileArr)
    mainByte = bytes.fromhex(mainFileString) # hex to byte conversion
    # gives user dialog option to save the file anywhere they want.
    filename = tk.filedialog.asksaveasfile(initialfile='SAVED.GAM',mode='wb', defaultextension=".GAM", filetypes=[('Ultima Save File', 'SAVED.GAM')])
    if filename is None: # if the user does not choose a location, destroys the window and returns to the main menu.
        rootMenu.destroy()
        return
    saveLocation = filename.name
    with open(saveLocation,'wb') as w: # creates and writes the bytes to a file named 'SAVED.GAM' in the directory specified.
        w.write(mainByte)
    rootMenu.destroy() # destroys the window once the function is complete.
    pass

# opens a GUI window to allow changing of characters stats as well as items.
# IMPORTANT: This only allows for changes to the first three characters as well as all needed items as putting in the remaining
# 13 characters would have takes forever in the time that I had to work on this, I hope this is good enough as a proof of concept
def characterHack():
    customRoot = tk.Tk() # makes window, uses grid layout instead of pack layout
    customRoot.title("UltimaV-Trainer Custom Stats")
    customCanvas = tk.Canvas(customRoot, height=0, width=400, bg="White") # canvas for design
    canvas.pack()

    tempstr = ''.join(G_hexFile) # combines file into a single string to prep for chunking
    tempSplicing = re.findall('..', tempstr) # uses regex to chunk into byte sized pieces
    mainFileArr = np.array(tempSplicing) # converts list into numpy array for easy array operations
    phStr = ''

    #labels and textboxes for Eman, with current values inserted into textboxes for ease of use
    emanLabel = tk.Label(customRoot, text="Eman: ")
    emanStr = tk.Text(customRoot, height=1, width = 5)
    emanStr.insert(END,int(mainFileArr[int('0e', 16)],16)) # inserts the already existing stat into the textbox
    emanDex = tk.Text(customRoot, height=1, width=5)
    emanDex.insert(END, int(mainFileArr[int('0f', 16)],16))
    emanInt = tk.Text(customRoot, height=1, width=5)
    emanInt.insert(END, int(mainFileArr[int('10', 16)],16))
    emanHp = tk.Text(customRoot, height=1, width=5)
    phStr = mainFileArr[int('13',16)] + mainFileArr[int('12',16)]
    emanHp.insert(END, int(phStr, 16))
    phStr=''
    emanMaxHp = tk.Text(customRoot, height=1, width=5)
    phStr = mainFileArr[int('15', 16)] + mainFileArr[int('14', 16)]
    emanMaxHp.insert(END, int(phStr, 16))
    phStr=''
    emanExp = tk.Text(customRoot, height=1, width=5)
    phStr = mainFileArr[int('17', 16)] + mainFileArr[int('16', 16)]
    emanExp.insert(END, int(phStr, 16))
    phStr = ''

    # labels and textboxes for Shamino
    shaminoLabel = tk.Label(customRoot, text="Shamino: ")
    shaminoStr = tk.Text(customRoot, height=1, width=5)
    shaminoDex = tk.Text(customRoot, height=1, width=5)
    shaminoInt = tk.Text(customRoot, height=1, width=5)
    shaminoHp = tk.Text(customRoot, height=1, width=5)
    shaminoMaxHp = tk.Text(customRoot, height=1, width=5)
    shaminoExp = tk.Text(customRoot, height=1, width=5)
    shaminoStr.insert(END, int(mainFileArr[int('2e', 16)],16))
    shaminoDex.insert(END, int(mainFileArr[int('2f', 16)],16))
    shaminoInt.insert(END, int(mainFileArr[int('30', 16)],16))
    phStr = mainFileArr[int('33', 16)] + mainFileArr[int('32', 16)]
    shaminoHp.insert(END, int(phStr, 16))
    phStr = ''
    phStr = mainFileArr[int('35', 16)] + mainFileArr[int('34', 16)]
    shaminoMaxHp.insert(END, int(phStr, 16))
    phStr = ''
    phStr = mainFileArr[int('37', 16)] + mainFileArr[int('36', 16)]
    shaminoExp.insert(END, int(phStr, 16))
    phStr = ''

    # labels and textboxes for Iolo
    IoloLabel = tk.Label(customRoot, text="Iolo: ")
    IoloStr = tk.Text(customRoot, height=1, width=5)
    IoloDex = tk.Text(customRoot, height=1, width=5)
    IoloInt = tk.Text(customRoot, height=1, width=5)
    IoloHp = tk.Text(customRoot, height=1, width=5)
    IoloMaxHp = tk.Text(customRoot, height=1, width=5)
    IoloExp = tk.Text(customRoot, height=1, width=5)
    IoloStr.insert(END, int(mainFileArr[int('4e', 16)],16))
    IoloDex.insert(END, int(mainFileArr[int('4f', 16)],16))
    IoloInt.insert(END, int(mainFileArr[int('50', 16)],16))
    phStr = mainFileArr[int('53', 16)] + mainFileArr[int('52', 16)]
    IoloHp.insert(END, int(phStr, 16))
    phStr = ''
    phStr = mainFileArr[int('55', 16)] + mainFileArr[int('54', 16)]
    IoloMaxHp.insert(END, int(phStr, 16))
    phStr = ''
    phStr = mainFileArr[int('57', 16)] + mainFileArr[int('56', 16)]
    IoloExp.insert(END, int(phStr, 16))
    phStr = ''

    # textboxes for the items
    keysTx = tk.Text(customRoot, height=1, width=5)
    skullkeysTx = tk.Text(customRoot, height=1, width=5)
    gemsTx = tk.Text(customRoot, height=1, width=5)
    blackBadgeTx = tk.Text(customRoot, height=1, width=5)
    carpetTx = tk.Text(customRoot, height=1, width=5)
    axesTx = tk.Text(customRoot, height=1, width=5)
    keysTx.insert(END, int(mainFileArr[int('206',16)],16))
    skullkeysTx.insert(END, int(mainFileArr[int('20b', 16)],16))
    gemsTx.insert(END, int(mainFileArr[int('207', 16)],16))
    blackBadgeTx.insert(END, int(mainFileArr[int('218', 16)],16))
    carpetTx.insert(END, int(mainFileArr[int('20a', 16)],16))
    axesTx.insert(END, int(mainFileArr[int('240', 16)],16))


    # character stat legend to allow for easy navigation of stats
    tk.Label(customRoot,text=" Character ").grid(row=0,column=0)
    tk.Label(customRoot,text=" Str [0-99] ").grid(row=0,column=1)
    tk.Label(customRoot,text=" Dex [0-99] ").grid(row=0,column=2)
    tk.Label(customRoot,text=" Int [0-99] ").grid(row=0,column=3)
    tk.Label(customRoot,text=" Hp [0-999] ").grid(row=0,column=4)
    tk.Label(customRoot,text=" MaxHp [0-999] ").grid(row=0,column=5)
    tk.Label(customRoot,text=" Exp [0-9999] ").grid(row=0,column=6)
    # grid organization of Eman's objects into customRoot
    emanLabel.grid(row=1,column=0)
    emanStr.grid(row=1, column=1)
    emanDex.grid(row=1, column=2)
    emanInt.grid(row=1, column=3)
    emanHp.grid(row=1, column=4)
    emanMaxHp.grid(row=1, column=5)
    emanExp.grid(row=1, column=6)
    # grid organization for Shamino
    shaminoLabel.grid(row=2, column=0)
    shaminoStr.grid(row=2, column=1)
    shaminoDex.grid(row=2, column=2)
    shaminoInt.grid(row=2, column=3)
    shaminoHp.grid(row=2, column=4)
    shaminoMaxHp.grid(row=2, column=5)
    shaminoExp.grid(row=2, column=6)
    # grid organization for Iolo
    IoloLabel.grid(row=3, column=0)
    IoloStr.grid(row=3, column=1)
    IoloDex.grid(row=3, column=2)
    IoloInt.grid(row=3, column=3)
    IoloHp.grid(row=3, column=4)
    IoloMaxHp.grid(row=3, column=5)
    IoloExp.grid(row=3, column=6)
    # legend for items and textboxes for easy navigation in grid layout
    tk.Label(customRoot,text="Keys [0-99]").grid(row=0,column=7)
    tk.Label(customRoot,text="Skull Keys [0-99]").grid(row=0, column=8)
    tk.Label(customRoot,text="Gems [0-99]").grid(row=0, column=9)
    tk.Label(customRoot,text="Black Badge [00,255]").grid(row=0, column=10)
    tk.Label(customRoot,text="Magic Carpets [0-100]").grid(row=0, column=11)
    tk.Label(customRoot,text="Magic Axes [0-100]").grid(row=0, column=12)
    keysTx.grid(row=1, column=7)
    skullkeysTx.grid(row=1, column=8)
    gemsTx.grid(row=1, column=9)
    blackBadgeTx.grid(row=1, column=10)
    carpetTx.grid(row=1, column=11)
    axesTx.grid(row=1, column=12)

    # Inner function that this windows button calls and uses all existing objects in parent function.
    def setValues(): # ===== math for this is explained further in writeup ====
        # changes values in the numpy array to match to hex equivalent values of decimals in textboxes
        mainFileArr[int('0e',16)] = str(hex(int(emanStr.get(1.0,END)))[2:]).zfill(2)
        mainFileArr[int('0f', 16)] = str(hex(int(emanDex.get(1.0,END)))[2:]).zfill(2)
        mainFileArr[int('10', 16)] = str(hex(int(emanInt.get(1.0,END)))[2:]).zfill(2)
        valTemp = str(hex(int(emanHp.get(1.0,END)))[2:])
        mainFileArr[int('12', 16)] = valTemp[len(valTemp)//2:].zfill(2)
        mainFileArr[int('13', 16)] = valTemp[:len(valTemp)//2].zfill(2)
        valTemp = str(hex(int(emanMaxHp.get(1.0, END)))[2:])
        mainFileArr[int('14', 16)] = valTemp[len(valTemp) // 2:].zfill(2)
        mainFileArr[int('15', 16)] = valTemp[:len(valTemp) // 2].zfill(2)
        valTemp = str(hex(int(emanExp.get(1.0, END)))[2:])
        mainFileArr[int('16', 16)] = valTemp[len(valTemp) // 2:].zfill(2)
        mainFileArr[int('17', 16)] = valTemp[:len(valTemp) // 2].zfill(2)

        mainFileArr[int('2e', 16)] = str(hex(int(shaminoStr.get(1.0, END)))[2:]).zfill(2)
        mainFileArr[int('2f', 16)] = str(hex(int(shaminoDex.get(1.0, END)))[2:]).zfill(2)
        mainFileArr[int('30', 16)] = str(hex(int(shaminoInt.get(1.0, END)))[2:]).zfill(2)
        valTemp = str(hex(int(shaminoHp.get(1.0, END)))[2:])
        mainFileArr[int('32', 16)] = valTemp[len(valTemp) // 2:].zfill(2)
        mainFileArr[int('33', 16)] = valTemp[:len(valTemp) // 2].zfill(2)
        valTemp = str(hex(int(shaminoMaxHp.get(1.0, END)))[2:])
        mainFileArr[int('34', 16)] = valTemp[len(valTemp) // 2:].zfill(2)
        mainFileArr[int('35', 16)] = valTemp[:len(valTemp) // 2].zfill(2)
        valTemp = str(hex(int(shaminoExp.get(1.0, END)))[2:])
        mainFileArr[int('36', 16)] = valTemp[len(valTemp) // 2:].zfill(2)
        mainFileArr[int('37', 16)] = valTemp[:len(valTemp) // 2].zfill(2)

        mainFileArr[int('4e', 16)] = str(hex(int(IoloStr.get(1.0, END)))[2:]).zfill(2)
        mainFileArr[int('4f', 16)] = str(hex(int(IoloDex.get(1.0, END)))[2:]).zfill(2)
        mainFileArr[int('50', 16)] = str(hex(int(IoloInt.get(1.0, END)))[2:]).zfill(2)
        valTemp = str(hex(int(IoloHp.get(1.0, END)))[2:])
        mainFileArr[int('52', 16)] = valTemp[len(valTemp) // 2:].zfill(2)
        mainFileArr[int('53', 16)] = valTemp[:len(valTemp) // 2].zfill(2)
        valTemp = str(hex(int(IoloMaxHp.get(1.0, END)))[2:])
        mainFileArr[int('54', 16)] = valTemp[len(valTemp) // 2:].zfill(2)
        mainFileArr[int('55', 16)] = valTemp[:len(valTemp) // 2].zfill(2)
        valTemp = str(hex(int(IoloExp.get(1.0, END)))[2:])
        mainFileArr[int('56', 16)] = valTemp[len(valTemp) // 2:].zfill(2)
        mainFileArr[int('57', 16)] = valTemp[:len(valTemp) // 2].zfill(2)

        mainFileArr[int('206', 16)] = str(hex(int(keysTx.get(1.0, END)))[2:]).zfill(2)
        mainFileArr[int('20b', 16)] = str(hex(int(skullkeysTx.get(1.0, END)))[2:]).zfill(2)
        mainFileArr[int('207', 16)] = str(hex(int(gemsTx.get(1.0, END)))[2:]).zfill(2)
        mainFileArr[int('218', 16)] = str(hex(int(blackBadgeTx.get(1.0, END)))[2:]).zfill(2)
        mainFileArr[int('20a', 16)] = str(hex(int(carpetTx.get(1.0, END)))[2:]).zfill(2)
        mainFileArr[int('240', 16)] = str(hex(int(axesTx.get(1.0, END)))[2:]).zfill(2)

        # joins together the fully adjusted numpy array into a single string, then converts to bytes
        mainFileString = ''.join(mainFileArr)
        mainByte = bytes.fromhex(mainFileString) # converts string into bytes
        # opens a user dialog to save file to any directory of choice
        filename = tk.filedialog.asksaveasfile(initialfile='SAVED.GAM', mode='wb', defaultextension=".GAM",
                                               filetypes=[('Ultima Save File', 'SAVED.GAM')])
        if filename is None: # save cancel check
            customRoot.destroy()
            return
        saveLocation = filename.name
        with open(saveLocation, 'wb') as w: # creates and writes a new/replaced 'SAVED.GAM' file with bytes to the specified directory.
            w.write(mainByte)
        customRoot.destroy()
        return
        pass
    # button that allows users to save their changes to the save file.
    tk.Button(customRoot,text="setValues", padx=10,pady=5, fg="Black",bg="Grey", command=setValues).grid(row=5,column=6)

    pass

# this function is called by the openFileBtn button, and it allows the user to locate and select the 'SAVED.GAM' file.
def fileSelect():
    # opens a user dialog to allow them to locate the save file for the game, also features filtering of filetypes
    filename = filedialog.askopenfilename(initialdir="/", title="selectFile", filetypes=(("Ultima Save Files","SAVED.GAM"),("All Files","*.*")))
    global G_filename # global string used to hold the files directory
    G_filename=filename
    if G_filename.find("SAVED.GAM") == -1: # this is a check to ensure that the user selects only the 'SAVED.GAM' file
        print("OI, SAVE FILES ONLY")
        G_filename = ''
        return
    with open(G_filename, 'rb') as f: # reads in the 'SAVED.GAM' file to G_filename
        hexFile = f.read().hex() # reads in the file as hex.
    global G_hexFile # global variable to hold the newly made hexfile contents.
    G_hexFile = hexFile
    startHackingBtn.pack() # shows a new button for beginning the hack
    pass


# Accesses the main menu of the program.
def accessMenu():
    # destroys all existing objects in root window as they have served their purpose
    startHackingBtn.destroy()
    openFileBtn.destroy()
    # new canvas as well as buttons for choosing between a full stat hack or a custom stat hack.
    canvasMenu = tk.Canvas(root, height=5, width=400, bg="Black")
    canvasMenu.pack()
    fullHackBtn=tk.Button(root, text="Full Hack", padx=10,pady=5, fg="Red",bg="Black",command=maxStatHack) # full hack button
    customHackBtn=tk.Button(root, text="Manual Hack", padx=10,pady=5, fg="Red",bg="Black",command=characterHack) # custom hack button
    # labels and pack() for all objects
    fullHackLabel = tk.Label(root, text="Click for Full stat/item hack")
    customHackLabel = tk.Label(root, text="Click for manual hacking")
    fullHackLabel.pack()
    fullHackBtn.pack()
    customHackLabel.pack()
    customHackBtn.pack()
    pass


root = tk.Tk() # the main window of the application. Holds buttons that can open other windows.
root.title('UltimaV_Trainer - Aryan Sanyal') # window title
tk.Label(text="Game trainer made by Aryan Sanyal for CECS378").pack()
canvas = tk.Canvas(root, height=0, width=400, bg="White")
canvas.pack()
# buttons for initial functionality.
# This button calls the fileSelect() function to allow for selection of the save file and also to make the startHackingBtn visible
openFileBtn = tk.Button(root, text="Open Save File", padx=10,pady =5, fg="White", bg="Blue", command=fileSelect)
openFileBtn.pack()
# This button calls the accessMenu() function to allow for the main cuntionality of the program.
startHackingBtn = tk.Button(root, text="Start Hack", padx=10,pady=5, fg="Red",bg="Black", command=accessMenu)

root.mainloop() # main for starting the program.