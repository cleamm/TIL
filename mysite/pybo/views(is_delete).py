# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Question, Answer
# from django.utils import timezone
# # from pybo.forms import QuestionForm
# from .forms import QuestionForm
# from django.core.paginator import Paginator
# from django.http import HttpResponseNotAllowed
# from .forms import QuestionForm, AnswerForm
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# 아래는 직접 만듦
# @login_required(login_url='common:login')
# def answer_delete(request, answer_id):
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.user != answer.author:
#         messages.error(request, '삭제권한이 없습니다')
#         return redirect('pybo:detail', question_id=answer.question.id)
#     answer.delete()
#     return redirect('pybo:index')
# @login_required(login_url='common:login')
# def answer_delete(request, answer_id):
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.user != answer.author:
#         messages.error(request, '삭제권한이 없습니다')
#     else:
#         answer.delete()
#     return redirect('pybo:detail', question_id=answer.question.id)
#
# @login_required(login_url='common:login')
# def answer_modify(request, answer_id):
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.user != answer.author:
#         messages.error(request, '수정권한이 없습니다')
#         return redirect('pybo:detail', question_id=answer.question.id)
#     if request.method == "POST":
#         form = AnswerForm(request.POST, instance=answer)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.modify_date = timezone.now()
#             answer.save()
#             return redirect('pybo:detail', question_id=answer.question.id)
#     else:
#         form = AnswerForm(instance=answer)
#     context = {'answer': answer, 'form': form}
#     return render(request, 'pybo/answer_form.html', context)

# @login_required(login_url='common:login')
# def question_delete(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '삭제권한이 없습니다')
#         return redirect('pybo:detail', question_id=question.id)
#     question.delete()
#     return redirect('pybo:index')
#
# @login_required(login_url='common:login')
# def question_modify(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '수정 권한이 없습니다')
#         return redirect('pybo:detail', question_id=question.id)
#     if request.method == "POST":
#         form = QuestionForm(request.POST, instance=question)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.modify_date = timezone.now()  # 수정일시 저장
#             question.save()
#             return redirect('pybo:detail', question_id=question.id)
#     else:
#         form = QuestionForm(instance=question)
#     context = {'form': form}
#     return render(request, 'pybo/question_form.html', context)
#
# @login_required(login_url='common:login')
# def question_create(request):
#     if request.method == "POST": #post방식 -> 질문작성후 -> 저장하기
#         form=QuestionForm(request.POST)
#         if form.is_valid(): #폼에 값이 올바르게 저장되었다면
#             question=form.save(commit=False) #임시저장
#             question.author = request.user # 로그인되어 있는 계정 저장
#             question.create_date=timezone.now() #작성일자 저장
#             question.save() #실제 저장
#             return redirect('pybo:index')
# #저장
#     else:   #get방식(초기화면에서 '질문등록하기' 눌렀을때) -> 질문폼
#         form = QuestionForm()
#     return render(request, 'pybo/question_form.html',{'form': form})


##http://localhost:8000/pybo/answer/create/2/
# => question_id 에는 2가 전달됨
# => 답변 내용은 request 변수에 전달됨
# @login_required(login_url='common:login')
# def answer_create(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     if request.method == "POST":
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.author = request.user
#             answer.create_date = timezone.now()
#             answer.question = question
#             answer.save()
#             return redirect('pybo:detail', question_id=question.id)
#     else:
#         # return HttpResponseNotAllowed('Only POST is possible.')
#         form = AnswerForm()
#     context = {'question': question, 'form': form}
#     return render(request, 'pybo/question_detail.html', context)


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'pybo/question_detail.html', context)
#
# def index(request):
#     #요청 페이지가 있다면 페이지 번호를 저장하고, 요청 페이지가 없다면 1을 저장
#     # http://localhost:8000/pybo/?page=3  => page변수에 3이 저장
#     # http://localhost:8000/pybo =>  page변수에 1이 저장
#     page = request.GET.get('page', 1) #기본 요청 페이지 : 1
#     question_list = Question.objects.order_by('-create_date')
#     paginator=Paginator(question_list, 10) #페이지당 10개
#     page_obj=paginator.get_page(page) #요청 페이지(page)의 내용을 가져와서 page_obj에 저장
#     context = {'question_list': page_obj}
#     return render(request, 'pybo/question_list.html', context)












