from tkinter import *
import tkintermapview

def add_marker_event(coords):
    new_marker = map_widget.set_marker(coords[0], coords[1], text="position")

root = Tk()
root.title("GPS BOT GUI")
# root.iconbitmap()
root.geometry("700x550")

label = LabelFrame(root)
label.pack(pady=20)

fime = [25.7252, -100.3135]
fime_2 = [25.7258, -100.3138]

map_widget = tkintermapview.TkinterMapView(label, width=500, height=500, corner_radius=0)
map_widget.set_position(fime[0], fime[1])
map_widget.set_zoom(20)


# first_position = map_widget.set_marker(fime[0], fime[1], text="First position")
# second_position = map_widget.set_marker(fime_2[0], fime_2[1], text="Second position")

map_widget.add_right_click_menu_command(label="Add first position",
                                        command=add_marker_event,
                                        pass_coords=True)

map_widget.add_right_click_menu_command(label="Add second position",
                                        command=add_marker_event,
                                        pass_coords=True)

# polygon_1 = map_widget.set_polygon([(fime[0], fime[1]),
#                                     (fime_2[0], fime_2[1])],
#                                    # fill_color=None,
#                                    # outline_color="red",
#                                    # border_width=12,
#                                    name="path")

map_widget.pack()
root.mainloop()