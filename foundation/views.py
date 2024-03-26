from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'foundation/index.html')


def about(request):
    context = {
        'title': 'About Us'
    }
    return render(request, 'foundation/about.html', context)


def sponsorship(request):
    sponsorships = Sponsorship.objects.all()
    context = {
        'sponsorships': sponsorships,
        'title': 'Sponsorship'
    }
    return render(request, 'foundation/sponsorship.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contacts = Contact(name=name, email=email,
                           phone=phone, message=message)
        contacts.save()
        return redirect('contact')
    context = {
        'title': "Contact Us"
    }
    return render(request, 'foundation/contact.html', context)

def getinvolve(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        states = request.POST['states']
        zipcode = request.POST['zipcode']
        volunteer_position = request.POST['volunteer_position']
        volunteer_experience = request.POST['volunteer_experience']
        volunteer_skills = request.POST['volunteer_skills']
        training_and_decrees_received = request.POST['training_and_decrees_received']
        reason_for_volunteer = request.POST['reason_for_volunteer']
        references = request.POST['references']
        datetime_available = request.POST['datetime_available']
        emergency_contact = request.POST['emergency_contact']
        criminal_conviction = request.POST['criminal_conviction']
        verified = request.POST['verified']
        signature = request.POST['signature']
        date = request.POST['date']
        message = request.POST['message']
        getinvolve = VolunteerApplication(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, city=city, states=states, zipcode=zipcode, volunteer_position=volunteer_position, volunteer_experience=volunteer_experience, volunteer_skills=volunteer_skills,
                                          training_and_decrees_received=training_and_decrees_received, reason_for_volunteer=reason_for_volunteer, references=references, datetime_available=datetime_available, emergency_contact=emergency_contact, criminal_conviction=criminal_conviction, verified=verified, signature=signature, date=date, message=message)
        getinvolve.save()
        return redirect('getinvolve')
    context = {
        'title': "Get Involve"
    }
    return render(request, 'foundation/getinvolve.html', context)


def watch(request):
    videos = YouTube.objects.all()
    context = {
        'videos': videos,
        'title': 'videos'
    }
    return render(request, 'foundation/watch.html', context)

def news(request):
    blogs = News.objects.all()
    context = {
        'blogs': blogs,
        'title': 'news',
    }
    return render(request, 'foundation/news.html', context)


def detail(request, news_slug):

    blog = News.objects.get(slug=news_slug)
    context = {
        'blog': blog,
        'title': 'news details'
    }
    return render(request, 'foundation/detailPage.html', context)


def photos(request):
    category = request.GET.get('category')

    if category == None:
        galleries = Gallery.objects.order_by('image')
    else:
        galleries = Gallery.objects.filter(category__title=category)
    categories = GalleryCategory.objects.all()
    context = {
        'categories': categories,
        'galleries': galleries,
        'title': 'Gallery'
    }
    return render(request, 'foundation/photos.html', context)

def galleryDetail(request):
    category = request.GET.get('category')
    gallery = Gallery.objects.filter(category__title=category).first()
    if category == None:
        galleries = Gallery.objects.order_by('image')
    else:
        galleries = Gallery.objects.filter(category__title=category)
    context = {
        'category': category,
        'gallery': gallery,
        'galleries': galleries,
        'title': 'Gallery'
    }
    return render(request, 'foundation/galleryDetail.html', context)




def ghProject(request):
    category = request.GET.get('category')

    if category == None:
        projects = GhanaProject.objects.order_by('image')
    else:
        projects = GhanaProject.objects.filter(category__title=category)
    categories = GhanaCategory.objects.all()
    context = {
        'categories': categories,
        'projects': projects,
        'title': 'Ghana Project'
    }
    return render(request, 'foundation/gh_project.html', context)


def ghprojectPhotos(request):

    category = request.GET.get('category')

    if category == None:
        projects = GhanaProject.objects.order_by('image')
    else:
        projects = GhanaProject.objects.filter(category__title=category)
    categories = GhanaCategory.objects.all()

    context = {
        'categories': categories,
        'projects': projects,
        'title': 'Donate'
    }
    return render(request, 'foundation/ghprojectPhotos.html', context)


def usaProject(request):
    category = request.GET.get('category')

    if category == None:
        projects = USAProject.objects.order_by('image')
    else:
        projects = USAProject.objects.filter(category__title=category)
    categories = USACategory.objects.all()

    context = {
        'categories': categories,
        'projects': projects,
        'title': 'USA Project'
    }
    return render(request, 'foundation/usa_project.html', context)


def usaprojectPhotos(request):

    category = request.GET.get('category')

    if category == None:
        projects = USAProject.objects.order_by('image')
    else:
        projects = USAProject.objects.filter(category__title=category)
    categories = USACategory.objects.all()

    context = {
        'categories': categories,
        'projects': projects,
        'title': 'Donate'
    }
    return render(request, 'foundation/usaprojectPhotos.html', context)
