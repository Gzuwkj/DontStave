import re
import time

from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework import serializers

from Issue.models import Problem
from django.http import JsonResponse
from Issue.serializers import *
from apps.util import get_data

# 获取用户的问题的通过状态
from UserProfile.util import check_auth


def is_accepted(user, problems):
    exec_problems = []
    for problem in problems:
        if ProblemSubmit.objects.filter(user__id=user.id, problem__no=problem["no"], result='1').exists():
            problem['is_ac'] = True
        elif ProblemSubmit.objects.filter(user__id=user.id, problem__no=problem["no"]).exists():
            problem['is_ac'] = False
        exec_problems.append(problem)
    return exec_problems


# 获取问题列表
class GetProblemPage(APIView):
    @staticmethod
    def get(request):  # 按（id|名字|类型|来源）查询第page页的问题列表
        problem_Id_Name = request.GET.get('problem_Id_Name', '')
        problem_Source = request.GET.get('problem_Source', 'All')
        algorithm_Type = request.GET.get('algorithm_Type', 'All')
        query_Criteria = {'probAuthority': '公开'}  # 创建一个多条件查询字典
        if problem_Id_Name != '':
            try:  # 尝试将参数作为数值处理，并当作id搜索，如果不行，就转化为name进行搜索
                query_Criteria['no'] = int(problem_Id_Name)
            except ValueError:
                query_Criteria['title__iregex'] = '.*'.join(problem_Id_Name)
        if problem_Source != '' and problem_Source != 'All':
            query_Criteria['probSource'] = problem_Source
        if algorithm_Type != '' and algorithm_Type != 'All':
            query_Criteria['classification'] = algorithm_Type
        problems = Problem.objects.filter(**query_Criteria).order_by('-no')
        # 分页处理

        dataList = ["no", "title", 'ac_nums', 'submit_nums']
        paginator_of_problems_all = Paginator(problems, 20)
        page_num = request.GET.get('page', 1)
        paginator_of_problems_all = paginator_of_problems_all.page(page_num)
        paginator_of_problems_all = paginator_of_problems_all.object_list
        paginator_of_problems_all = get_data(obj=paginator_of_problems_all, serializer=ProblemSerializer,
                                             dataList=dataList, many=True)

        is_login, user = check_auth(request)
        exec_problems = is_accepted(user, paginator_of_problems_all)
        # 将这些数据返回到前端，这样便于进行多条件过滤
        data = {'status': 200, 'msg': '已获取所有问题'}
        data.update({'problems': exec_problems,
                     'now_page': page_num, 'problem_id_name': problem_Id_Name,
                     'problem_source': problem_Source, 'algorithm_type': algorithm_Type})

        return JsonResponse(data)


# 获取单个问题或修改单个问题
class GetProblem(APIView):

    def get(self, request, prob_id):
        data = {'status': 200, 'msg': '成功获取题目', 'data': {}}
        try:
            # 获取问题
            prob_no = str(prob_id)

            problem = Problem.objects.get(no=prob_no, probAuthority='公开')

            data["data"].update({"problem": problem.get_problem()})
            print(prob_no)

            code = ''
            language = 'C'

            # 如果用户登录 则获取用户最新一次提交代码
            is_Login, user = check_auth(request._request)
            try:
                problem_Submit = ProblemSubmit.objects.filter(problem__no=prob_no, user__id=user.id).last()
                language = problem_Submit.language
                code = problem_Submit.content
            except:
                pass
            data["data"].update({"language": language, "code": code})
        except:
            data['msg'] = '题目不存在'
            data['status'] = 400
        return JsonResponse(data=data)

    def post(self, request, prob_id):
        data = {'status': 200, 'msg': '修改成功', 'data': {}}
        try:
            problem = Problem.objects.get(no=prob_id)
            problem.updata_problem(request.data)
        except:
            data['msg'] = '问题不存在'
            data['status'] = 400

        return JsonResponse(data=data)


# 创建问题
class CreateProblem(APIView):
    def post(self):
        data = {'status': 200, 'msg': '已获取所有问题', 'data': {}}

        # 身份验证


def change_status(status_List):  # 提交状态
    for item in status_List:
        if item.result == '0':
            item.result = 'Queueing'
        elif item.result == '1':
            item.result = 'Accepted'
        elif item.result == '2':
            item.result = 'Presentation Error'
        elif item.result == '3':
            item.result = 'Wrong Answer'
        elif item.result == '4':
            item.result = 'Time Limit Exceeded'
        elif item.result == '5':
            item.result = 'Memory Limit Exceeded'
        elif item.result == '6':
            item.result = 'Output Limit Exceeded'
        elif item.result == '7':
            item.result = 'Runtime Error'
        elif item.result == '8':
            item.result = 'Compilation Error'
        elif item.result == '9':
            item.result = 'Compile Output Limit'


