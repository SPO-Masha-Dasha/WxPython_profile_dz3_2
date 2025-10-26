import wx

class ProfileFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Профиль Джедая - Оби-Ван Кеноби",
                         size=(320, 620),
                         style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        self.panel = wx.Panel(self)
        self.background = None
        self.avatar = None
        self.create_interface()
        self.Centre()

    def create_round_image(self, image_path, size=120):
        try:
            image = wx.Image(image_path, wx.BITMAP_TYPE_ANY)
            image = image.Scale(size, size, wx.IMAGE_QUALITY_HIGH)
            return wx.Bitmap(image)
        except Exception as e:
            print(f"Ошибка загрузки аватара: {e}")
            return wx.Bitmap(size, size)

    def create_interface(self):
        try:
            background_image = wx.Image("", wx.BITMAP_TYPE_ANY)
            background_image = background_image.Scale(320, 200, wx.IMAGE_QUALITY_HIGH)
            background_bmp = wx.Bitmap(background_image)
            self.background = wx.StaticBitmap(self.panel, -1, background_bmp, pos=(0, 0))
        except Exception as e:
            print(f"Ошибка загрузки фона: {e}")
            bg_panel = wx.Panel(self.panel, pos=(0, 0), size=(320, 200))
            bg_panel.SetBackgroundColour(wx.Colour(135, 206, 235))

        try:
            avatar_bitmap = self.create_round_image("", 120)
            self.avatar = wx.StaticBitmap(self.panel, -1, avatar_bitmap, pos=(90, 40))
        except Exception as e:
            print(f"Ошибка загрузки аватара: {e}")

        name_label = wx.StaticText(self.panel, -1, "Оби-Ван Кеноби", pos=(60, 210))
        name_font = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        name_label.SetFont(name_font)

        bio_title = wx.StaticText(self.panel, -1, "Биография", pos=(25, 250))
        title_font = wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        bio_title.SetFont(title_font)

        bio_text = wx.StaticText(self.panel, -1,
                                 "Мастер-Джедай, наставник Энакина и Люка Скайуокеров. Хранитель мира в галактике.",
                                 pos=(25, 275), size=(270, -1))
        bio_text.Wrap(270)
        text_font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        bio_text.SetFont(text_font)

        skills_title = wx.StaticText(self.panel, -1, "Способности", pos=(25, 330))
        skills_title.SetFont(title_font)

        skills_text = wx.StaticText(self.panel, -1,
                                    "Сила Джедаев | Форма III | Философия | Наставничество",
                                    pos=(25, 355), size=(270, -1))
        skills_text.Wrap(270)
        skills_text.SetFont(text_font)

        exp_title = wx.StaticText(self.panel, -1, "Опыт", pos=(25, 420))
        exp_title.SetFont(title_font)

        exp1 = wx.StaticText(self.panel, -1, "Мастер-Джедай Совета", pos=(25, 445))
        exp1.SetFont(text_font)

        exp1_date = wx.StaticText(self.panel, -1, "32 ДБЯ - 19 ДБЯ", pos=(25, 465))
        date_font = wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        exp1_date.SetFont(date_font)
        exp1_date.SetForegroundColour(wx.Colour(128, 128, 128))

        exp2 = wx.StaticText(self.panel, -1, "Падаван Квай-Гона Джинна", pos=(25, 490))
        exp2.SetFont(text_font)

        exp2_date = wx.StaticText(self.panel, -1, "44 ДБЯ - 32 ДБЯ", pos=(25, 510))
        exp2_date.SetFont(date_font)
        exp2_date.SetForegroundColour(wx.Colour(128, 128, 128))


class ProfileApp(wx.App):
    def OnInit(self):
        frame = ProfileFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = ProfileApp()
    app.MainLoop()