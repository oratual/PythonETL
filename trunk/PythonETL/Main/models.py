# Create your models here.
from django.db import models
import datetime
from django.utils import timezone
from django.forms import ModelForm
from django import forms
from django.forms.models import modelformset_factory

class Template(models.Model):
    name = models.CharField(max_length=256)
    content = models.TextField() #xml-txt data
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)
    
    #objects = TemplateManager()
    def __unicode__(self):
        return self.name
    
    def was_created_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)
        
class Job(models.Model):
    template =models.ForeignKey('Template')
    #source = models.CharField(max_length=1024) #change to filefield
    source = models.FileField(upload_to='doc')
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)
    dow = models.PositiveSmallIntegerField(blank=True) #1...7 
    dom = models.PositiveSmallIntegerField(blank=True) #1...31
    hour = models.TimeField(blank=True)
    
    #periodicity choice
    daily = 'DAILY' 
    monthly = 'MONTHLY'
    weekly = 'WEEKLY'
    PERIODICITY_CHOICES = (
        (daily, 'DAILY'), 
        (monthly, 'MONTHLY'),
        (weekly, 'WEEKLY'),
    )
    periodicity =  models.CharField(max_length=10,
                                    choices=PERIODICITY_CHOICES)

    #status choice
    default = 'DEFAULT'
    to_review = 'TO_REVIEW'
    finished_with_error = 'FINISHED_WITH_ERROR'
    finished = 'FINISHED'    
    STATUS_CHOICES = (                      
        (default, 'DEFAULT'),
        (to_review, 'TO_REVIEW'),
        (finished_with_error, 'FINISHED_WITH_ERROR'),
        (finished, 'FINISHED'),
        )
    status =  models.CharField(max_length=30,
                               choices=STATUS_CHOICES)
    
    def __unicode__(self):
        return self.source
#nombre???

class Output(models.Model):
    job = models.ForeignKey('Job')
    file = models.TextField()
    to_review = models.BooleanField()
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)
    
    def __unicode__(self):
        return self.file
    
class TemplateForm(ModelForm):
    class Meta:
        model = Template
        exclude = ('created','updated')
        

              
#class TemplateListForm(ModelForm):
#    class Meta:
#        
#        
##        content = CharField(max_length = 1500,
##        widget= forms.Textarea(attrs={'class':'task-description'}),
#        required=True)
#        
#        model = Template
#        #edit=False
#        exclude = ('created','updated')
      
        
class JobForm(ModelForm):    
    class Meta:
        model = Job           
        exclude = ('created','updated')




class JobForm2(ModelForm):    
    class Meta:
        model = Job           
        exclude = ('created','updated')
        widgets = {
            #'dow': 
            #'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }        
        
        
        
        
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )        
        
        
class OutputForm(ModelForm):
    class Meta:
        model = Output   
        exclude = ('created','updated') 
      
        
TemplateFormSet = modelformset_factory(Template)
JobFormSet = modelformset_factory(Job)
OutputFormSet = modelformset_factory(Output)

#class TemplateIDForm(ModelForm):
#    class Meta:
#        model = Template
#        #edit=False
#        exclude = ('created','updated')


        