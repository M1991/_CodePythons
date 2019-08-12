import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based views

# def home(request):
# 	html_ ="""
# 	<!DOCTYPE html>
# 	<html lang=en>

# 	<head></head>
# 	<body> 
# 	<h1> Hello World </h1>
# 	<p>This is testing </p>
# 	</body>
# 	</html>
# 	"""
# 	return HttpResponse(html_)
# 	#return render(request,"home.html",{})

# def home(request):
# 	num = random.randint(0,1000000)
# 	some_list = [num, random.randint(0,1000000),random.randint(0,1000000)]
# 	context = {
# 		"bool_item": False,
# 		"num":num,
# 		"some_list":some_list
# 	}
# 	return render(request,"base.html",context)

def home(request):
	num = random.randint(0,1000000)
	some_list = [num, random.randint(0,1000000),random.randint(0,1000000)]
	context = {
		"bool_item": False,
		"num":num,
		"some_list":some_list
	}
	return render(request,"home.html",context)

def home2(request):
	# num = random.randint(0,1000000)
	# some_list = [num, random.randint(0,1000000),random.randint(0,1000000)]
	context = {
		# "bool_item": False,
		# "num":num,
		# "some_list":some_list
	}
	return render(request,"home2.html",context)

def home3(request):	
	context = {
		# "bool_item": False,
		# "num":num,
		# "some_list":some_list
	}
	return render(request,"home3.html",context)