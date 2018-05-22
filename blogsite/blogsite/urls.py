"""blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve


import xadmin
from users.views import *
from blogsite.settings import MEDIA_ROOT
from DjangoUeditor import urls as DjangoUeditor_urls

urlpatterns = [
    url(r'^admin/', xadmin.site.urls,name = 'admin'),
    #富文本编辑器
    url(r'^ueditor/',include(DjangoUeditor_urls)),
    #验证码
    url(r'^captcha/',include('captcha.urls')),
    #首页
    url(r'^$',IndexView.as_view(),name = 'index'),
    #登录
    url(r'^login/$',LoginView.as_view(),name = 'login'),   
    #登出
    url(r'^logout/$',LogoutView.as_view(),name = 'logout'),   
    #注册
    url(r'^register/$',RegisterView.as_view(),name = 'register'),
    #激活用户
    url(r'^active/(?P<email_code>.*)/$',ActiveUserView.as_view(),name = 'active'),
    #忘记密码
    url(r'^forget/$',ForgetPwdView.as_view(),name = 'forget'),
    #重置链接
    url(r'^reset/(?P<reset_code>.*)/$',ResetView.as_view(),name = 'reset'),
    #修改密码
    url(r'^reset_pwd/$',ResetPwdView.as_view(),name = 'reset_pwd'),

    #blog相关
    url(r'^blog/',include('blog.urls',namespace = 'blog')),
    #用户操作相关
    url(r'^user/',include('operation.urls',namespace = 'user')),
    #上传文件访问地址
    url(r'^media/(?P<path>.*)/$',serve,{"document_root":MEDIA_ROOT}),
    #测试环境关闭debug
    #url(r'^static/(?P<path>.*)/$',serve,{"document_root":STATIC_ROOT})


]

handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_erorr_500'
handler403 = 'users.views.page_erorr_403'