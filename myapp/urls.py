from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^index.html/$', views.index),
    url(r'^(\d+)/$', views.detail),

    url(r'^grades/$', views.grades),
    url(r'^students/$', views.student),
    url(r'^grades/(\d+)$', views.gradeStudents),
    url(r'^attribles', views.attribles),
    url(r'^get1/$', views.get1),
    url(r'^get2/$', views.get2),
    url(r'^showregist/$', views.showregist),
    url(r'^showregist/regist/$', views.regist),
    url(r'^showresponse/$', views.showresponse),
    url(r'^cookietest/$', views.cookietest),

    url(r'^redirect1/$', views.redirect1),
    url(r'^redirect2/$', views.redirect2),

    url(r'^main/$', views.main),
    url(r'^login/$', views.login),
    url(r'^login/showmain/$', views.showmain),

    url(r'^good/$', views.good, name='good'),
    url(r'^extendmain/$', views.extendmain),
    url(r'^extenddetail/$', views.extenddetail),

    url(r'^postfile/$', views.postfile),
    url(r'^showinfo/$', views.showinfo),

    url(r'^verifycode/$', views.verifycode),
    url(r'^verifycodefile/$', views.verifycodefile),
    url(r'^verifycodecheck/$', views.verifycodecheck),

    url(r'^upfile/$', views.upfile, name='upfile'),
    url(r'^savefile/$', views.savefile, name='savefile'),

    url(r'^studentpage/(\d+)$', views.studentpage),

    url(r'^ajaxstudents/$', views.ajaxstudents),

    url(r'^studentsinfo/$', views.studentsinfo),
    url(r'^edit/$', views.edit),
]