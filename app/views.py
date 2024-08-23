from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader
from app.models import JobPost
job_title = [
    "First Job",
    "Second job",
    "Third job"
]

job_description = [
    "First job description",
    "Second job description",
    "Third job Description"
]

# <ul><li>job 1</li> <li>job 1</li> <li>job 1</li></ul>

# Create your views here.
# def hello(request):
#     return HttpResponse('<h3>Hello World</h3s>')
class TempClass:
    x=5


def hello(request):
    
    list = ['Alpha','Beta']
    is_authenticated = 1
    context = {
        'name':'Abhay',
        "first_list":list,
        'temp_object':TempClass,
        'age':19,
        'is_authenticated':is_authenticated
         }
    return render(request, "app/Hello.html", context)

def job_list(request):
    # <ul><li>job 1</li> <li>job 1</li> <li>job 1</li></ul>
    # list_of_jobs = "<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail_url = reverse('jobs_detail', args=(job_id,))
    #     list_of_jobs += f"<li><a href='{detail_url}'><b>{j}</b></a></li>"
    # list_of_jobs += "</ul>"
    # return HttpResponse(list_of_jobs)
    jobs = JobPost.objects.all()
    context = {
        "jobs":jobs, 
    }
    return render(request, "app/index.html", context)

#"<domaain>/job/1" --> job detail page
def job(request, id):
    try:
        # if id ==  0:
        #     return redirect(reverse('jobs_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}"
        # return HttpResponse(return_html)
        # context = {
        #     "job_title":job_title[id],
        #     "job_desciption":job_description[id]
        # }
        job = JobPost.objects.get(id=id)
        context = {
            "job":job,
        }
        return render(request, "app/job_detail.html", context)
    except: 
        return HttpResponseNotFound("Not Found")