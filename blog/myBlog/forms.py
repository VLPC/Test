from django import forms
from .models import Post, Tag
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):

	class Meta:
		model = Tag
		fields = ['title', 'slug']

	#title = forms.CharField(max_length=100)
	#slug = forms.CharField(max_length=100)

	def clean_slug(self):
		slug = self.cleaned_data['slug'].lower()
		if slug == 'create':
			raise ValidationError('Slug may not be "Create"')

		if Tag.objects.filter(slug__iexact=slug).count():
			raise ValidationError('Slug not unique')

		return slug

	#def save(self):
		#tag = Tag.objects.create(title=self.cleaned_data['title'], slug=self.cleaned_data['slug'])
		#return tag

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'slug', 'text', 'tags']

	def clean_slug(self):
		slug = self.cleaned_data['slug'].lower()
		if slug == 'create':
			raise ValidationError('Slug may not be "Create"')

		return slug
