from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from PIL import ImageFont
from PIL import ImageDraw
from kivy.uix.floatlayout import FloatLayout
from PIL import Image  # Required Imports

from android.permissions import request_permissions, Permission
request_permissions([Permission.WRITE_EXTERNAL_STORAGE,
                     Permission.READ_EXTERNAL_STORAGE])
from android.storage import primary_internal_storage_path
SD_CARD = primary_external_storage_path()


from os.path import dirname, join



import os

filenames = ''  # Initializing Variables for later use
filenamess = ''
filename = ""
image_copy = ""
image_count = 0
Backround_Name = ""
image = ""
image1 = False
image2 = False
image3 = False
image4 = False
image5 = False
image6 = False
d = os.path.split(os.getcwd())
d = os.path.join(d[0],d[1])
e = "Backrounds"
f = os.path.join(str(d),str(e))
print(f)
#dcim =join(dirname(user_data_dir), 'DCIM')
#print(dcim)
"""
s = os.path.abspath("Bst.png")
filenames_for_backround = ["Bst.png", "—Pngtree—happy birthday background shading_2256915.png","circle2.png","âPngtreeâvalentines day transparent heart frame_5738228.png"]
asb_paths = []
for filename in filenames_for_backround:
    g = os.path.abspath(filename)
    asb_paths.append(g)
print(asb_paths)
"""
"""
config = {

    "apiKey": "AIzaSyC16MQdD1ksSId7ufgfNkQMzq-E36Vq-Tw",
    "authDomain": "pythonprojectbirthday.firebaseapp.com",
    "databaseURL": "https://pythonprojectbirthday.firebaseio.com",
    "projectId": "pythonprojectbirthday",
    "storageBucket": "pythonprojectbirthday.appspot.com",
    "messagingSenderId": "296870160547",
    "appId": "1:296870160547:web:5cc2722407151befeaf716",
    "measurementId": "G-KLVY122D0Z"
}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud = "Bst.png"
path_on_sytem = "furbase.png"
r = requests.get((storage.child(path_on_cloud).get_url(path_on_cloud)))
filename = str(r).split("/")[-1]
with open(filename, 'wb') as f:
    f.write(r.content)
    print("done")
"""
class Final_Screen(Screen):  # Final Screen
    def clearing(self):
        self.ids.textinputbox.text = ""
    def helos(self):  # Picture aspect ratio adjustment called by start button in Final_Screen and Final_Widget
        b1 = f + "/Backround_for_frame.png"
        b2 = f + "/happy-birthday-card-picture-frame-greeting-card-clip-art-birthday-frames-0eb9653d62e134da4a9730accc2425fb.png"
        b3 = f + "/Bst.png"
        b4 = f + "/—Pngtree—fantasy beautiful color colorful _1224737.png"
        b5 = f + "/—Pngtree—happy birthday background shading_2256915.png"
        b6 = f + "/b6.png"
        b7 = f + "/circle2.png"

        if globals()['Backround_Name'] == b1:
            globals()['filenames'] = Image.open(
                str(globals()['filename'])
            )  # importing file path and opening from a global variable


            siz = (641, 586)
            globals()['filenames'].thumbnail(siz)  # Resizing the image

            globals()['image'] = Image.open(b1)  # Loading backround

            globals()['image_copy'] = globals()['image']  # copying the image just incase we lose the original image.
            image1 = True

            """
            if globals()['filenames'].width > globals()['filenames'].height:  # Logic for resizing a landscape image.
                # Landscape
    
                position = (30, int((590 - globals()['filenames'].height) / 2) + 590)
    
            
            else:
                position = (
                    int((652 - globals()['filenames'].width) / 2)+27), int(((590 - globals()['filenames'].height) / 2) + 590) # Logic for resizing a portrait image.
            """
            position = (
                (int((652 - globals()['filenames'].width) / 2) + 27),
                int(((590 - globals()['filenames'].height) / 2) + 597))

            globals()['image_copy'].paste(globals()['filenames'], position)

            # Saving the image as it can't be directly be given to the source of the Widget image.source.

            globals()['image_copy'].save("Final.png")
            self.ids.imagess.source = str("Final.png")
            self.ids.imagess.reload()
        elif globals()[
            'Backround_Name'] == b2:
            image2 = True
            globals()['filenames'] = ""
            globals()['filenames'] = Image.open(
                str(globals()['filename'])).convert('RGBA')
            if globals()['filenames'].width >= globals()['filenames'].height:
                self.ids.textinputbox.text = "Not Compatible"

            # globals()['filenames'] = Image.open(
            # "/Users/sanjayshreeyansgmail.com/Downloads/Adgenda Quiz 5th Feb.jpg").convert('RGBA')
            # importing file path and opening from a global variable
            print(globals()['filenames'].width, globals()['filenames'].height)

            # Resizing the image

            print(globals()['filenames'].width, globals()['filenames'].height)
            globals()['image'] = Image.open(b2)
            globals()['image'] = globals()['image'].convert('RGBA')
            print(globals()['image'].width, globals()['image'].width, " Background")
            # Loading backround

            globals()['image'] = globals()['image'].resize(
                (globals()["filenames"].width, globals()["filenames"].height))

            globals()['image_copy'] = globals()['image']  # copying the image just incase we lose the original image.
            """
            if globals()['filenames'].width > globals()['filenames'].height:  # Logic for resizing a landscape image.
                # Landscape

                position = (30, int((590 - globals()['filenames'].height) / 2) + 590)


            else:
                position = (
                    int((652 - globals()['filenames'].width) / 2)+27), int(((590 - globals()['filenames'].height) / 2) + 590) # Logic for resizing a portrait image.
            """

            globals()['filenames'].paste(globals()['image'], mask=globals()['image'])

            # Saving the image as it can't be directly be given to the source of the Widget image.source.

            globals()['filenames'].save("Final.png")
            self.ids.imagess.source = str("Final.png")
            self.ids.imagess.reload()
        elif globals()[
            'Backround_Name'] == b3:
            image3 = True
            globals()['filenames'] = ""
            globals()['filenames'] = Image.open(
                str(globals()['filename'])).convert('RGBA')
            if globals()['filenames'].width <= globals()['filenames'].height:
                self.ids.textinputbox.text = "Not Compatible"

            # globals()['filenames'] = Image.open(
            # "/Users/sanjayshreeyansgmail.com/Downloads/Adgenda Quiz 5th Feb.jpg").convert('RGBA')
            # importing file path and opening from a global variable
            print(globals()['filenames'].width, globals()['filenames'].height)

            # Resizing the image

            print(globals()['filenames'].width, globals()['filenames'].height)
            globals()['image'] = Image.open(b3)
            globals()['image'] = globals()['image'].convert('RGBA')
            print(globals()['image'].width, globals()['image'].width, " Background")
            # Loading backround

            globals()['image'] = globals()['image'].resize(
                (globals()["filenames"].width, globals()["filenames"].height))

            globals()['image_copy'] = globals()['image']  # copying the image just incase we lose the original image.
            """
            if globals()['filenames'].width > globals()['filenames'].height:  # Logic for resizing a landscape image.
                # Landscape

                position = (30, int((590 - globals()['filenames'].height) / 2) + 590)


            else:
                position = (
                    int((652 - globals()['filenames'].width) / 2)+27), int(((590 - globals()['filenames'].height) / 2) + 590) # Logic for resizing a portrait image.
            """

            globals()['filenames'].paste(globals()['image'], mask=globals()['image'])

            # Saving the image as it can't be directly be given to the source of the Widget image.source.

            globals()['filenames'].save("Final.png")
            self.ids.imagess.source = str("Final.png")
            self.ids.imagess.reload()
        elif globals()[
            'Backround_Name'] == b4:

            globals()['filenames'] = ""
            globals()['filenames'] = Image.open(
                str(globals()['filename'])).convert('RGBA')

            if globals()['filenames'].width >= globals()['filenames'].height:
                self.ids.textinputbox.text = "Not Compatible, height should be greater"

            # globals()['filenames'] = Image.open(
            # "/Users/sanjayshreeyansgmail.com/Downloads/Adgenda Quiz 5th Feb.jpg").convert('RGBA')
            # importing file path and opening from a global variable
            print(globals()['filenames'].width, globals()['filenames'].height)

            # Resizing the image

            print(globals()['filenames'].width, globals()['filenames'].height)
            globals()['image'] = Image.open(b4)
            globals()['image'] = image.convert('RGBA')
            print(globals()['image'].width, globals()['image'].width, " Background")
            # Loading backround

            globals()['image'] = globals()['image'].resize((globals()["filenames"].width, globals()["filenames"].height))

            globals()['image_copy'] = globals()['image'] # copying the image just incase we lose the original image.
            """
            if globals()['filenames'].width > globals()['filenames'].height:  # Logic for resizing a landscape image.
                # Landscape

                position = (30, int((590 - globals()['filenames'].height) / 2) + 590)


            else:
                position = (
                    int((652 - globals()['filenames'].width) / 2)+27), int(((590 - globals()['filenames'].height) / 2) + 590) # Logic for resizing a portrait image.
            """

            globals()['filenames'].paste(globals()['image'], mask=globals()['image'])

            # Saving the image as it can't be directly be given to the source of the Widget image.source.

            globals()['filenames'].save("Final.png")
            self.ids.imagess.source = str("Final.png")
            self.ids.imagess.reload()
        elif globals()[
            'Backround_Name'] == b5:

            globals()['filenames'] = ""
            globals()['filenames'] = Image.open(
                str(globals()['filename'])).convert('RGBA')


            # globals()['filenames'] = Image.open(
            # "/Users/sanjayshreeyansgmail.com/Downloads/Adgenda Quiz 5th Feb.jpg").convert('RGBA')
            # importing file path and opening from a global variable
            print(globals()['filenames'].width, globals()['filenames'].height)

            duplicate = globals()['filenames']
            # Resizing the image

            print(globals()['filenames'].width, globals()['filenames'].height)
            globals()['image'] = Image.open(b5)
            globals()['image'] = globals()['image'].convert('RGBA')
            print(globals()['image'].width, globals()['image'].width, " Background")
            # Loading backround

            globals()['image'] = globals()['image'].resize((globals()["filenames"].width, globals()["filenames"].height))

            globals()['image_copy'] = globals()['image']  # copying the image just incase we lose the original image.
            """
            if globals()['filenames'].width > globals()['filenames'].height:  # Logic for resizing a landscape image.
                # Landscape

                position = (30, int((590 - globals()['filenames'].height) / 2) + 590)


            else:
                position = (
                    int((652 - globals()['filenames'].width) / 2)+27), int(((590 - globals()['filenames'].height) / 2) + 590) # Logic for resizing a portrait image.
            """

            globals()['filenames'].paste(globals()['image'], mask=globals()['image'])

            # Saving the image as it can't be directly be given to the source of the Widget image.source.

            globals()['filenames'].save("Final.png")
            self.ids.imagess.source = str("Final.png")
            self.ids.imagess.reload()
        elif globals()[
            'Backround_Name'] == b6:

            globals()['filenames'] = ""
            globals()['filenames'] = Image.open(
                str(globals()['filename'])).convert('RGBA')
            if globals()['filenames'].width != globals()['filenames'].height:
                self.ids.textinputbox.text = "Not Compatible, be square"

            # globals()['filenames'] = Image.open(
            # "/Users/sanjayshreeyansgmail.com/Downloads/Adgenda Quiz 5th Feb.jpg").convert('RGBA')
            # importing file path and opening from a global variable
            print(globals()['filenames'].width, globals()['filenames'].height)

            duplicate = globals()['filenames']
            # Resizing the image

            print(globals()['filenames'].width, globals()['filenames'].height)
            globals()['image'] = Image.open(b6)
            globals()['image'] = globals()['image'].convert('RGBA')
            print(globals()['image'].width, globals()['image'].width, " Background")
            # Loading backround

            globals()['image'] = globals()['image'].resize((globals()["filenames"].width, globals()["filenames"].height))

            globals()['image_copy'] = globals()['image'] # copying the image just incase we lose the original image.
            """
            if globals()['filenames'].width > globals()['filenames'].height:  # Logic for resizing a landscape image.
                # Landscape

                position = (30, int((590 - globals()['filenames'].height) / 2) + 590)


            else:
                position = (
                    int((652 - globals()['filenames'].width) / 2)+27), int(((590 - globals()['filenames'].height) / 2) + 590) # Logic for resizing a portrait image.
            """

            globals()['filenames'].paste(globals()['image'], mask=globals()['image'])

            # Saving the image as it can't be directly be given to the source of the Widget image.source.

            globals()['filenames'].save("Final.png")
            self.ids.imagess.source = str("Final.png")
            self.ids.imagess.reload()
        elif globals()[
            'Backround_Name'] == b7:

            globals()['filenames'] = ""
            globals()['filenames'] = Image.open(
                str(globals()['filename'])).convert('RGBA')

            if globals()['filenames'].width != globals()['filenames'].height:
                self.ids.textinputbox.text = "Not Compatible, be square"

            # globals()['filenames'] = Image.open(
            # "/Users/sanjayshreeyansgmail.com/Downloads/Adgenda Quiz 5th Feb.jpg").convert('RGBA')
            # importing file path and opening from a global variable
            print(globals()['filenames'].width, globals()['filenames'].height)

            duplicate = globals()['filenames']
            # Resizing the image

            print(globals()['filenames'].width, globals()['filenames'].height)
            globals()['image'] = Image.open(b7)
            globals()['image'] = globals()['image'].convert('RGBA')
            print(globals()['image'].width, globals()['image'].width, " Background")
            # Loading backround

            globals()['image'] = globals()['image'].resize((globals()["filenames"].width, globals()["filenames"].height))

            globals()['image_copy'] = globals()['image']  # copying the image just incase we lose the original image.
            """
            if globals()['filenames'].width > globals()['filenames'].height:  # Logic for resizing a landscape image.
                # Landscape

                position = (30, int((590 - globals()['filenames'].height) / 2) + 590)


            else:
                position = (
                    int((652 - globals()['filenames'].width) / 2)+27), int(((590 - globals()['filenames'].height) / 2) + 590) # Logic for resizing a portrait image.
            """

            globals()['filenames'].paste(globals()['image'], mask=globals()['image'])

            # Saving the image as it can't be directly be given to the source of the Widget image.source.

            globals()['filenames'].save("Final.png")
            self.ids.imagess.source = str("Final.png")
            self.ids.imagess.reload()
    def mover(self):
        globals()['filenames'].paste(globals()['image'], (100,30), mask=globals()['image'])

        # Saving the image as it can't be directly be given to the source of the Widget image.source.

        globals()['filenames'].save("Final.png")
        self.ids.imagess.source = str("Final.png")
        print("Process successful")




    def text_render(self, text):
        print(text)

        img = globals()['filenames']
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype("/System/Library/Fonts/Palatino.ttc", 100)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text(((img.width - (img.width / 2)-100), (img.height - 100)), text, (255, 255, 255), font=font)
        img.save("sample-out.png")
        self.ids.textinputbox.pos_hint = {"center_x": 2, "center_y": 2}
        self.ids.imagess.source = ""
        self.ids.imagess.source = str("sample-out.png")


