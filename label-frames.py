import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import json

class ImageLabeler:
    def __init__(self, root, image_dir):
        self.root = root
        self.image_dir = image_dir
        self.image_files = [f for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
        self.current_image = None
        self.current_index = 0
        self.labels = {}
        self.load_state()

        self.canvas = tk.Canvas(root, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.on_click)

        self.status_label = tk.Label(root, text="", anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

        self.next_button = tk.Button(root, text="No Object", command=self.skip_image)
        self.next_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.update_status()
        self.display_image()

    def update_status(self):
        status_text = f"Image {self.current_index + 1} of {len(self.image_files)}"
        self.status_label.config(text=status_text)

    def load_state(self):
        try:
            with open('labels.json', 'r') as file:
                self.labels = json.load(file)

            for i, img in enumerate(self.image_files):
                if img not in self.labels:
                    self.current_index = i
                    break
            else:
                self.current_index = len(self.image_files)
        except FileNotFoundError:
            self.current_index = 0

    def save_state(self):
        with open('labels.json', 'w') as file:
            json.dump(self.labels, file)

    def display_image(self):
        if self.current_index < len(self.image_files):
            img_path = os.path.join(self.image_dir, self.image_files[self.current_index])
            self.current_image = Image.open(img_path)
            self.photo = ImageTk.PhotoImage(self.current_image)
            self.canvas.config(width=self.current_image.width, height=self.current_image.height)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.update_status()
        else:
            messagebox.showinfo("Complete", "All images have been labeled")
            self.root.destroy()

    def on_click(self, event):
        # self.labels[self.image_files[self.current_index]] = {'x': event.x, 'y': event.y}
        linear_index = event.y * self.current_image.width + event.x
        self.labels[self.image_files[self.current_index]] = linear_index
        self.save_state()
        self.next_image()

    def skip_image(self):
        # self.labels[self.image_files[self.current_index]] = {'x': None, 'y': None}
        self.labels[self.image_files[self.current_index]] = None  # No object
        self.save_state()
        self.next_image()

    def next_image(self):
        self.current_index += 1
        self.display_image()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Labeler")

    image_dir = filedialog.askdirectory(title="Select image directory")
    if image_dir:
        app = ImageLabeler(root, image_dir)
        root.mainloop()
    else:
        root.destroy()
