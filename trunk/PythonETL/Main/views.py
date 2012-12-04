# Create your views here.
from Main.models import Template, Job, Output, TemplateForm, TemplateFormSet,OutputForm,JobForm,JobFormSet
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.forms.models import modelformset_factory
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext

import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


def counter(until):
    count_list = range(1-(until+1))   
    dictionary = {}
    for i in count_list: 
        dictionary.update(dict(i=i))
    return dictionary

def listar(until):
    count_list = range(1-(until+1))   
    return count_list

@csrf_protect
def templates_create(request):   
    if request.method == 'POST':
        form_data = TemplateForm(request.POST)
        if form_data.is_valid():           
            c = {}
            #c.update(csrf(request))
            form_data.save()
            return redirect('/templates/show/all/')  
        else:
            error = 'No valid: create template data'
            errors=form_data.errors
            return render_to_response('pendings_show_all.html', {'error':error,'errors':errors}, context_instance=RequestContext(request)) 
    else:
        form = TemplateForm()
        object_Name = 'Template'
        c = {"form":form, "object_Name":object_Name, }
        c.update(csrf(request))
    return render_to_response("create_templates.html",c, context_instance=RequestContext(request)) 



@csrf_protect
def templates_show_all(request):  
    template_list = Template.objects.all().order_by('id')
    object_Name = 'Template'
    response = render_to_response('templates_show_all.html', {'template_list':template_list,'object_Name':object_Name, }, context_instance=RequestContext(request))#'job_list':job_list,'output_list':output_list,})
    return response


def templates_show_by_id(request,id1):
        the_template = Template.objects.get(pk=id1)
        object_Name = 'Template'
        return render_to_response("show_templates_by_id.html", {'object_Name':object_Name, 'the_template':the_template, }, context_instance=RequestContext(request))

@csrf_protect
def templates_edit_all(request):
    TemplateFormSet = modelformset_factory(Template,extra=0)
    if request.method == 'POST':
        formset = TemplateFormSet(request.POST, request.FILES)
        if formset.is_valid():
            c = {}
            formset.save()
            return render_to_response('pendings_show_all.html')
    else:
        formset = TemplateFormSet()
        c = {'formset': formset}
        c.update(csrf(request))
        
    return render_to_response("edit_templates.html", c)


@csrf_protect
def templates_edit_by_id(request,id1):
        the_template=Template.objects.get(pk=id1)      
        if request.method == 'POST':
            form = TemplateForm(request.POST, instance = the_template)
            if form.is_valid():
                c = {}
                form.save()
            #return render_to_response('getting-started.html', {'edited_id':id1, })   #wawa
            return redirect('/templates/show/all/')   #wawa
        else:                
            form = TemplateForm(instance=the_template)    
            object_Name = 'Template'
            c = {'form': form, 'object_Name':object_Name, "edited_id":id1, }
            c.update(csrf(request))    
            return render_to_response("edit_templates_by_id.html", c, context_instance=RequestContext(request))


@csrf_protect
def templates_delete(request):
    TemplateFormSet = modelformset_factory(Template, can_delete=True, extra=0)
    if request.method == 'POST':
        formset = TemplateFormSet(request.POST, request.FILES)
        if formset.is_valid():
            c = {}
            formset.save()
            return redirect('/templates/show/all/')   
    else:
        formset = TemplateFormSet()
        c = {'formset': formset}
        c.update(csrf(request))
    return render_to_response("delete_templates.html", c)


@csrf_protect
def templates_delete_by_id(request, id1):     
        Template.objects.filter(id=id1).delete()
        return redirect('/templates/show/all/',context_instance=RequestContext(request))


@csrf_protect
def outputs_show_all(request):  
    output_list = Output.objects.all().order_by('id')
    object_Name = 'Outputs'
    response = render_to_response('outputs_show_all.html', {'output_list':output_list, 'object_Name':object_Name, }, context_instance=RequestContext(request))
    return response




