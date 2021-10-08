from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_avatar.png', upload_to='profile_pics/')

    def __str__(self) -> str:
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        image = Image.open(self.image.path)
        if image.height > 300 or image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.image.path)


class Post(models.Model):
	description = models.CharField(max_length=255, blank=True)
	pic = models.ImageField(upload_to='doodle/')
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.description


	def get_absolute_url(self):
		return reverse('profile', kwargs={'pk': self.pk})
