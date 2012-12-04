"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

import unittest
from models import Template,Job,Output

#test Database IO
class TemplateTestCase(unittest.TestCase):
    def setUp(self):
        'Populate a template'
        self.template1=Template.objects.create(content="test_xml.xml")    
        #test if not empty
        entry_list = list(Template.objects.all())
        if  len(entry_list) > 0:
            print("Template Entry contained in queryset")
        else:
            print("Template Queryset empty!")   
        
        "Dummy template show"            
        print self.template1.id
        print self.template1.content
        print self.template1.created
        print self.template1.updated

        'Populate a dummy job'
        template1FK = Template.objects.get(content="test_xml.xml")
        template1FK.save()      
        self.job1 = Job.objects.create( template = template1FK, source = "test_source.url", periodicity = 'MONTHLY', hour = '14:30:59', dow = 4, dom = 15)
        
        "Dummy job show"
        print self.job1.id
        print self.job1.source
        print self.job1.periodicity
        print self.job1.hour
        print self.job1.dow
        print self.job1.dom
        
        "Populate a dummy output"
        job1FK = Job.objects.get(source="test_source.url")
        job1FK.save()      
        
        entry_list = list(Job.objects.all())
        if  len(entry_list) > 0:
            print("Job Entry contained in queryset")
        else:
            print("Job Queryset empty!")
        
        self.output1 = Output.objects.create( job = job1FK, file = "test_file.fil", to_review = False)
        
        "Dummy output show"
        print self.output1.id
        print self.output1.file
        print self.output1.to_review
        print self.output1.created
        print self.output1.updated
        
    def test_template_show(self):
        'Test the Database objects'   
        self.assertEqual(self.template1.content, "test_xml.xml")
        self.assertEqual(self.job1.source, "test_source.url")
        self.assertEqual(self.output1.file, "test_file.fil")        
        
        
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