@csrf_protect
def manager_outputs(request): 
    OutputFormSet = modelformset_factory(Output)
    if request.method == 'POST':
        formset = OutputFormSet(request.POST, request.FILES)
        if formset.is_valid():
            c = {}
            formset.save()
            return render_to_response('pendings_show_all.html') 
    else:
        formset = OutputFormSet()
        c = {'formset': formset}
        c.update(csrf(request))
        
    return render_to_response("edit_outputs.html", c)


@csrf_protect
def manager_jobs(request): 
    JobFormSet = modelformset_factory(Job, can_delete=True)
    if request.method == 'POST':
        formset = JobFormSet(request.POST, request.FILES)
        if formset.is_valid():
            c = {}
            formset.save()
            return render_to_response('pendings_show_all.html')    
    else:
        formset = JobFormSet()
        c = {'formset': formset}
        c.update(csrf(request))
        
    return render_to_response("edit_jobs.html", c)


@csrf_protect
def outputs_create(request):   
    if request.method == 'POST':
        form_data = OutputForm(request.POST)
        if form_data.is_valid():          
            c = {}
            form_data.save()
            return render_to_response('pendings_show_all.html')#, {'created_outputs':created_content})
        else:
            error = 'No valid: create output data'
            errors=form_data.errors
            return render_to_response('pendings_show_all.html', {'error':error,'errors':errors})
    else:
        form = OutputForm()
        c = {'form': form}
        c.update(csrf(request))
    return render_to_response("create_outputs.html",c) 
        


def outputs_show_by_id(request):
    OutputFormSet = modelformset_factory(Output, extra=0)
    if request.method == 'POST':
        formset = OutputFormSet(request.POST, request.FILES)
        if formset.is_valid():
            c = {}
            formset.save()
            return render_to_response('pendings_show_all.html')
    else:
        form = OutputForm()
        c = {'form': form}
        c.update(csrf(request))

    return render_to_response("edit_outputs.html", c)



@csrf_protect
def outputs_edit_all(request):
    OutputFormSet = modelformset_factory(Output,extra=0)
    if request.method == 'POST':
        formset = OutputFormSet(request.POST, request.FILES)
        if formset.is_valid():
            c = {}
            formset.save()
            return render_to_response('pendings_show_all.html')
    else:
        formset = OutputFormSet()
        c = {'formset': formset}
        c.update(csrf(request))
        
    return render_to_response("edit_outputs.html", c)


@csrf_protect
def outputs_delete(request):
    OutputFormSet = modelformset_factory(Output, can_delete=True, extra=0)
    if request.method == 'POST':
        formset = OutputFormSet(request.POST, request.FILES)
        if formset.is_valid():
            c = {}
            formset.save()
            return render_to_response('pendings_show_all.html')    
    else:
        formset = OutputFormSet()
        c = {'formset': formset}
        c.update(csrf(request))
        
    return render_to_response("delete_outputs.html", c)

@csrf_protect
def outputs_delete_by_id(request, id1):     
        Output.objects.filter(id=id1).delete()
        return render_to_response('pendings_show_all.html', {'deleted_id':id1, })

@csrf_protect
def outputs_edit_by_id(request,id1):
        the_output=Output.objects.get(pk=id1)      
        if request.method == 'POST':
            form = OutputForm(request.POST, instance = the_output)
            if form.is_valid():
                c = {}
                form.save()
            return render_to_response('pendings_show_all.html', {'edited_id':id1, })   
        else:                
            form = OutputForm(instance=the_output)    
            c = {'form': form}
            c.update(csrf(request))    
            return render_to_response("edit_outputs_by_id.html", c) 
        


