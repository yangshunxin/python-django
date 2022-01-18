from django.db import models


# Create your models here.

class Grades(models.Model):
    # Grades 表中的 字段名
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggrilnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField()

    def __str__(self):
        return self.gname

    class Meta:
        db_table = "grades"
        ordering = ["id"]


class StudentsManager(models.Manager):
    # 过滤掉 isDelete为True的
    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(isDelete=False)

    # 定义一个类方法来创建对象，不能用init
    def createStudent(self, name, age, gender, contend, grade, lastT, createT, isD=False):
        stu = self.model()
        print(type(grade))
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontendn = contend
        stu.sgrade = grade
        stu.lasttime = lastT
        stu.createtime = createT
        return stu


class Students(models.Model):
    # 自定义模型管理器
    # 自定义模型管理器，objects就不存在了
    objects = models.Manager()
    stuObj2 = StudentsManager()

    sname = models.CharField(max_length=20)
    sgender = models.BooleanField()
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    # 外键关联 Grades的主键
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)
    # 创建时间
    createtime = models.DateTimeField(auto_now_add=True)
    # 最后修改时间
    lasttime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sname

    # 定义表名和排序
    class Meta:
        db_table = "students"
        ordering = ["id"]

    # 定义一个类方法来创建对象，不能用init
    @classmethod
    def createStudent(cls, name, age, gender, contend, grade, lastT, createT, isD=False):
        return cls(sname=name, sage=age, sgender=gender, scontend=contend, sgrade=grade, lasttime=lastT,
                   createtime=createT, isDelete=isD)


from tinymce.models import HTMLField

class Text(models.Model):
    strField = HTMLField()
