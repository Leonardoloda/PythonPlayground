from tkinter import Tk, Button, Canvas

from PIL import Image, ImageTk

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from file_handler import FileHandler


class UI:
    def __init__(self):
        self._window = Tk()
        self._image_input = Button(text="Select")
        self._watermark_input = Button(text="Watermark")
        self._merge_input = Button(text="Merge")

        self._image_canvas = Canvas(width=500, height=500)
        self._image_render = self._image_canvas.create_image(200, 200)
        self._image = None
        self._pil_image = None

        self._watermark_canvas = Canvas(width=500, height=500)
        self._watermark_render = self._watermark_canvas.create_image(200, 200)
        self._watermark = None
        self._pil_watermark = None

        self._file_handler = FileHandler()

        self.config()

    def config(self):
        self._window.title("Watermark Applier")

        self._window.minsize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self._window.config(padx=10, pady=10)

        self._image_input.config(command=self.select_image)
        self._watermark_input.config(command=self.select_watermark)
        self._merge_input.config(command=self.merge)

    def select_image(self):
        self._file_handler.select_image()

        self._pil_image = Image.open(self._file_handler.image_path)
        self._image = ImageTk.PhotoImage(self._pil_image)

        self._image_canvas.itemconfig(self._image_render, image=self._image)

    def select_watermark(self):
        self._file_handler.select_watermark()

        self._pil_watermark = Image.open(self._file_handler.watermark_path)
        self._watermark = ImageTk.PhotoImage(self._pil_watermark)

        self._watermark_canvas.itemconfig(self._watermark_render, image=self._watermark)

    def start(self):
        self._image_input.grid(row=0, column=0)
        self._watermark_input.grid(row=0, column=2)

        self._image_canvas.grid(row=1, column=0)
        self._watermark_canvas.grid(row=1, column=2)

        self._merge_input.grid(row=2, column=1)

        self._window.mainloop()

    def merge(self):
        background = self._pil_image;
        foreground = self._pil_watermark;

        background.paste(foreground, (0, 0), foreground)
        background.show()