# 获取提交列表或者
class GetProblemSubmitPage(APIView):
    @staticmethod
    def get(request):  # 按（提交人|提交结果|提交语言|提交问题）查询第page页的提交列表
        submit_username = request.GET.get('submit_UserName', '')
        judge_states = request.GET.get('judege_States', '')
        language = request.GET.get('language', '')
        problem_id = request.GET.get('problem_Id', '')
        page_num = request.GET.get('page', 1)
        query_Criteria = {}  # 创建一个多条件查询字典
        if submit_username != '':
            query_Criteria['user__username__iregex'] = submit_username  # 用户名不区分大小写
        if judge_states != '' and judge_states != '0':
            query_Criteria['result'] = judge_states
        if language != '' and language != 'All':  # 当值为C++时不知道为什么传不过来，推测可能是无法解析
            if language == 'Csrc':
                query_Criteria['language'] = 'C++'
            else:
                query_Criteria['language'] = language
        if problem_id != '':
            try:
                query_Criteria['problem__no'] = int(problem_id)
            except ValueError:
                pass
        submit_list = ProblemSubmit.objects.filter(**query_Criteria).order_by('-runID')
        # change_status(submit_list)

        # 分页
        dataList = ["runID", "result", "time", "memory", "language", "subTime", "user", "problem"]
        paginator_of_submit_list_all = Paginator(submit_list, 25)  # 分页
        paginator_of_submit_list_all = paginator_of_submit_list_all.page(page_num)
        paginator_of_submit_list_all = paginator_of_submit_list_all.object_list
        paginator_of_submit_list_all = get_data(obj=paginator_of_submit_list_all, serializer=ProblemSubmitSerializer,
                                                dataList=dataList, many=True)

        data = {'status': 200, 'msg': '获取成功', 'statusList': paginator_of_submit_list_all, 'now_page': page_num,
                'submit_user_name': submit_username, 'judge_states': judge_states,
                'language': language, 'problem_id': problem_id}
        return JsonResponse(data)


# 获取单个提交
class GetProblemSubmit(APIView):
    @staticmethod
    def get(request):
        data = {'status': 200, 'msg': '获取成功', 'data': {}}
        is_login, user = check_auth(request)
        if not is_login:
            data["data"].update({'status': 400, 'msg': '未登录', })
            return JsonResponse(data)
        username = request.GET.get("username", "")
        if username != user.username:
            data["data"].update({'status': 400, 'msg': '不同用户', })
            return JsonResponse(data)
        problem_Submit_Id = request.GET.get("problem_Submit_Id", "")
        print(problem_Submit_Id)
        problem_Submit = ProblemSubmit.objects.get(runID=problem_Submit_Id)
        problem_Submit = get_data(obj=problem_Submit, serializer=ProblemSubmitSerializer)

        data["data"] = {"problem_Submit": problem_Submit}
        return JsonResponse(data)


class CreateProblemSubmit(APIView):
    def post(self, request):  # 创一份ProblemSubmit
        data = {'status': 200, 'msg': '提交成功', 'data': {}}
        is_Login, user = check_auth(request._request)
        if is_Login == False:
            return JsonResponse(data.update({'status': 400, 'msg': '未登录'}))
        if request._request.is_ajax():

            prob_no = request.POST.get('prob_no', '')
            try:
                prob_no = int(prob_no)
            except:
                data['status'] = 400
                data['msg'] = 'Error: Unknown problem submit'
                return JsonResponse(data)
            if 1000 > prob_no or prob_no > Problem.objects.last().no:
                data['status'] = 400
                data['msg'] = 'Error: Unknown problem submit'
                return JsonResponse(data)
            # 对于防止恶意提交空语言， 进行判断提交语言是否符合规定
            language = request.POST.get('language', 'C')
            if not re.search('[C|C++|Java|Python]', language):
                language = 'C'

            # 获取提交代码
            content = request.POST.get('editor', '')

            if content != '':
                prob = Problem.objects.get(no=prob_no)
                statuses = ProblemSubmit.objects.create(
                    user=user,
                    problem=prob,
                    content=content,
                    result="0",
                    language=language,
                )
                prob.submit_nums += 1
                flag = 0
                while statuses.result == '0':
                    time.sleep(0.7)  # 如果还在判题，那就等0.7秒以后重新查询，直到结果出来后，再返回数据
                    if flag >= 10:
                        time.sleep(0.6)
                        if flag > 35:
                            data['status'] = 400
                            data['msg'] = 'Error: Server busy, try again later'
                            return JsonResponse(data)
                    statuses = ProblemSubmit.objects.filter(problem__no=prob_no, user__id=user.id).last()
                    flag += 1
                if statuses.result == '1':
                    prob.ac_nums += 1
                prob.ratio = round(float(prob.ac_nums / prob.submit_nums), 3) * 100
                prob.save()
                data['msg'] = 'Success: ' + str(statuses.result)
                return JsonResponse(data)
            else:
                # 对于空代码提交， 向ajax返回错误信息
                data['status'] = 400
                data['msg'] = 'Error: Your code is empty!'
                return JsonResponse(data)
