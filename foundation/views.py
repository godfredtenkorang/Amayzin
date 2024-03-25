from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    main_category = request.GET.get('main_category')

    if main_category == None:
        projects = Project.objects.order_by('image')
    else:
        projects = Project.objects.filter(category__name=main_category)
    main_categories = ProjectCategory.objects.all()
    
    context = {
        'projects': projects,
        'main_categories': main_categories,
        'main_category': main_category
    }
    return render(request, 'foundation/index.html', context)

def about(request):
    main_category = request.GET.get('main_category')

    if main_category == None:
        projects = Project.objects.order_by('image')
    else:
        projects = Project.objects.filter(category__name=main_category)
    main_categories = ProjectCategory.objects.all()

    context = {
        'projects': projects,
        'main_categories': main_categories,
        'main_category': main_category,
        'title': 'About Us'
    }
    return render(request, 'foundation/about.html', context)

def sponsorship(request):
    main_category = request.GET.get('main_category')

    if main_category == None:
        projects = Project.objects.order_by('image')
    else:
        projects = Project.objects.filter(category__name=main_category)
    main_categories = ProjectCategory.objects.all()
    sponsorships = Sponsorship.objects.all()
    context = {
        'projects': projects,
        'main_categories': main_categories,
        'main_category': main_category,
        'sponsorships': sponsorships,
        'title': 'Sponsorship'
    }
    return render(request, 'foundation/sponsorship.html', context)

def contact(request):
    main_category = request.GET.get('main_category')

    if main_category == None:
        projects = Project.objects.order_by('image')
    else:
        projects = Project.objects.filter(category__name=main_category)
    main_categories = ProjectCategory.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contacts = Contact(name=name, email=email, phone=phone, message=message)
        contacts.save()
        return redirect('contact')
    context = {
        'projects': projects,
        'main_categories': main_categories,
        'main_category': main_category,
        'title': "Contact Us"
    }
    return render(request, 'foundation/contact.html', context)

def getinvolve(request):
    main_category = request.GET.get('main_category')

    if main_category == None:
        projects = Project.objects.order_by('image')
    else:
        projects = Project.objects.filter(category__name=main_category)
    main_categories = ProjectCategory.objects.all()
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
        getinvolve = VolunteerApplication(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, city=city, states=states, zipcode=zipcode, volunteer_position=volunteer_position, volunteer_experience=volunteer_experience, volunteer_skills=volunteer_skills, training_and_decrees_received=training_and_decrees_received, reason_for_volunteer=reason_for_volunteer, references=references, datetime_available=datetime_available, emergency_contact=emergency_contact, criminal_conviction=criminal_conviction, verified=verified, signature=signature, date=date, message=message)
        getinvolve.save()
        return redirect('getinvolve')
    context = {
        'projects': projects,
        'main_categories': main_categories,
        'main_category': main_category,
        'title': "Get Involve"
    }
    return render(request, 'foundation/getinvolve.html', context)

def watch(request):
    main_category = request.GET.get('main_category')

    if main_category == None:
        projects = Project.objects.order_by('image')
    else:
        projects = Project.objects.filter(category__name=main_category)
    main_categories = ProjectCategory.objects.all()
    videos = YouTube.objects.all()
    context = {
        'projects': projects,
        'main_categories': main_categories,
        'main_category': main_category,
        'videos': videos,
        'title': 'videos'
    }
    return render(request, 'foundation/watch.html', context)

def news(request):
    main_category = request.GET.get('main_category')

    if main_category == None:
        projects = Project.objects.order_by('image')
    else:
        projects = Project.objects.filter(category__name=main_category)
    main_categories = ProjectCategory.objects.all()
    blogs = News.objects.all()
    context = {
        'projects': projects,
        'main_categories': main_categories,
        'main_category': main_category,
        'blogs': blogs,
        'title': 'news',
    }
    return render(request, 'foundation/news.html', context)

def detail(request, news_slug):
    main_category = request.GET.get('main_category')

    if main_category == None:
        projects = Project.objects.order_by('image')
    else:
        projects = Project.objects.filter(category__name=main_category)
    main_categories = ProjectCategory.objects.all()
    blog = News.objects.get(slug=news_slug)
    context = {
        'projects': projects,
        'main_categories': main_categories,
        'main_category': main_category,
        'blog': blog,
        'title': 'news details'
    }
    return render(request, 'foundation/detailPage.html', context)

def photos(request):
    main_category = request.GET.get('main_category')

    if main_category == None:
        projects = Project.objects.order_by('image')
    else:
        projects = Project.objects.filter(category__name=main_category)
    main_categories = ProjectCategory.objects.all()
    category = request.GET.get('category')
    
    if category == None:
        galleries = Gallery.objects.order_by('image')
    else:
        galleries = Gallery.objects.filter(category__title=category)
    categories = GalleryCategory.objects.all()
    context = {
        'projects': projects,
        'main_categories': main_categories,
        'main_category': main_category,
        'categories': categories,
        'galleries': galleries,
        'title': 'Gallery'
    }
    return render(request, 'foundation/photos.html', context)

def galleryDetail(request):
    main_category = request.GET.get('main_category')

    if main_category == None:
        projects = Project.objects.order_by('image')
    else:
        projects = Project.objects.filter(category__name=main_category)
    main_categories = ProjectCategory.objects.all()
    category = request.GET.get('category')
    gallery = Gallery.objects.filter(category__title=category).first()
    if category == None:
        galleries = Gallery.objects.order_by('image')
    else:
        galleries = Gallery.objects.filter(category__title=category)
    context = {
        'projects': projects,
        'main_categories': main_categories,
        'main_category': main_category,
        'category': category,
        'gallery': gallery,
        'galleries': galleries,
        'title': 'gallery'
    }
    return render(request, 'foundation/galleryDetail.html', context)

def project(request):
    main_category = request.GET.get('main_category')
    project = Project.objects.filter(main_category__name=main_category).first()

    if main_category == None:
        projects = Project.objects.order_by('-date_added')
    else:
        projects = Project.objects.filter(category__name=main_category)
    main_categories = ProjectCategory.objects.all()

    context = {
        'project': project,
        'projects': projects,
        'main_category': main_category,
        'main_categories': main_categories,
        'title': 'Projects'
    }
    return render(request, 'foundation/project.html', context)

def donate(request):
    main_category = request.GET.get('main_category')

    if main_category == None:
        projects = Project.objects.order_by('-date_added')
    else:
        projects = Project.objects.filter(category__name=main_category)
    main_categories = ProjectCategory.objects.all()
    
    context = {
        'projects': projects,
        'main_categories': main_categories,
        'main_category': main_category,
        'title': 'Donate'
    }
    return render(request, 'foundation/donate.html', context)


def projectPhotos(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    
    context = {
        'project': project,
        'title': 'Donate'
    }
    return render(request, 'foundation/projectPhotos.html', context)

