import re
import time
from datetime import datetime, timedelta

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework.views import APIView
from Issue.serializers import ProblemDataSerializer, ProblemSerializer
from Contest.serializers import *
from UserProfile.util import check_auth


def change_status(status_list):
    for item in status_list:
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


class GetContestPage(APIView):

    @staticmethod
    def get(request):  # 按（id|名字|状态）查询第page页的竞赛列表
        data = {'status': 200, 'msg': '成功获取竞赛列表'}
        contest_status = request.GET.get('contest_status', None)

        contest = Match.objects.filter().order_by('-id')
        a = datetime.now()
        if contest_status is not None and contest_status != '4':
            if contest_status == '1':
                contest = contest.filter(startTime__gt=a)
            elif contest_status == '2':
                contest = contest.extra(
                    where=["startTime < '%s' and '%s' < datetime(startTime, '+'||howLong||' minute', 'localtime')" % (a, a)])
            elif contest_status == '3':
                contest = contest.extra(where=["datetime(startTime, '+'||howLong||' minute', 'localtime') < '%s'" % a])
        is_login, user = check_auth(request)
        paginator_of_contest_all = Paginator(contest, 10)
        page_num = request.GET.get('page', 1)
        paginator_of_contest_all = paginator_of_contest_all.page(page_num)
        paginator_of_contest_all = paginator_of_contest_all.object_list
        paginator_of_contest_all = get_data(obj=paginator_of_contest_all, serializer=MatchSerializer,
                                          dataList=['owner', 'info', 'id', 'startTime', 'registerNum', 'howLong',
                                                    'matchName'],
                                          context={'request': request}, many=True)
        data.update({
            'contest': paginator_of_contest_all,
            'now_page': page_num,
            })
        return JsonResponse(data)


def is_accepted(match, user, problems):
    exec_problems = []
    for problem in problems:
        # 判断当前用户的提交记录中 是否存在已经正确的提交 有则在信息中添加一条字段记录状态
        if MatchSubmit.objects.filter(match__id=match.id, user__username=user.username,
                                      problem__no=problem['problem']['no'], result='1').exists():
            problem['is_ac'] = True
        # 此处表示 有提交 但是并未正确
        elif MatchSubmit.objects.filter(match__id=match.id, user__username=user.username,
                                        problem__no=problem['problem']['no']).exists():
            problem['is_ac'] = False
        exec_problems.append(problem)
    return exec_problems


# 以下为展示比赛内容

class ContestShowContent(APIView):
    @staticmethod
    def get(request, match_id):  # 比赛包含的题目
        data = {'status': 200, 'msg': '成功获取比赛题目列表', 'data': {}}
        try:
            match = Match.objects.get(id=match_id)
        except ObjectDoesNotExist:
            data.update({'status': 400, 'msg': '竞赛不存在'})
            return JsonResponse(data)
        except MultipleObjectsReturned:
            data.update({'status': 400, 'msg': '竞赛错误'})
            return JsonResponse(data)

        is_login, user = check_auth(request)
        t = match
        match = get_data(obj=match, serializer=MatchSerializer, dataList=[])
        if match['status'] == 1:
            data.update({'is_start': False, 'contest': match})
        elif match['status'] > 1:
            problems = get_data(obj=t.matchinclude_set.all(), serializer=MatchIncludeSerializer, dataList=[],
                                many=True)
            exec_problems = is_accepted(t, user, problems)  # 包含对于当前用户是否已经通过
            data.update({'is_start': True, 'contest': match, 'problems': exec_problems})
        return JsonResponse(data)


# 以下为展示比赛题目, 此函数是由Ajax提交的
class ContestGetProblems(APIView):

    @staticmethod
    def get(request, match_id):  # 获取题目的提交人数&通过人数&通过率&用户的通过情况
        data = {'status': 200, 'msg': '成功获取比赛题目列表'}
        try:
            match = Match.objects.get(id=match_id)
            # 尝试获取比赛，获取不到就不做处理
        except ObjectDoesNotExist:
            data.update({'status': 404, 'msg': '竞赛不存在'})
            return JsonResponse(data)
        problems = get_data(obj=match.matchinclude_set.all(), serializer=MatchIncludeSerializer, dataList=[], many=True)
        is_login, user = check_auth(request)
        exec_problems = is_accepted(match, user, problems)  # 包含对于当前用户是否已经通过
        data.update({
            'problems': exec_problems
        })
        return JsonResponse(data)


