from django import forms
from multiselectfield import MultiSelectFormField


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }
        )
    )

    rating = forms.IntegerField(
        label='Rating',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter rating'
            }
        )
    )

    feedback = forms.CharField(
        label='Feedback',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter feedback'
            }
        )
    )


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }
        ), required=True
    )
    mobile = forms.IntegerField(
        label='Mobile number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Mobile number'
            }
        ), required=True, min_value=10
    )

    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }
        ), required=True
    )

    COURSE_CHOICES = (
        ('py', 'Python'),
        ('dj', 'Django'),
        ('ui', 'UI'),
        ('rest', 'REST API')
    )

    courses = MultiSelectFormField(choices=COURSE_CHOICES, required=True)

    SHIFT_CHOICES = (
        ('mng', 'Morning'),
        ('aftn', 'Afternoon'),
        ('evng', 'Evening'),
        ('ngt', 'Night')
    )

    shifts = MultiSelectFormField(choices=SHIFT_CHOICES, required=True)

    LOCATION_CHOICES = (
        ('hyd', 'Hyderabad'),
        ('bang', 'Banglore'),
        ('chen', 'Chennai'),
        ('pune', 'Pune')
    )

    locations = MultiSelectFormField(choices=LOCATION_CHOICES, required=True)

    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female')
    )

    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    y = range(2019, 1960, -1)

    start_date = forms.DateField(widget=forms.SelectDateWidget(years=y))
