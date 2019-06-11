from django.shortcuts import render
from .forms import FeedbackForm, ContactForm
from .models import FeedbackData, CoursesData, ContactData
from django.http.response import HttpResponse
import datetime

date1 = datetime.datetime.now()


# Create your views here.

def main_page(request):
    return render(request, 'base.html')


def home_page(request):
    return render(request, 'home_page.html')


def contact_page(request):
    if request.method == 'POST':
        cform = ContactForm(request.POST)
        if cform.is_valid():
            name = cform.cleaned_data.get('name', '')
            mobile = cform.cleaned_data.get('mobile', '')
            email = cform.cleaned_data.get('email', '')
            courses = cform.cleaned_data.get('courses', '')
            shifts = cform.cleaned_data.get('shifts', '')
            locations = cform.cleaned_data.get('locations', '')
            gender = cform.cleaned_data.get('gender', '')
            start_date = cform.cleaned_data.get('start_date', '')

            data = ContactData(
                name=name,
                mobile=mobile,
                email=email,
                courses=courses,
                shifts=shifts,
                locations=locations,
                gender=gender,
                start_date=start_date
            )
            data.save()
            cform = ContactForm()
            return render(request, 'contact_page.html', {'cform': cform})
        else:
            return HttpResponse("all fields are mandatory")
    else:
        cform = ContactForm()
        return render(request, 'contact_page.html', {'cform': cform})


def courses_page(request):
    courses = CoursesData.objects.all()
    return render(request, 'courses_page.html', {'courses': courses})


def feedback_page(request):
    if request.method == 'POST':
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get('name', '')
            rating = request.POST.get('rating', '')
            feedback = request.POST.get('feedback', '')

            data = FeedbackData(
                name=name,
                rating=rating,
                date=date1,
                feedback=feedback
            )
            data.save()
            ddata = FeedbackData.objects.all()
            fform = FeedbackForm()
            return render(request, 'feedback_page.html', {'fform': fform, 'ddata': ddata})
        else:
            return HttpResponse('All fields are mandatory')
    else:
        ddata = FeedbackData.objects.all()
        fform = FeedbackForm()
        return render(request, 'feedback_page.html', {'fform': fform, 'ddata': ddata})


def team_page(request):
    return render(request, 'team_page.html')


def gallery_page(request):
    return render(request, 'gallery_page.html')
