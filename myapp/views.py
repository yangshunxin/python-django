from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Students
def index(request):
    # return HttpResponse("ysx first django html page")
    student = Students.objects.get(pk=1)
    students = Students.objects.all()
    return render(request, 'myapp/index.html', {"stu": student, "students": students, "num": 10,
    'str': "ysx is a good man", 'list':["faf", "aaaa"], 'code': "<h1> i am code<h1/>"})

def detail(request, num):
    return HttpResponse("response: {}".format(num))

from .models import Grades
def grades(request):
    # 去模版里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板， 模板再渲染页面，然后将渲染好的页面给到浏览器
    return render(request,
                  'myapp/grades.html', # 模版路径，前面的路径在setting.py中已经配置了
                  {'grades': gradesList} # 传递给模板的参数，key:模版中的变量名，value：当前文件中的值
                  )

def student(request):
    studensList = Students.objects.all()
    return render(request,
                  'myapp/students.html',
                  {"students": studensList}
                  )

def gradeStudents(request, gradeid):
    # 获取班级对象
    grade = Grades.objects.get(pk=gradeid)
    # 获取班级对象下的 学生列表
    studentsList = grade.students_set.all()
    return render(request, 'myapp/students.html', {'students':studentsList})

def addstudent(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("刘德华",12, True, "i am liudehau", grade, "2019-01-01", '2020-09')
    stu.save()

def attribles(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attribles")

def get1(request):
    """
    获取get传递的数据
    :param request:
    :return:
    """
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse("a={} b={} c={}".format(a, b, c))

def get2(request):
    """
    http://localhost:8000/get1?a=1&a=2&b=2&c=3
    :param request:
    :return:
    """
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse("a={} a2={} c={}".format(a1, a2, c))


def showregist(request):
    return render(request, 'myapp/regist.html')

def regist(request):
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    hobby = request.POST.getlist("hobby")
    return HttpResponse("name:{} gender:{} age:{} hobby:{}".format(name, gender, age, hobby))

def showresponse(request):
    res = HttpResponse("143234")
    return HttpResponse("{} {} {}".format(res.content, res.charset, res.status_code))

def cookietest(request):
    """
    第一次设置cookie后，以后直接取就可以了,浏览器每次都会带着这个cookie给我
    :param request:
    :return:
    """
    cookie = request.COOKIES

    res = HttpResponse("cookie key:{} value:{}".format("ysx", cookie["ysx"]))

    # res.write("test cookie")
    # res.set_cookie("ysx","good")
    return res

# 输入http://localhost:8000/redirect1 显示的是redirect2的内容
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def redirect1(request):
    # return HttpResponseRedirect("/redirect2")
    return redirect('/redirect2')

def redirect2(request):
    return HttpResponse("我是reditect2")


def main(request):
    # 取出username
    username = request.session.get("name", "游客")
    print("main:{}".format(username))
    return render(request, 'myApp/main.html', {"username": username})

def login(request):
    return render(request, 'myapp/login.html')

def showmain(request):
    # username = request.POST.get("username", "123")
    username = request.POST.get("name")
    print("showmain:{}".format(username))
    request.session["name"] = username
    return redirect('/main')

def good(request):
    return render(request, "myapp/good.html")


def extendmain(request):
    return render(request, 'myapp/extend-main.html')

def extenddetail(request):
    return render(request, 'myapp/extend-detail.html')


def postfile(request):
    return render(request, 'myapp/postfile.html')

def showinfo(request):
    username = request.POST.get("username")
    passwd = request.POST.get("passwd")
    return render(request, 'myapp/showinfo.html', {"username": username, "passwd": passwd})

def verifycode(request):
    """
    生产验证码
    :param request:
    :return:
    """
    from PIL import Image, ImageDraw, ImageFont
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), random.randrange(20, 100))
    width = 100
    height = 50
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的被选值
    str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklxcvbnm'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str[random.randrange(0, len(str))]
    # 构造字体对象
    font = ImageFont.truetype(r"/System/Library/Fonts/Supplemental/Arial Black.ttf", 40)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5,2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25,2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50,2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75,2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存到内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存文件中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

def verifycodefile(request):
    """
    获取验证码页面
    :param request:
    :return:
    """
    flag = request.session.get('flag', True)
    tag = ''
    if flag == False:
        tag = '请重新输入'
    request.session.clear()
    return render(request, 'myapp/verifycodefile.html', {"flag": tag})

def verifycodecheck(request):
    """
    点击登陆上传验证码信息
    :param request:
    :return:
    """
    code1 = request.POST.get('verifycode').upper()
    code2 = request.session["verifycode"]
    if code1 == code2:
        return render(request, 'myapp/success.html')
    else:
        # 登陆失败，就设置标志位
        request.session['flag'] = False
        return redirect('/myapp/verifycodefile')

def upfile(request):
    return render(request, 'myapp/upfile.html')

import os
from django.conf import settings

def savefile(request):
    if request.method == "POST":
        f = request.FILES["file"]
        # 文件在服务器中路径
        filePath = os.path.join(settings.MDEIA_ROOT, f.name)
        with open(filePath, 'wb') as fp:
            for info in f.chunks():
                fp.write(info)
        return HttpResponse("上传成功")
    else:
        return HttpResponse("上传失败")

from django.core.paginator import Paginator

def studentpage(request, pageid):
    # 所有学生的列表
    allList = Students.objects.all()
    #
    paginator = Paginator(allList, 3)
    page = paginator.page(pageid)

    return render(request, 'myapp/studentpage.html', {"students": page})

def ajaxstudents(request):
    return render(request, 'myapp/ajaxstudents.html')

from django.http import JsonResponse
def studentsinfo(request):
    stus = Students.objects.all()
    list = []
    for stu in stus:
        list.append([stu.sname, stu.sage])
    return JsonResponse({"data": list})

def edit(request):
    return render(request, 'myapp/edit.html')