import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess

class AnalogQT:
    def __init__(self, master):
        self.master = master
        master.title("analogQT")
        
        self.label = tk.Label(master, text="Преобразование изображения в аналоговое")
        self.label.pack()

        self.import_button = tk.Button(master, text="Импортировать изображение", command=self.import_image)
        self.import_button.pack()

        self.modemodulate_button = tk.Button(master, text="Modemodulate!", command=self.modemodulate)
        self.modemodulate_button.pack()

        self.image_path = None

    def import_image(self):
        self.image_path = filedialog.askopenfilename(title="Выберите изображение", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if self.image_path:
            messagebox.showinfo("Импорт", f"Изображение загружено: {os.path.basename(self.image_path)}")

    def modemodulate(self):
        if not self.image_path:
            messagebox.showwarning("Ошибка", "Сначала импортируйте изображение!")
            return
        
        # Создание имени выходного файла
        base_name, ext = os.path.splitext(self.image_path)
        output_path = f"{base_name}_modemodulated{ext}"

        try:
            # Предполагается, что colormodem.py и cli.py находятся в одной директории
            subprocess.run(['python', 'cli.py', self.image_path, output_path], check=True)
            messagebox.showinfo("Успех", f"Изображение успешно преобразовано и сохранено как {output_path}!")
        except subprocess.CalledProcessError:
            messagebox.showerror("Ошибка", "Не удалось преобразовать изображение.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnalogQT(root)
    root.mainloop()
