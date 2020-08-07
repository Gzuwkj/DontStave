from .feild import ListFiled
from django.db import models
from tinymce.models import HTMLField
from Issue.models import Problem
from UserProfile.models import User

ATTRIBUTE_CHOICE = (('私有', '私有'), ('公开', '公开'))
LANGUAGE_CHOICE = (('C', 'C'), ('C++', 'C++'), ('Java', 'Java'), ('Python', 'Python'))


class Match(models.Model):  # 比赛列表
    matchName = models.CharField(max_length=30)  # 比赛名称
    startTime = models.DateTimeField()  # 开始时间
    howLong = models.IntegerField(default=120, blank=True)  # 比赛时长
    attribute = models.CharField(max_length=2, choices=ATTRIBUTE_CHOICE, default='公开')  # 比赛属性
    info = models.TextField(blank=True, default='这个出题人很懒，没有比赛说明...')  # 比赛说明
    registerNum = models.IntegerField(default=0)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.matchName

    def get_problem_list(self):
        from Contest.serializers import MatchIncludeSerializer
        problem_list = self.matchinclude_set
        problem_list = MatchIncludeSerializer(problem_list)
        return problem_list.data

    # def get_problems(self):


class MatchSubmit(models.Model):  # 比赛提交
    match = models.ForeignKey(to=Match, on_delete=models.CASCADE, default='')  # 比赛ID
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default='')  # 用户名
    problem = models.ForeignKey(to=Problem, on_delete=models.CASCADE, default='')  # 题目编号
    content = models.TextField(blank=True)  # 提交代码
    runID = models.AutoField(primary_key=True)  # 运行编号
    result = models.CharField(max_length=2, default='0', blank=True)  # 运行结果
    time = models.IntegerField(blank=True, default=0)  # 运行时间
    memory = models.IntegerField(blank=True, default=0)  # 运行内存
    language = models.CharField(default='C++', blank=True, max_length=9, choices=LANGUAGE_CHOICE)  # 语言
    subTime = models.DateTimeField(auto_now=True)  # 提交时间

    def __str__(self):
        return str(self.runID)


class MatchRankManager(models.Manager):
    def create(self, *args, **kwargs):
        if 'problem_num' in kwargs:
            kwargs['rank'] = [{'is_ac': False, 'useTime': 0, 'wrongTime': 0} for i in range(0, kwargs['problem_num'])]
        return super(MatchRankManager, self).create(*args, **kwargs)


class MatchRank(models.Model):  # 比赛排名
    match = models.ForeignKey(to=Match, on_delete=models.CASCADE, default='')  # 比赛
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default='')  # 用户名
    acNum = models.IntegerField(blank=True, default=0)
    rank = ListFiled(blank=True, default='[]')
    objects = MatchRankManager()

    def __init__(self, *args, **kwargs):
        problem_num = None
        if 'problem_num' in kwargs:
            problem_num = kwargs['problem_num']
            del kwargs['problem_num']
        super().__init__(*args, **kwargs)
        if problem_num:
            self.rank = [{'is_ac': False, 'useTime': 0, 'wrongTime': 0, 'problem_no': chr(ord('A') + i)}
                         for i in range(0, problem_num)]

    def __str__(self):
        return str(self.id) + ' ' + str(self.rank)


class MatchRegister(models.Model):  # 注册比赛
    match = models.ForeignKey(to=Match, on_delete=models.CASCADE, default='')  # 比赛
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default='')  # 用户名
    registerTime = models.DateTimeField(auto_now=True)  # 注册时间

    def __str__(self):
        return self.match


class MatchInclude(models.Model):
    no = models.CharField(default='A', max_length=1)
    match = models.ForeignKey(to=Match, on_delete=models.CASCADE, default='')  # 比赛ID
    problem = models.ForeignKey(to=Problem, on_delete=models.CASCADE, default='')  # 问题
    first_ac = models.OneToOneField(to=User, on_delete=models.SET_DEFAULT, default='0')  # 第一个ac者
    ac_num = models.IntegerField(default=0)  # ac人数
    total_num = models.IntegerField(default=0)  # 总提交

    def __str__(self):
        return str(self.id)
