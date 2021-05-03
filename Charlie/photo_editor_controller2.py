class PhotoController()

   def selected(self):
        global img_path, img
        img_path = filedialog.askopenfilename(initialdir=os.getcwd())
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        #imgg = img.filter(ImageFilter.BoxBlur(0))
        img1 = ImageTk.PhotoImage(img)
        canvas2.create_image(300, 210, image=img1)
        canvas2.image = img1

    def blur(self, event):
        global img_path, img1, imgg
        for m in range(0, v1.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = img.filter(ImageFilter.BoxBlur(m))
            img1 = ImageTk.PhotoImage(imgg)
            canvas2.create_image(300, 210, image=img1)
            canvas2.image = img1
    def brightness(self, event):
        global img_path, img2, img3
        for m in range(0, v2.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Brightness(img)
            img2 = imgg.enhance(m)
            img3 = ImageTk.PhotoImage(img2)
            canvas2.create_image(300, 210, image=img3)
            canvas2.image = img3

    def contrast(event):
        global img_path, img4, img5
        for m in range(0, v3.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Contrast(img)
            img4 = imgg.enhance(m)
            img5 = ImageTk.PhotoImage(img4)
            canvas2.create_image(300, 210, image=img5)
            canvas2.image = img5

    def rotate_image(self, event):
        global img_path, img6, img7
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img6 = img.rotate(int(rotate_combo.get()))
        img7 = ImageTk.PhotoImage(img6)
        canvas2.create_image(300, 210, image=img7)
        canvas2.image = img7

    def flip_image(self, event):
        global img_path, img8, img9
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        if flip_combo.get() == "FLIP LEFT TO RIGHT":
            img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif flip_combo.get() == "FLIP TOP TO BOTTOM":
            img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
        img9 = ImageTk.PhotoImage(img8)
        canvas2.create_image(300, 210, image=img9)
        canvas2.image = img9   

    def image_border(self, event):
        global img_path, img10, img11
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img10 = ImageOps.expand(img, border=int(border_combo.get()), fill=95)
        img11 = ImageTk.PhotoImage(img10)
        canvas2.create_image(300, 210, image=img11)
        canvas2.image = img11

    def save(self):
        global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
        # file=None
        ext = img_path.split(".")[-1]
        file = asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
        if file:
            if canvas2.image ==img1:
                imgg.save(file)
            elif canvas2.image ==img3:
                img2.save(file)
            elif canvas2.image ==img5:
                img4.save(file)
            elif canvas2.image ==img7:
                img6.save(file)
            elif canvas2.image ==img9:
                img8.save(file)
            elif canvas2.image ==img11:
                img10.save(file)
