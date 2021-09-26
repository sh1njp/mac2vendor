import csv
from tkinter import *
from tkinter import ttk
from tkinter.font import Font

with open('oui.csv' ,encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    dict_from_csv = {row[1]:row[2] for row in reader}

def mac2vendor():
	list_mac=txt.get("1.0", "end-1c").split("\n")
	print("------ koko kara ------------------")
	for mac in list_mac:
		search_mac = mac.upper().replace(':', '').replace('-', '').replace('.', '')[0:6]
		print(mac.strip("\n") ,dict_from_csv.get(search_mac))
	print("------ koko made ------------------")

root = Tk()
root.title('Mac2Vendor')
root.minsize(100, 100)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Frame
frame1 = ttk.Frame(root, padding=10)
frame1.rowconfigure(1, weight=1)
frame1.columnconfigure(0, weight=1)
frame1.grid(sticky=(N, W, S, E))

# Button
button1 = ttk.Button(
    frame1, text='OK',
    command=mac2vendor)
button1.grid(
    row=0, column=0, columnspan=2, sticky=(N, E))

# Text
f = Font(family='MS Gothic', size=16)
v1 = StringVar()
txt = Text(frame1, height=15, width=20)
txt.configure(font=f)
txt.insert(1.0, "38-AF-D7-00-00-00\n38-AF-D7-FF-FF-FF")
txt.grid(row=1, column=0, sticky=(N, W, S, E))

# Scrollbar
scrollbar = ttk.Scrollbar(
    frame1,
    orient=VERTICAL,
    command=txt.yview)
txt['yscrollcommand'] = scrollbar.set
scrollbar.grid(row=1, column=1, sticky=(N, S))

root.mainloop()