def handle_uploaded_file(f):
    with open('file', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@csrf_protect
def jobs_create(request):   
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():          
            c = {}
         
            
            form.save()
            
            return redirect('/jobs/show/all/',context_instance=RequestContext(request))
        else:
            error = 'No valid: create job data'
            errors=form.errors
            return render_to_response('jobs_show_all.html', {'error':error,'errors':errors})
    else:
        form = JobForm()
        object_Name = 'Job'
        days_in_month = range(1,32)
        c = {'form': form,'object_Name':object_Name, 'days_in_month' : days_in_month }
        
        c.update(csrf(request))
    return render_to_response("create_jobs.html",c,context_instance=RequestContext(request))  


@csrf_protect
def jobs_show_all(request):
    job_list = Job.objects.all().order_by('id')
    object_Name = 'Job'
    response = render_to_response('jobs_show_all.html', {'job_list':job_list, 'object_Name':object_Name, }, context_instance=RequestContext(request))
    return response

@csrf_protect
def jobs_show_by_id(request,id1):
        the_job = Job.objects.get(pk=id1)
        object_Name = 'Job'
        c = {'the_job': the_job, 'object_Name':object_Name, "edited_id":id1, }
        c.update(csrf(request))    
        return render_to_response("show_jobs_by_id.html", c, context_instance=RequestContext(request))

@csrf_protect
def jobs_edit_all(request):
    JobFormSet = modelformset_factory(Job, extra=0)
    if request.method == 'POST':
        formset = JobFormSet(request.POST, request.FILES)
        if formset.is_valid():
            c = {}
            formset.save()
            return render_to_response('pendings_show_all.html')
    else:
        formset = JobFormSet()
        c = {'formset': formset}
        c.update(csrf(request))
        
    return render_to_response("edit_jobs.html", c)

@csrf_protect
def jobs_delete(request):
    JobFormSet = modelformset_factory(Job, can_delete=True, extra=0)

    if request.method == 'POST':
        formset = JobFormSet(request.POST, request.FILES)
        if formset.is_valid():
            c = {}
            formset.save()
            return render_to_response('pendings_show_all.html')    
    else:
        formset = JobFormSet()
        c = {'formset': formset}
        c.update(csrf(request))
        
    return render_to_response("delete_jobs.html", c)


@csrf_protect
def jobs_delete_by_id(request, id1):     
        Job.objects.filter(id=id1).delete()
        #return render_to_response('pendings_show_all.html', {'deleted_id':id1, })
        return redirect('/jobs/show/all/',context_instance=RequestContext(request))


@csrf_protect
def jobs_edit_by_id(request,id1):
        the_job=Job.objects.get(pk=id1)      
        if request.method == 'POST':
            form = JobForm(request.POST, instance = the_job)
            if form.is_valid():
                c = {}
                form.save()
            return render_to_response('pendings_show_all.html', {'edited_id':id1, }, context_instance=RequestContext(request)) 
        else:                
            form = JobForm(instance=the_job)    
            object_Name = 'Job'
            days_in_month = range(1,32)          
            c = {'form': form, 'days_in_month' : days_in_month, 'object_Name':object_Name, 'the_job':the_job }
            c.update(csrf(request))    
            return render_to_response("edit_jobs_by_id.html", c, context_instance=RequestContext(request))
        
#pendings are Jobs with STATUS:TO_REVIEW.        
@csrf_protect
def pendings_show_all(request):
    pending_list = Job.objects.filter(status='TO_REVIEW')
    #pending_list = Job.objects.all().order_by('id')
    object_Name = 'Pending'
    response = render_to_response('pendings_show_all.html', {'pending_list':pending_list, 'object_Name':object_Name, }, context_instance=RequestContext(request))
    return response


@csrf_protect
def pendings_validate_by_id(request,id1):
        the_pending=Job.objects.get(pk=id1)      
        if request.method == 'POST':
            form = JobForm(request.POST, instance = the_pending)
            if form.is_valid():
                c = {}
                form.save()
            return render_to_response('pendings_show_all.html', {'edited_id':id1, }, context_instance=RequestContext(request)) 
        else:                
            form = JobForm(instance=the_pending)    
            object_Name = 'Pending'         
            c = {'form': form, 'object_Name':object_Name, 'the_pending':the_pending }
            c.update(csrf(request))    
            return render_to_response("validate_pendings_by_id.html", c, context_instance=RequestContext(request))

def count_pendings(request):
    badge_pendings=Job.objects.filter(status='TO_REVIEW').count()
    return {'badge_pendings' : badge_pendings }

def index(request):
    return render_to_response("pendings_show_all.html")












    