class main(App):  # Main App

    def build(self):  # Build Method
        return

    def selected(self, filename):
        globals()['filename'] = filename[0]  # Passing in the path for the variable that we can use to resize the image.
        print(globals()['filename'])  # Printing path to check if it is working


class MyWidget(GridLayout):  # Main Widget in Selection_Screen
    pass


class MyWidgets(GridLayout):  # Main Widget in Selection_Screen
    pass


class Final_Widget(FloatLayout):  # Main Widget in Final_Screen
    pass


class First_Widget(FloatLayout):  # Main Widget in Final_Screen
    pass

class Test_Screen(Screen):  # Main Widget in Final_Screen
    pass
class Test_Widget(FloatLayout):  # Main Widget in Final_Screen
    pass
# Needed for showing preview in Filechooser
class Selection_Screen_Backround(Screen):
    def Imagefecher(self):
        self.ids.image.source = globals()['Backround_Name']  # Needed for showing preview in Filechooser

    def selected(self, filename):
        globals()['Backround_Name'] = filename[
            0]  # Passing in the path for the variable that we can use to resize the image.
        print("Test PAssed")


class Selection_Screen(Screen):
    def helo(self):
        self.ids.image.source = globals()['filename']  # Needed for showing preview in Filechooser

main().run()  # Running the App
