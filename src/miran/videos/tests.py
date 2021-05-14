from django.test import TestCase
from videos.models import *


class VideoModelTestCase(TestCase):
	"""It is usually good to test as a whole unit as below but also create
	individual tests for each field,, why? since in setup if one fielf fails, all fails
	which is what happens in filling the real database too. Why then are individual tests important
	1. to make sure that each field meets not only the group standard but individual standard,
	this can be skipped only if all it's individual standards are accurately tested in the group test
	to test individually, just create seperately. It is confirmed that you will need to test some
	things like max_length specifically but it could work in a group test,."""

	def setUp(self):
		Video.objects.create(

			title="Ola Iya",
			description="A film about a mother's stuggles.", 
			slug="ola-iya",
			video_id="hbcu84iribf"

			)


	def test_valid_title(self):
		title="Ola Iya"
		qs = Video.objects.filter(title=title)
		self.assertTrue(qs.exists())

	def test_valid_description(self):
		description="A film about a mother's stuggles."
		qs = Video.objects.filter(description=description)
		self.assertTrue(qs.exists())

	def test_valid_slug(self):
		slug="ola-iya"
		qs = Video.objects.filter(slug=slug)
		self.assertTrue(qs.exists())

	def test_valid_video_id(self):
		video_id="hbcu84iribf"
		qs = Video.objects.filter(video_id=video_id)
		self.assertTrue(qs.exists())

