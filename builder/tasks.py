import time

from celery import shared_task
import os
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont

from builder.models import Mockup, Dress


@shared_task()
def mockup_builder(mockup_id):
    time.sleep(30)
    mockup = Mockup.objects.get(pk=mockup_id)
    image_folder = os.path.join(settings.BASE_DIR, 'static', 'shirts')
    output_folder = os.path.join(settings.MEDIA_ROOT, 'edited')
    os.makedirs(output_folder, exist_ok=True)
    font = ImageFont.truetype("arial.ttf", 60)
    text = mockup.text
    for filename in os.listdir(image_folder):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            img_path = os.path.join(image_folder, filename)
            output_path = os.path.join(output_folder, filename)

            image = Image.open(img_path)
            img_width, img_height = image.size
            draw = ImageDraw.Draw(image)

            x = img_width / 2
            y = img_height / 2
            draw.text((x, y), text, fill=(255, 255, 255), font=font)

            image.save(output_path)
            Dress.objects.create(image=output_path, mockup=mockup)

    return mockup.id