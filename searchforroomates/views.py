from django.shortcuts import render

# Create your views here.
def SearchforroomatesView(request):
	return render(request, 'searchforroomates.html')