from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	ruser_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext':user_text, 'rusertext':ruser_text, 'len':len(user_text.split())})