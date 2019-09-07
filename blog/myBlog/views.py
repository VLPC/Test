# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Tag
from .utils import *
from .forms import *

from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

def posts_list(request):
	posts = Post.objects.all().order_by('-id')

	limit = request.GET.get('limit', 2)
	page = request.GET.get('page', 1)
	paginator = Paginator(posts, limit)
	page = paginator.page(page)
	
	return render(request, 'myBlog/index.html', {'page' : page})

def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'myBlog/tags_list.html', {'tags' : tags})

class PostDetails(ObjectDetailsMixin, View):
	model = Post
	template = 'myBlog/post_detail.html'

class TagDetails(ObjectDetailsMixin, View):
	model = Tag
	template = 'myBlog/tag_detail.html'

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	form = PostForm
	template = 'myBlog/post_create.html'
	raise_exception = True

class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	form = TagForm
	template = 'myBlog/tag_create.html'
	raise_exception = True

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Post
	form = PostForm
	template = 'myBlog/post_update.html'
	raise_exception = True

class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Tag
	form = TagForm
	template = 'myBlog/tag_update.html'
	raise_exception = True

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Post
	template = 'myBlog/post_delete.html'
	redirect_url = 'posts_list'
	raise_exception = True

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Tag
	template = 'myBlog/tag_delete.html'
	redirect_url = 'tags_list'
	raise_exception = True
