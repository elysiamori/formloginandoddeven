# importing the necessary libraries
from django.shortcuts import render
def index(request):
      number = int(request.GET.get('number', 0))
      return render(request, 'index.html', {'number': number})