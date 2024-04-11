from django.shortcuts import render

def story(request):
    return render(request, 'story/story.html')