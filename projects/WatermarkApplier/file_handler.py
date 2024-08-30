from tkinter import filedialog


class FileHandler:

    def __init__(self):
        self._image_path = ""
        self._watermark_path = ""

    @property
    def image_path(self):
        return self._image_path

    @property
    def watermark_path(self):
        return self._watermark_path

    def select_image(self) -> str:
        self._image_path = filedialog.askopenfilename();

    def select_watermark(self) -> str:
        self._watermark_path = filedialog.askopenfilename();
