from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

class ObjectDetailsMixin:
	model = None
	template = None

	def get(self, request, pk):
		obj = get_object_or_404(self.model, id=pk)
		return render(request, self.template, {self.model.__name__.lower() : obj, 'admin_object' : obj, 'detail' : True})

class ObjectCreateMixin:
	form = None
	template = None

	def get(self, request):
		form = self.form()
		return render(request, self.template, {'form' : form})

	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid():
			obj = form.save()
			return redirect(obj)
		return render(request, self.template, {'form' : form})

class ObjectUpdateMixin:
	model = None
	form = None
	template = None

	def get(self, request, pk):
		obj = self.model.objects.get(id=pk)
		form = self.form(instance=obj)
		return render(request, self.template, {'form' : form, self.model.__name__.lower() : obj})

	def post(self, request, pk):
		obj = self.model.objects.get(id=pk)
		form = self.form(request.POST, instance=obj)
		if form.is_valid():
			new_obj = form.save()
			return redirect(new_obj)
		return render(request, self.template, {'form' : form, self.model.__name__.lower() : obj})

class ObjectDeleteMixin:
	model = None
	template = None
	redirect_url = None

	def get(self, request, pk):
		obj = self.model.objects.get(id=pk)
		return render(request, self.template, {self.model.__name__.lower() : obj})

	def post(self, request, pk):
		obj = self.model.objects.get(id=pk)
		obj.delete()
		return redirect(reverse(self.redirect_url))
