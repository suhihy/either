from django.shortcuts import render, redirect
from .models import Either, Comment
from .forms import EitherForm, CommentForm


# Create your views here.
def index(request):
    eithers = Either.objects.all()

    context = {
        'eithers': eithers,
    }

    return render(request, 'index.html', context)

def detail(request, id):
    either = Either.objects.get(id=id)

    form = CommentForm()
    comments = Comment.objects.filter(either_id=id)
    
    total_comments = comments.count()
    a_count = comments.filter(choice='A').count()
    b_count = comments.filter(choice='B').count()

    a_percentage = (a_count / total_comments) * 100 if total_comments > 0 else 0
    b_percentage = (b_count / total_comments) * 100 if total_comments > 0 else 0

    context = {
        'either': either,
        'form': form,
        'comments': comments,
        'a_percentage': a_percentage,
        'b_percentage': b_percentage,
    }

    return render(request, 'detail.html', context)

def create(request):
    if request.method == 'POST':
        form = EitherForm(request.POST)
        if form.is_valid():
            either = form.save()
            return redirect('questions:index')

    else:
        form = EitherForm()

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)

def comment_create(request, either_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.either_id = either_id
            comment.save()
            return redirect('questions:detail', id=either_id)

    else:
        return redirect('questions:index')

def random(request):
    random = random.choice(either_id)

    context = {
        'random': random,
    }

    return render(request, 'random.html', context)