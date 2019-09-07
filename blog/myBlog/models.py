# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, unique=True)
	text = models.TextField(blank=True)
	date = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk' : self.id})

	def get_update_url(self):
		return reverse('post_update', kwargs={'pk' : self.id})

	def get_delete_url(self):
		return reverse('post_delete', kwargs={'pk' : self.id})

	def __str__(self):
		return self.title

class Tag(models.Model):
	title = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('tag_detail', kwargs={'pk' : self.id})

	def get_update_url(self):
		return reverse('tag_update', kwargs={'pk' : self.id})

	def get_delete_url(self):
		return reverse('tag_delete', kwargs={'pk' : self.id})
