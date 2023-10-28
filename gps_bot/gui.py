from tkinter import *
import tkintermapview


class GPSGui:
    def __init__(self):
        root = Tk()
        root.title("GPS BOT GUI")
        # root.iconbitmap()
        root.geometry("700x550")

        label = LabelFrame(root)
        label.pack(pady=20)

        fime = [25.7252, -100.3135]
        fime_2 = [25.7258, -100.3138]

        self.map_widget = tkintermapview.TkinterMapView(label, width=500, height=500, corner_radius=0)
        self.map_widget.set_position(fime[0], fime[1])
        self.map_widget.set_zoom(20)

        self.map_widget.add_right_click_menu_command(label="Add first position",
                                                command=self.add_marker_event,
                                                pass_coords=True)

        self.map_widget.add_right_click_menu_command(label="Add second position",
                                                command=self.add_marker_event,
                                                pass_coords=True)

        self.map_widget.pack()
        root.mainloop()
    
    def add_marker_event(self,coords):
        new_marker = self.map_widget.set_marker(coords[0], coords[1], text="position")
