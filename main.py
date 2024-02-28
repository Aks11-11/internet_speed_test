from tkinter import *
import speedtest

def speedcheck():
    ak = speedtest.Speedtest()
    ak.get_servers()
    down = str(round(ak.download()/(10**6),3))+"Mbps"
    up = str(round(ak.upload()/(10 ** 6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text = up)
ak = Tk()
ak.title("Ak's Internet's Speed")
ak.geometry("500x500")
ak.config(bg ="Blue")


lab = Label(ak, text = "Internet's Speed",font = ("Times new roman",60,"bold"),bg = "blue", fg ="White")
lab.place(x= 35, y =40)

lab = Label(ak, text = "Download Speed",font = ("Times new roman",30,"bold"),bg = "black", fg ="White")
lab.place(x= 50, y =150, height = 30, width = 380)

lab_down = Label(ak, text = "00",font = ("Times new roman",20,"bold"),bg = "black", fg ="White")
lab_down.place(x= 50, y =190,height = 30,width = 380)

lab = Label(ak, text = "Upload Speed",font = ("Times new roman",30,"bold"),bg = "Sky Blue", fg ="White")
lab.place(x= 50, y =230,height = 30,width = 380)

lab_up = Label(ak, text = "00",font = ("Times new roman",20,"bold"),bg = "Sky blue", fg ="White")
lab_up.place(x= 50, y =270,height = 30,width = 380)

button = Button(ak,text="Check Speed",font = ("Times new roman",20,"bold"),relief= RAISED,command=speedcheck)
button.place(x= 50, y =400,height = 30,width = 380)

ak.mainloop()