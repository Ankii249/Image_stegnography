# # import io
# # from idlelib.autocomplete import FILES
# #
# # from django.shortcuts import render
# # import stepic    # pip install stepic
# # from PIL import Image   # pip install pillow
# # from django.utils.archive import extract
# #
# #
# # # Create your views here.
# #
# # def index(request):
# #     return render(request,'index.html')
# #
# # def hide_text_in_image(image,text):
# #     data = text.encode('utf-8')
# #     return stepic.encode(image,data)
# #
# # def encryption_views(request):
# #     message = " "
# #     if request.method == "POST":
# #         text = request.POST['text']
# #         image_file = request.FILES['image']
# #         image = Image.open(image_file)
# #
# #         if image.format != 'PNG':
# #             image = image.convert('RGBA')
# #             buffer = io.BytesIO()
# #             image.save(buffer, format="PNG")
# #             image = Image.open(buffer)
# #
# #         new_image = hide_text_in_image(image,text)
# #         image_path = 'encrypted_images/' + 'new_'+image_file.name
# #         new_image.save(image_path)
# #         message = "Text has been encrypted in the image "
# #     return render(request,'encryption.html',locals())
# #
# # def decryption_views(request):
# #     text = ""
# #     if request.method == 'POST':
# #         image_file = request.FILES['image']
# #         image = Image.open(image_file)
# #
# #         if image.format != 'PNG':
# #             image = image.convert('RGBA')
# #             buffer = io.BytesIO()
# #             image.save(buffer,format="PNG")
# #             image = Image.open(buffer)
# #
# #         text = extract_text_from_image(image)
# #     return render(request,'decryption.html',locals())
# #
# # def extract_text_from_image(image):
# #     data = stepic.decode(image)
# #     if isinstance(data,bytes):
# #         return data.decode('utf-8')
# #     return data
#
#



import io
from django.shortcuts import render
import stepic  # pip install stepic
from PIL import Image  # pip install pillow


# Create your views here.
def index(request):
    return render(request, 'index.html')


def hide_text_in_image(image, text):
    data = text.encode('utf-8')
    return stepic.encode(image, data)


def encryption_views(request):
    message = " "
    if request.method == "POST":
        text = request.POST['text']
        image_file = request.FILES['image']
        image = Image.open(image_file)

        # Ensure the image is in PNG format (Stepic does NOT support JPEG)
        if image.mode != 'RGBA':
            image = image.convert('RGBA')

        buffer = io.BytesIO()
        image.save(buffer, format="PNG")  # Always save as PNG
        buffer.seek(0)
        image = Image.open(buffer)

        # Encrypt text into the image
        new_image = hide_text_in_image(image, text)

        # Save encrypted image as PNG only
        image_path = 'encrypted_images/new_' + image_file.name
        if not image_path.lower().endswith('.png'):
            image_path = image_path.rsplit('.', 1)[0] + ".png"  # Ensure PNG extension

        new_image.save(image_path, format="PNG")

        message = "Text has been encrypted in the image."
    return render(request, 'encryption.html', locals())


def decryption_views(request):
    text = ""
    if request.method == 'POST':
        image_file = request.FILES['image']  # Fix request.FILES typo
        image = Image.open(image_file)

        # Ensure the image is in PNG format
        if image.mode != 'RGBA':
            image = image.convert('RGBA')

        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)
        image = Image.open(buffer)

        # Extract hidden text
        text = extract_text_from_image(image)
    return render(request, 'decryption.html', locals())


def extract_text_from_image(image):
    try:
        data = stepic.decode(image)
        if isinstance(data, bytes):
            return data.decode('utf-8')  # Ensure UTF-8 decoding
        return str(data)
    except Exception as e:
        return f"Error: Unable to extract text ({str(e)})"  # Handle decoding




