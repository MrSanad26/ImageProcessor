import cv2
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk


class ImageProcessor:
    def __init__(self, master):
        self.master = master
        master.title("Image Processor")
        master.geometry("800x600")
        master.configure(bg="#7187c2")

        # Set background style
        master.configure(bg="#585858")
        self.logo_frame = tk.Frame(master, bg="#585858")
        self.logo_frame.pack(fill=tk.X)

        # set up company logo header
        self.logo = Image.open("C:/CV/logo.png")
        self.logo = self.logo.resize((400, 100))
        self.logo_image = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(master, image=self.logo_image, bg="#585858")
        self.logo_label.pack(padx=10, pady=10)
        self.image = None
        self.modified_image = None
        self.angle = 0
        self.blur = 0
        self.canny = 0
        self.width = None
        self.height = None

        # create widgets
        self.canvas = tk.Canvas(master, bg="#baa7ce")
        self.canvas.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.add_image_button = tk.Button(self.canvas, text="Add Image", command=self.add_image, bg="#d53a95",
                                          fg="#FFFFFF", font=("TkDefaultFont", 16, "bold"))
        self.add_image_button.pack(pady=10)

        self.filter_frame = tk.LabelFrame(master, text="Filters", padx=20, pady=20, font=("TkDefaultFont", 12, "bold",),
                                          bg="#585858", fg="#FFFFFF")
        self.filter_frame.pack(pady=10)

        self.save_frame = tk.LabelFrame(master, text="Filters", padx=20, pady=25, bg="#F5F5F5", font=("Arial", 12))
        self.save_frame.pack(pady=5)

        self.height_label = tk.Label(self.filter_frame, text="Height:", font=("TkDefaultFont", 12, "bold",),
                                     bg="#585858", fg="#FFFFFF")
        self.height_label.grid(row=0, column=0, padx=10, pady=10)
        self.height_entry = tk.Entry(self.filter_frame, font=("Arial", 12), width=10, justify=tk.CENTER, bg="#585858",
                                     fg="#FFFFFF")
        self.height_entry.grid(row=0, column=1, padx=10, pady=10)

        self.width_label = tk.Label(self.filter_frame, text="Width:", font=("TkDefaultFont", 12, "bold",), bg="#585858",
                                    fg="#FFFFFF")
        self.width_label.grid(row=1, column=0, padx=10, pady=10)
        self.width_entry = tk.Entry(self.filter_frame, font=("Arial", 12), width=10, justify=tk.CENTER, bg="#585858",
                                    fg="#FFFFFF")
        self.width_entry.grid(row=1, column=1, padx=10, pady=10)

        self.change_size_button = tk.Button(self.filter_frame, text="Change Size", command=self.change_size,
                                            bg="#d53a95", fg="#FFFFFF", font=("TkDefaultFont", 12, "bold"), width=12)
        self.change_size_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.angle_label = tk.Label(self.filter_frame, text="Angle: 0", font=("TkDefaultFont", 12, "bold",),
                                    bg="#585858", fg="#FFFFFF")
        self.angle_label.grid(row=3, column=0, padx=10, pady=10)
        self.angle_slider = tk.Scale(self.filter_frame, from_=0, to=180, orient=tk.HORIZONTAL,
                                     command=self.change_angle, bg="#585858", fg="#FFFFFF")
        self.angle_slider.grid(row=3, column=1, padx=10, pady=10)

        self.blur_label = tk.Label(self.filter_frame, text="Blur: 0", font=("TkDefaultFont", 12, "bold",), bg="#585858",
                                   fg="#FFFFFF")
        self.blur_label.grid(row=4, column=0, padx=10, pady=10)
        self.blur_slider = tk.Scale(self.filter_frame, from_=0, to=10, orient=tk.HORIZONTAL, command=self.change_blur,
                                    bg="#585858", fg="#FFFFFF")
        self.blur_slider.grid(row=4, column=1, padx=10, pady=10)

        self.canny_label = tk.Label(self.filter_frame, text="Contour Detection: 0", font=("TkDefaultFont", 12, "bold",),
                                    bg="#585858", fg="#FFFFFF")
        self.canny_label.grid(row=5, column=0, padx=10, pady=10)
        self.canny_slider = tk.Scale(self.filter_frame, from_=0, to=255, orient=tk.HORIZONTAL,
                                     command=self.change_canny, bg="#585858", fg="#FFFFFF")
        self.canny_slider.grid(row=5, column=1, padx=10, pady=10)

        self.grayscale_button = tk.Button(self.filter_frame, text="Grayscale", command=self.grayscale, bg="#d53a95",
                                          fg="#FFFFFF", font=("TkDefaultFont", 12, "bold"), width=12)
        self.grayscale_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.reset_button = tk.Button(master, command=self.reset, bg="#d53a95")
        self.reset_image = Image.open("C:/CV/icons8-reset-50.png")
        self.reset_image = self.reset_image.resize((50, 50))
        self.reset_image = ImageTk.PhotoImage(self.reset_image)
        self.reset_button.config(image=self.reset_image, width="50", height="50")
        self.reset_button.place(relx=0.95, rely=0.8, anchor="center")

        self.save_button = tk.Button(master, command=self.save, bg="#d53a95")
        self.save_image = Image.open("C:/CV/icons8-save-button-50.png")
        self.save_image = self.save_image.resize((50, 50))
        self.save_image = ImageTk.PhotoImage(self.save_image)
        self.save_button.config(image=self.save_image, width="50", height="50")
        self.save_button.place(relx=0.9, rely=0.8, anchor="center")

        self.show_result_button = tk.Button(master, command=self.show_result, bg="#d53a95")
        self.show_result_image = Image.open("C:/CV/icons8-show-property-50.png")
        self.show_result_image = self.show_result_image.resize((50, 50))
        self.show_result_image = ImageTk.PhotoImage(self.show_result_image)
        self.show_result_button.config(image=self.show_result_image, width="50", height="50")
        self.show_result_button.place(relx=0.85, rely=0.8, anchor="center")

    def add_image(self):
        path = filedialog.askopenfilename()
        if path:
            self.image = cv2.imread(path)
            self.modified_image = self.image.copy()
            self.width, self.height = self.image.shape[1], self.image.shape[0]
            self.show_image()

    def show_image(self):
        if self.image is not None:
            image = cv2.cvtColor(self.modified_image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
            self.canvas.image = photo

    def change_size(self):
        try:
            new_height = self.height_entry.get()
            new_width = self.width_entry.get()
            if new_height == "":
                new_height = self.height
            else:
                new_height = int(new_height)
            if new_width == "":
                new_width = self.width
            else:
                new_width = int(new_width)
            if new_height <= 0 or new_width <= 0:
                messagebox.showerror("Error", "Invalid input please enter numbers only or leave it blank")
            else:
                self.modified_image = cv2.resize(self.modified_image, (new_width, new_height))
                self.width, self.height = new_width, new_height
                self.show_image()
        except ValueError:
            messagebox.showerror("Error", "Invalid input please enter numbers only or leave it blank")

    def change_angle(self, angle):
        self.angle = int(angle)
        self.angle_label.config(text=f"Angle: {self.angle}")
        if self.modified_image is not None:
            self.rotate()

    def rotate(self):
        center = (self.width // 2, self.height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, self.angle, 1.0)
        self.modified_image = cv2.warpAffine(self.modified_image, rotation_matrix, (self.width, self.height))
        self.show_image()

    def grayscale(self):
        self.modified_image = cv2.cvtColor(self.modified_image, cv2.COLOR_BGR2GRAY)
        self.show_image()

    def change_blur(self, blur):
        self.blur = int(blur)
        self.blur_label.config(text=f"Blur: {self.blur}")
        if self.modified_image is not None:
            self.blur_image()

    def blur_image(self):
        self.modified_image = cv2.GaussianBlur(self.modified_image, (self.blur * 2 + 1, self.blur * 2 + 1), 0)
        self.show_image()

    def change_canny(self, canny):
        self.canny = int(canny)
        self.canny_label.config(text=f"Canny: {self.canny}")
        if self.modified_image is not None:
            self.canny_image()

    def canny_image(self):
        self.modified_image = cv2.Canny(self.modified_image, self.canny, self.canny * 2)
        self.show_image()

    def reset(self):
        self.modified_image = self.image.copy() if self.image is not None else None
        self.angle = 0
        self.blur = 0
        self.canny = 0
        self.width, self.height = self.image.shape[1], self.image.shape[0] if self.image is not None else None
        self.width_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.angle_slider.set(0)
        self.blur_slider.set(0)
        self.canny_slider.set(0)
        self.show_image()

    def save(self):
        if self.modified_image is not None:
            path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
            if path:
                cv2.imwrite(path, self.modified_image)
                messagebox.showinfo("Success", "Image saved successfully.")

    def show_result(self):
        if self.modified_image is not None:
            cv2.imshow("Result", self.modified_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


root = tk.Tk()
app = ImageProcessor(root)
root.mainloop()