# 以下为展示比赛排名, 此函数是由Ajax提交的

class ContestGetRank(APIView):

    @staticmethod
    def get(request, match_id):
        data = {'status': 200, 'msg': '获取成功', }
        try:
            match = Match.objects.get(id=match_id)  # 获得这场比赛的所有信息
        except ObjectDoesNotExist:
            data.update({'msg': 'Error: No such contest!'})
            return JsonResponse(data)
        ranks = get_data(match.matchrank_set.all(), serializer=MatchRankSerializer, dataList=[], many=True)

        data.update({
            'ranks': ranks
        })
        return JsonResponse(data)
        # 从比赛中获取题目列表
        # users = MatchRegister.objects.filter(match__id=contest.id)  # 从注册比赛的所有用户中查找用户
        # if not users.exists():
        #     return HttpResponse(json.dumps({'Error': {'content': 'No user registration contest!'}}))
        # return HttpResponse(json.dumps({'Success': {'rankList': []}}))


# 以下为展示比赛状态, 此函数是由Ajax提交的

class ContestGetStatus(APIView):

    @staticmethod
    def get(request, match_id):
        data = {'status': 200, 'msg': '获取成功', 'data': {}}
        try:
            contest = Match.objects.get(id=match_id)
        except ObjectDoesNotExist:
            data.update({'msg': 'Error: No such contest!'})
            return JsonResponse(data)

        # 从提交GET 提交请求中去获取筛选条件
        submit_username = request.GET.get('username', '')
        page_num = request.GET.get('page', 1)
        judge_states = request.GET.get('judge_states', '')
        language = request.GET.get('language', '')
        problem_id = request.GET.get('problem_id', '')

        query_criteria = {'match__id': contest.id}  # 创建一个多条件查询字典

        # 创建对用户名进行正则匹配的条件
        if submit_username != '':
            query_criteria['user__username__iregex'] = submit_username

        # 创建对题目状态尽行筛选的条件
        if judge_states != '' and judge_states != '0':
            query_criteria['result'] = judge_states

        # 创建对提交语言进行筛选的条件
        if language != '' and language != 'All':  # 当值为C++时不知道为什么传不过来，推测可能是无法解析
            if language == 'Csrc':
                query_criteria['language'] = 'C++'
            else:
                query_criteria['language'] = language

        # 创建对题目的筛选条件
        if problem_id != '' and problem_id != '0':
            try:
                query_criteria['problem__no'] = int(problem_id)
            except ValueError:
                pass

        matchSubmit_list = MatchSubmit.objects.filter(**query_criteria).order_by('-runID')

        # 分页处理
        try:
            page_num = int(page_num)
        except ValueError:
            page_num = 1
        dataList = ["match", "user", "problem", "runID", "result", "time", "memory", "language", "subTime", ]
        paginator_of_status = Paginator(matchSubmit_list, 20)
        matchSubmit_list = paginator_of_status.page(page_num).object_list
        matchSubmit_list = get_data(obj=matchSubmit_list, serializer=MatchSubmitSerializer, dataList=dataList,
                                    many=True)

        data.update({
            'statusList': matchSubmit_list, 'pages': paginator_of_status.num_pages,
        })
        return JsonResponse(data)


