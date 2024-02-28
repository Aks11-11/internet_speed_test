from tkinter import *
import speedtest
import st


def speedcheck():
    st = speedtest.Speedtest()
    st.get_servers()
    down = str(round(st.download()))  # /(10**6),3))+"Mbps"
    up = str(round(st.upload()))  # /(10**6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title("Ak's Internet's Speed")
sp.geometry("500x500")
sp.config(bg="Blue")

lab = Label(sp, text="Internet's Speed", font=("Times new roman", 60, "bold"), bg="blue", fg="White")
lab.place(x=35, y=40)

download_label = Label(sp, text="Download Speed", font=("Times new roman", 30, "bold"), bg="black", fg="White")
download_label.place(x=50, y=150, height=30, width=380)

lab_down = Label(sp, text="00", font=("Times new roman", 20, "bold"), bg="black", fg="White")
lab_down.place(x=50, y=190, height=30, width=380)

upload_label = Label(sp, text="Upload Speed", font=("Times new roman", 30, "bold"), bg="Sky Blue", fg="White")
upload_label.place(x=50, y=230, height=30, width=380)

lab_up = Label(sp, text="00", font=("Times new roman", 20, "bold"), bg="Sky blue", fg="White")
lab_up.place(x=50, y=270, height=30, width=380)

button = Button(sp, text="Check Speed", font=("Times new roman", 20, "bold"), relief=RAISED, command=speedcheck)
button.place(x=50, y=400, height=30, width=380)

sp.mainloop()

if __name__ == '__speedtest__':
    speedcheck()
