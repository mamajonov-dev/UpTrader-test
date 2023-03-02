from django.shortcuts import render, redirect
from .models import ProjectsModel
from .forms import ProjectsForm


def projects(request):
    projects = ProjectsModel.objects.all()

    return render(request=request, template_name='projects/projects.html', context={'projects': projects})

def project(request, pk):
    projectObj = ProjectsModel.objects.get(id=pk)
    tags = projectObj.tags.all()

    return render(request=request, template_name='projects/single-project.html', context={'project': projectObj, 'tags': tags})

def createProject(request):
    form = ProjectsForm
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request=request, template_name='projects/project_form.html', context={'form': form})

def updateProject(request,  pk):
    project = ProjectsModel.objects.get(id=pk)
    form = ProjectsForm(instance=project)
    if request.method =='POST':
        form = ProjectsForm(request.POST, request.FILES , instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    return render(request, 'projects/project_form.html', {'form': form})

def deleteProject(request, pk):
    project = ProjectsModel.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)