class ContestProblemPage(APIView):
    @staticmethod
    def get(request, match_id, problem_id):
        try:
            problem = MatchInclude.objects.get(match__id=match_id, problem__no=problem_id)
        except ObjectDoesNotExist:
            return JsonResponse({

            })

        data = {}
        data.update({
            'problem': MatchIncludeSerializer(problem).data
        })
        data['problem'].update({
            'problem': ProblemSerializer(problem.problem).data
        })

        return JsonResponse(data)

    @staticmethod
    def post(request, match_id, problem_id):
        data = {'status': 200, 'msg': '提交成功'}
        is_login, user = check_auth(request)
        if not is_login:
            data.update({'status': 401, 'msg': '未登录'})
            return JsonResponse(data)
        contest = Match.objects.filter(id=match_id)
        if contest.exists():
            contest = contest[0]
        else:
            data.update({'status': 400, 'msg': '竞赛不存在'})
            return JsonResponse(data)
        # 获取时间 进行是否还在比赛的判定
        # time1 = contest.startTime.replace(tzinfo=None)  # 比赛开始时间
        # time2 = datetime.now()  # 当前系统时间
        # time3 = time1 + timedelta(minutes=int(contest.howLong))  # 比赛结束时间
        #
        # # 如果还未开始， 就重定向到比赛开始页面
        # if time1 > time2:
        #     data.update({'status': 400, 'msg': 'Error： contest not start'})
        #     return JsonResponse(data)
        # elif time2 > time3:
        #     # 如果比赛已经结束， 向前端ajax提交处返回错误信息
        #     data.update({'status': 400, 'msg': 'Error： contest is over'})
        #     return JsonResponse(data)

        # 对于非法提交， 进行判断该用户是否注册了比赛， 没有就重定向到比赛列表页面
        # if not MatchRegister.objects.filter(match__id=match_id, user__username=user.username).exists():
        #     data.update({'status': 400, 'msg': '未注册比赛'})
        #     return JsonResponse(data)

        # 对于防止恶意提交空语言， 进行判断提交语言是否符合规定
        language = request.data['language']
        print(language)
        if not re.search('[C|C++|Java]', language):
            language = 'C'

        # 获取提交代码
        content = request.data['code']

        if content != '':
            # 创建提交记录
            problem = Problem.objects.filter(no=problem_id)
            if problem.exists():
                problem = problem[0]
            else:
                data.update({'msg': '题目错误'})
                return JsonResponse(data)
            statuses = MatchSubmit.objects.create(
                match=contest,
                user=user,
                problem=problem,
                content=content,
                result="0",
                language=language,
            )
            flag = 1
            # 进行循环查询题目结果
            while statuses.result == '0':
                time.sleep(1)  # 如果还在判题，那就等一秒以后重新查询，直到结果出来后，再返回数据
                if flag > 10:
                    time.sleep(1)
                    if flag > 35:
                        data.update({'status': 400, 'msg': 'Error： Server busy, try again later'})
                        return JsonResponse(data)
                statuses = MatchSubmit.objects.get(runID=statuses.runID)
                flag += 1
            if not MatchSubmit.objects.filter(
                    match__id=match_id, user__id=user.id, problem__no=problem_id, result='1').exists():
                rank = MatchRank.objects.get(match__id=match_id, user__id=user.id)
                problem = MatchInclude.objects.get(match__id=match_id, problem_id=problem_id)
                for i in rank.rank:
                    if i['problem_no'] == problem.no:
                        if statuses.result == '1':
                            i['is_ac'] = True
                            i['useTime'] = (statuses.subTime - contest.startTime).total_seconds() * 1000
                        else:
                            i['wrongTime'] += 1
            data["data"].update({'result': statuses.result})
            return JsonResponse(data)
        else:
            # 对于空代码提交， 向ajax返回错误信息
            data.update({'status': 400, 'msg': 'Error： Your code is empty!'})
            return JsonResponse(data)


class GetContestSubmitCode(APIView):
    @staticmethod
    def get(request, match_id, run_id):
        try:
            submit = MatchSubmit.objects.get(match__id=match_id, runID=run_id)
        except ObjectDoesNotExist:
            return JsonResponse({
                'msg': 'error'
            }, status=404)
        return JsonResponse({
            'submit': MatchSubmitSerializer(submit).data
        })


# 注册比赛

class RegisterContest(APIView):

    @staticmethod
    def get(request):
        contest_Id = request.GET.get('contest_Id', '')
        contest = Match.objects.get(id=contest_Id)
        data = {'status': 200, 'msg': '报名成功'}
        is_Login, user = check_auth()
        if is_Login:
            matchRank = MatchRank(match=contest, user=user)
            matchRank.save()

            return JsonResponse(data)
        else:
            return
