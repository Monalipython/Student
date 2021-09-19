from django.core import paginator
from django.shortcuts import render ,HttpResponseRedirect ,get_object_or_404 ,redirect
from .forms import StudentRegistration
from .models import *
from django.core.paginator import Paginator ,EmptyPage , PageNotAnInteger
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.views.generic import TemplateView , ListView, CreateView
from django.core.mail import message, send_mail , BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from .forms import BookForm





# Create your views here.
# This function  for add and show data
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
          nm = fm.cleaned_data['name']
          em = fm.cleaned_data['email']
          pw = fm.cleaned_data['password']
          p = Profile(name = nm , email = em , password = pw)
          p.save()
          subject= "Website Inquiry"
          body = {
                'nm' : fm.cleaned_data['name'],
                'em' : fm.cleaned_data['email'],
                'pw' : fm.cleaned_data['password']
            }
          message = '\n'.join(body.values())
          try:
                send_mail(subject ,message , 'monali.nimkar7@gmail.com' , ['recieiver@gmail.com'])
          except BadHeaderError:
             return HttpResponse("Invalid header found")
            
          messages.success(request , "Student data save  and email send successfully......")
          fm = StudentRegistration()  
    else:
        fm = StudentRegistration() 
    stud = Profile.objects.all() 
    paginator = Paginator(stud , 4)
    page_number = request.GET.get('page')
    try:
        stud_list = paginator.page(page_number)
    except PageNotAnInteger:
        stud_list = paginator.page(1)
    except EmptyPage:
       stud_list= paginator.page(paginator.num_pages)  
    return render(request , 'enroll/addandshow.html',{'form':fm , 'stud_list' :stud_list})


#This function for update data
def update_data(request,id):
    if request.method =='POST':
       pi =   Profile.objects.get(pk = id)
       fm = StudentRegistration(request.POST , instance=pi)
       if fm.is_valid():
           fm.save()
           messages.info(request , "Student data update successfully......")
    else:
        pi =   Profile.objects.get(pk = id)
        fm = StudentRegistration(instance=pi)    
    return render(request , 'enroll/updatestudent.html',{'form':fm})
    

#This function for delete data
def delete_data(request , id):
    if request.method =='POST':
        p = Profile.objects.get(pk = id)  
        p.delete()
        messages.warning(request , "Student data deleted successfully......")
        return HttpResponseRedirect('/')



print("----------------")

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        messages.success(request , "File upload successfully......")
    return render(request, 'enroll/upload.html', context)


def book_list(request):
    books = Book.objects.all()
    return render(request, 'enroll/book_list.html', {
        'books': books
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'enroll/upload_book.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
        messages.warning(request , "Book deleted successfully......")
    return redirect('book_list')


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'
