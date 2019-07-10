from django.db import models
# 设计和表相对应的类，模板类
# Create your models here.

# 一类
# 图书类
class BookInfo(models.Model):
    '''图书模型类'''
    # 图书名称 CharFiekd代表是一个字符串，max_length 代表字符串的最大长度
    btitle = models.CharField(max_length=20)
    # 图书出版信息, DateField代表日期
    bpub_date = models.DateField()

    def __str__(self):
        return self.btitle

# 多类
# 英雄人物类
# 英雄名 hname
# 性别 hgender
# 年龄 hage
# 备注 hcomment
# 关系属性 hbook 简历图书类和英雄人物类之间一对多的关系
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20) # 英雄名称
    # 性别，BooleanField为bool类型，default为默认值，False为男
    hgender = models.BooleanField(default=False) # 英雄性别
    # 备注
    hcomment = models.CharField(max_length=128)
    # 关系属性
    hbook = models.ForeignKey('BookInfo')
