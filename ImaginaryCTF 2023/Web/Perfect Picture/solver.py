from PIL import Image, PngImagePlugin

def create_perfect_picture():
    # Create a new image with the desired dimensions (690x420 pixels)
    img = Image.new("RGBA", (690, 420), (255, 255, 255, 255))

    # Set pixel colors at specified coordinates
    img.putpixel((412, 309), (52, 146, 235, 123))
    img.putpixel((12, 209), (42, 16, 125, 231))
    img.putpixel((264, 143), (122, 136, 25, 213))

    # Add metadata to the image
    metadata = PngImagePlugin.PngInfo()
    metadata.add_text("Description", "jctf{not_the_flag}")
    metadata.add_text("Title", "kool_pic")
    metadata.add_text("Author", "anon")

    # Save the image with metadata
    img.save("perfect_picture.png", pnginfo=metadata)

    print("Perfect picture created and saved as perfect_picture.png")

if __name__ == "__main__":
    create_perfect_picture()
