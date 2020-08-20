from django.shortcuts import render
from django.conf import settings


from .models import Photo

import os
from PIL import Image, ExifTags

def photography(request):

    photos = Photo.objects.all()

    for photo in photos:
        photo.contains_meta_data = False
        path = str(settings.BASE_DIR) + photo.image.url

        try:
            img = Image.open(path)
            exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
            setattr(photo, 'date', exif.get('DateTimeOriginal', ''))
            setattr(photo, 'aperture', exif.get('ApertureValue', ''))
            setattr(photo, 'focal', exif.get('FocalLength', ''))
            setattr(photo, 'model', exif.get('Model', ''))
            setattr(photo, 'exposure', exif.get('ExposureTime', ''))
            setattr(photo, 'iso', exif.get('ISOSpeedRatings', ''))
            setattr(photo, 'lens', exif.get('LensModel', ''))

            photo.contains_meta_data = True

        except AttributeError:
            exif = None

    return render(request, 'photography.html', {'photos': photos})


def photo(request):

    return render(request, 'photography.html', {'photos': photos})


# import os
# from PIL import Image, ExifTags
# path = '/home/victor/coding/projects/website/website/static/images/_photography'

# img = Image.open(os.path.join(path, 'IMG_0298.JPG'))

# exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
# print('\n'.join(['%s:%s' % (k, v) for k, v in exif.items()]))

# 'DateTimeOriginal'
# 'ApertureValue'
# 'FocalLength:28.0'
# 'Model'
# 'ExposureTime'
# 'ISOSpeedRatings'
# 'LensModel'
