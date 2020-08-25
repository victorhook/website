from django.db import models

class Photo(models.Model):

    image = models.ImageField('photography/')
    title = models.CharField(max_length=100, null=True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.image



# import os
# from PIL import Image, ExifTags
# path = '/home/victor/coding/projects/website/website/static/images/_photography'

# for img in os.listdir(path):
#     img = Image.open(os.path.join(path, img))

#     exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
#     print('\n'.join(['%s:%s' % (k, v) for k, v in exif.items()]))
