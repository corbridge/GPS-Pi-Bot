from tkinter import *
import tkintermapview

root = Tk()
root.title("GPS BOT GUI")
# root.iconbitmap()
root.geometry("700x550")

label = LabelFrame(root)
label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(label, width=500, height=500, corner_radius=0)
fime = [25.725260848439078, -100.31355131896652]
map_widget.set_position(fime[0], fime[1])
map_widget.set_zoom(20)

map_widget.pack()
root.mainloop()