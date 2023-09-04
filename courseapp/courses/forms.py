from django.forms import SelectMultiple, TextInput, Textarea
from django import forms

from courses.models import Course
# class CourseCreateForm(forms.Form):
#     title = forms.CharField(label="Kurs Başlıgı",
#         required=True,
#         error_messages={
#             "required":"Kurs Başlığı Girmelisiniz."},
#         widget=forms.TextInput(attrs={"class":"form-control"}))
#     description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#     imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug = forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title','description','image','slug')  #'__all__' kullanılarak tum veriler alınabilir.
        labels ={
            'title' : 'Kurs Başlığı',
            'description' : 'Kurs Açıklaması',
            'imageUrl' : 'Resim bilgisi',
            'slug' : 'Kurs Adresi'
        }
        widgets ={
            "title" : TextInput(attrs={"class":"form-control"}),
            "description" : Textarea(attrs={"class":"form-control"}),
            "slug" : TextInput(attrs={"class":"form-control"}),
            "categories" : SelectMultiple(attrs={"class":"form-control"}),
        }
        error_messages ={
            "title": {
                "required":"Kurs Başlığı Girmelisiniz.",
                "max_length": "maksimum 50 karakter girmelisiniz."
            },

            "description": {
                "required":"Kurs Açıklaması Gerekmektedir."
            }
        }

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title','description','image','slug','categories',"isActive","isHome")  #'__all__' kullanılarak tum veriler alınabilir.
        labels ={
            'title' : 'Kurs Başlığı',
            'description' : 'Kurs Açıklaması',
            'image' : 'Resim bilgisi',
            'slug' : 'Kurs Adresi'
        }
        widgets ={
            "title" : TextInput(attrs={"class":"form-control"}),
            "description" : Textarea(attrs={"class":"form-control"}),
            "slug" : TextInput(attrs={"class":"form-control"}),
            "categories":SelectMultiple(attrs={"class":"form-control"})

        }
        error_messages ={
            "title": {
                "required":"Kurs Başlığı Girmelisiniz.",
                "max_length": "maksimum 50 karakter girmelisiniz."
            },

            "description": {
                "required":"Kurs Açıklaması Gerekmektedir."
            }
        }


class UploadForm(forms.Form):
    image = forms.ImageField()