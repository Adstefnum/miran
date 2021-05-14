from django.contrib import admin
from videos.models import *


class VideoAdmin(admin.ModelAdmin):
	list_display = ['id','title','video_id','description','is_published']
	list_filter = ['active']
	search_fields = ['title']
	readonly_fields = ['id','is_published']
	class Meta:
		model = Video

admin.site.register(Video, VideoAdmin)


class PublishedVideoAdmin(admin.ModelAdmin):
	list_display = ['title','video_id','description']
	search_fields = ['title']
	class Meta:
		model = PublishedVideo

	def query_set(self,request):
		return Video.objects.filter(active=True)

admin.site.register(PublishedVideo,PublishedVideoAdmin)
