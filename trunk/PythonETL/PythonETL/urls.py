from django.conf.urls import patterns, url, include
from django.conf import settings
from django.conf.urls.static import static
from Main.views import templates_create,templates_show_all,templates_show_by_id,templates_edit_all,templates_edit_by_id,\
        templates_edit_by_id,templates_delete,templates_delete_by_id,\
        jobs_create,jobs_show_all,jobs_show_by_id,jobs_edit_all,\
        jobs_delete,jobs_edit_by_id,jobs_delete_by_id,\
        outputs_create,outputs_show_all,outputs_show_by_id,manager_outputs,\
        outputs_delete,outputs_edit_by_id,outputs_delete_by_id,index,\
        pendings_show_all,pendings_validate_by_id

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       
         
    # Examples:
    # url(r'^$', 'PythonETL.views.home', name='home'),
    # url(r'^PythonETL/', include('PythonETL.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#templates_create,templates_show_all,templates_show_by_id,manager_templates,templates_edit_by_id,/
#templates_edit_by_id,templates_delete,templates_delete_by_id
#
#jobs_create,jobs_show_all,jobs_show_by_id,manager_jobs,jobs_edit_by_id,/
#jobs_edit_by_id,jobs_delete,jobs_delete_by_id
#
#outputs_create,output_show_alls,outputs_show_by_id,manager_outputs,outputs_edit_by_id,/
#outputs_edit_by_id,outputs_delete,outputs_delete_by_id
    
    url(r'^index/$', index),    
    #templates
    url(r'^templates/create$', templates_create),    
    url(r'^templates/show/all/$', templates_show_all), 
    url(r'^templates/show/(\d+)/$', templates_show_by_id), #show by id
    url(r'^templates/edit/all$', templates_edit_all),
    url(r'^templates/edit/(\d+)/$', templates_edit_by_id), #edit by id   
    url(r'^templates/delete/all$', templates_delete), #show all to check delete
    url(r'^templates/delete/(\d+)/$', templates_delete_by_id), #delete by id
    #jobs
    url(r'^jobs/create$', jobs_create),    
    url(r'^jobs/show/all/$', jobs_show_all), 
    url(r'^jobs/show/(\d+)/$', jobs_show_by_id), #show by id
    url(r'^jobs/edit/all$', jobs_edit_all),
    url(r'^jobs/edit/(\d+)/$', jobs_edit_by_id), #edit by id   
    url(r'^jobs/delete/all$', jobs_delete), #show all to check delete
    url(r'^jobs/delete/(\d+)/$', jobs_delete_by_id), #delete by id
    #outputs
    url(r'^outputs/create$', outputs_create),    
    url(r'^outputs/show/all/$', outputs_show_all), 
    url(r'^outputs/show/(\d+)/$', outputs_show_by_id), #show by id
    url(r'^outputs/edit/all$', manager_outputs),
    url(r'^outputs/edit/(\d+)/$', outputs_edit_by_id), #edit by id   
    url(r'^outputs/delete/all$', outputs_delete), #show all to check delete
    url(r'^outputs/delete/(\d+)/$', outputs_delete_by_id), #delete by id
    #pendings are Jobs wit STATUS:TO_REVIEW
    url(r'^pendings/show/all/$', pendings_show_all), #show all
    url(r'^pendings/validate/(\d+)/$', pendings_validate_by_id), #validate by id
    
    

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
    
#
#      s
#    #url(r'^templates/edit/(\d+)/$', manager_templates), #edit by id
#
#
#    
# 
#
#    url(r'^manage_jobs$', manager_jobs),
#    url(r'^manage_outputs$', manager_outputs),
#    #url(r'^index.html$', index),
    
#)
