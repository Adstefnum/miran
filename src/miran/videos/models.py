from django.db import models

class Video(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(null=True,blank=True)
	slug = models.SlugField(blank=True)
	video_id = models.CharField(max_length=100)
	active = models.BooleanField(default=True)

	""" Also add date_created, date_updated, published
	and think of others to add"""

	@property
	def is_published(self):
		return self.active
	
class PublishedVideo(Video):
	class Meta:
		proxy = True
		verbose_name = 'Published Video'
		verbose_name_plural = 'Published Videos'


