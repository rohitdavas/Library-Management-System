from PIL import Image, ImageTk


def get_background_image(path) -> 'Tk image':
    """ returns the background image to be used from cover"""

    bg_image = Image.open(path)
    # bg_image = bg_image.resize((400,400))
    # TODO
    # image level resizing to fill the wall
    try:
        return ImageTk.PhotoImage(bg_image)

    except:
        raise (Exception("------Try to create tkinter root first"))


if __name__ == "__main__":
    img = get_background_image(path="lib.jpg")
    print(dir(img))
