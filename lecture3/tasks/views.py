
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    else:
        return render(request, "tasks/add.html", {
            "form": NewTaskForm()
        })




# from django.shortcuts import render
# from django import forms
# from django.urls import reverse
# from django.http import HttpResponseRedirect

# # tasks = ["foo", "bar", "baz"]

# class NewTaskForm(forms.Form):
#     task = forms.CharField(label="New Task")

# # Create your views here.
# def index(request):
#     if "tasks" not in request.session:
#         request.session["tasks"]=[]
#     return render(request, "tasks/index.html", {
#         "tasks": request.session["tasks"]
#     } )


# #Add New Task
# def add(request):
#     #Check if methos id post
#     if request.method == "POST":
#         #take in the data the user submited and save it as form
#         form = NewTaskForm(request.POST)

#         #check if form data is valid (server-side)
#         if form.is_valid():
#             #Isolate  the task from the  'cleaned' version of form data
#             task = form.cleaned_data["task"]

#             request.session["tasks"] += [task]
#             return HttpResponseRedirect(reverse("tasks:index"))
#         else:
#             #if the form is invalid, re-render the page with existing information
#             return render(request, "tasks/add.html", {
#                 "form":form
#             })
#     else:
#          return render(request, "tasks/add.html", {
#              "form": NewTaskForm()
#              })

