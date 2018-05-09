
import Tkinter as tk
root = tk.Tk()

root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d' % (width, height))


image_file = "welcome.gif"


image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height, width=width, bg="black")
canvas.create_image(width*0.5, height*0.95, image=image)
canvas.pack()


root.after(3000, root.destroy)
root.mainloop()




