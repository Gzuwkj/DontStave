from django.db import models
from tinymce.models import HTMLField


from UserProfile.models import User
import os

POWER_CHOSE = (('公开', '公开'), ('隐藏', '隐藏'))
LANGUAGE_CHOICE = (('C', 'C'), ('C++', 'C++'), ('Java', 'Java'), ('Python', 'Python'))
CLASSIFICATION = (('搜索', '搜索'), ('计算几何', '计算几何'), ('数学', '数学'),
                  ('数据结构', '数据结构'), ('动态规划', '动态规划'),
                  ('图论', '图论'), ('基本算法', '基本算法'))


def save_standard_input(instance, filename):
    return os.path.join('problems/', str(instance), filename)


def save_standard_output(instance, filename):
    return os.path.join('problems/', str(instance), filename)


class Problem(models.Model):                                 # 问题类
    no = models.IntegerField(primary_key=True)               # 题目编号
    title = models.CharField(max_length=20, unique=True)     # 标题
    content = HTMLField(blank=True, default='')               # 内容
    InputFormat = HTMLField(blank=True, default='')           # 输入
    OutputFormat = HTMLField(blank=True, default='')          # 输出
    time = models.IntegerField(blank=True, default=1000)     # 运行时间
    memory = models.IntegerField(blank=True, default=256)    # 运行内存
    tips = HTMLField(blank=True, default='')                           # 提示
    probSource = models.CharField(max_length=10, blank=True)          # 题目来源
    classification = models.CharField(choices=CLASSIFICATION, blank=True, max_length=10)  # 分类
    probAuthority = models.CharField(default='公开', choices=POWER_CHOSE, max_length=2)   # 权限
    weight = models.IntegerField(default=100)      # 分数
    ac_nums = models.IntegerField(default=0)       # 通过数
    submit_nums = models.IntegerField(default=0)   # 提交数

    def update_problem(self, data):  # 改
        self.title = data.get("title", self.title)
        self.content = data.get("content", self.content)
        self.InputFormat = data.get("InputFormat", self.InputFormat)
        self.OutputFormat = data.get("OutputFormat", self.OutputFormat)
        self.time = data.get("time", self.time)
        self.memory = data.get("memory", self.memory)
        self.tips = data.get("tips", self.tips)
        self.probSource = data.get("probSource", self.probSource)
        self.classification = data.get("classification", self.classification)
        self.probAuthority = data.get("probAuthority", self.probAuthority)
        self.weight = data.get("weight", self.weight)
        self.ratio = data.get("ratio", self.ratio)

    def get_problem(self):
        from .serializers import ProblemSerializer
        problemSerializer = ProblemSerializer(self)
        data = problemSerializer.data
        # 获取样例
        from Issue.serializers import ProblemExampleSerializer
        problem_ExampleList = self.problemexample_set.all()
        problem_ExampleList = ProblemExampleSerializer(problem_ExampleList, many=True).data
        data.update({"problemExample": problem_ExampleList})
        return data


    def __str__(self):
        return str(self.no)


class ProblemData(models.Model): #数据
    problem = models.ForeignKey(to=Problem, on_delete=models.CASCADE, default='') #与Problem一对多
    standardInput = models.FileField(upload_to=save_standard_input, blank=True)  # 标准输入
    standardOutput = models.FileField(upload_to=save_standard_output, blank=True)  # 标准输出

    def updata_problemdata(self, data):
        self.standardInput = data.get("standardInput", self.standardInput)
        self.standardOutput = data.get("standardOutput", self.standardOutput)

    def get_problemdata(self):
        from .serializers import ProblemDataSerializer
        problemDataSerializer = ProblemDataSerializer(self)
        return  problemDataSerializer.data


class ProblemExample(models.Model): #样例
    problem = models.ForeignKey(to=Problem, on_delete=models.CASCADE, default='')  # 与Problem一对多
    sampleInput = HTMLField(blank=True,default='')  # 样列输入
    sampleOutput = HTMLField(blank=True, default='') # 样列输出

    def updata_problemexample(self, data):
        self.sampleInput = data.get("sampleInput", self.sampleInput)
        self.sampleOutput = data.get("sampleOutput", self.sampleOutput)

    def get_problemexample(self):
        from .serializers import ProblemExampleSerializer
        problemExampleSerializer = ProblemExampleSerializer(self)
        return problemExampleSerializer.data


class ProblemSubmit(models.Model):      # 用户题库提交的代码
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default='')              # 用户名
    problem = models.ForeignKey(to=Problem, on_delete=models.CASCADE, default='')        # 题目编号
    content = models.TextField(blank=True)                                   # 提交代码
    runID = models.AutoField(primary_key=True)                               # 运行编号
    result = models.CharField(max_length=15, default='0', blank=True)         # 运行结果
    time = models.IntegerField(blank=True, default=0)                        # 运行时间
    memory = models.IntegerField(blank=True, default=0)                      # 运行内存
    language = models.CharField(default='C++', blank=True, max_length=9, choices=LANGUAGE_CHOICE)   # 语言
    subTime = models.DateTimeField(auto_now=True)                            # 提交时间

    def change_problem(self):
        problem = self.problem
        problem.submit_nums = problem.submit_nums+1
        if self.result == "正确":
            problem.ac_nums = problem.ac_nums+1
        problem.save()

    def __str__(self):
        return str(self.runID)


class test(models.Model):
    test = models.CharField(max_length=20)


