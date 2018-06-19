from django.shortcuts import render, redirect
from .forms import RegisterForm, NovelForm
from .models import Author, Novel, Group

# 设置全局变量，比如作者姓名。使用户登录后系统始终显示用户姓名
session_message = {
    "session_name": None,  # 防止用户未登录时弹框
}


# story_list = {
#     "圣墟": "彼岸花开，天下的点点滴滴的点点滴滴dddddddddddddddddddddddddddddddddddddddddddddd的",
#     "斗罗大陆": "唐三魂兽的点点滴滴大道",
#     "斗破苍穹": "萧炎什么了的",
#               }
#
# story_summary = ["圣墟", "堕落", "全职法师"]
#
# session_message['story_list'] = story_list
# session_message['story_summary'] = story_summary


def get_story():
    novel_list = Novel.objects.order_by("-create_time")
    # title_list为最新发表的小说名单，即story数据库逆序，暂定为等待合作的小说
    summary_list = [novel.title for novel in novel_list]

    novel_list_2 = Novel.objects.order_by("create_time")
    # title_list为阅读最多的小说，即story数据库顺序
    title_list = [novel.title for novel in novel_list_2]

    if len(summary_list) > 12:
        summary_list = summary_list[0:12]
    if len(title_list) > 12:
        title_list = title_list[0:12]
    print(summary_list)
    print(title_list)

    session_message['story_list'] = title_list
    session_message['story_summary'] = summary_list
    return


def index(request):
    get_story()
    return render(request, 'mysite/index.html', session_message)


def login(request):
    get_story()
    if request.method == 'POST':
        info = request.POST
        if Author.objects.filter(email=info['email']) and Author.objects.filter(password=info['password']):
            session_message['session_name'] = info["email"]
            return render(request, 'mysite/main.html', session_message)
        elif not Author.objects.filter(email=info['email']):
            return render(request, "mysite/index.html", {'errorMessage': "邮箱未注册，请注册！"})
        else:
            return render(request, "mysite/index.html", {'errorMessage': "密码出错！"})
    else:
        return render(request, "mysite/index.html", {'errorMessage': "表单出错！"})


def to_register(request):
    print("投")
    return render(request, 'mysite/register.html', session_message)


def getAuthorInfo(request):
    get_story()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            author = Author()
            author.name = form.cleaned_data['name']
            author.email = form.cleaned_data['email']
            author.password = form.cleaned_data['password']
            author.telephone = form.cleaned_data['telephone']
            author.nickname = form.cleaned_data['nickname']
            author.address = form.cleaned_data['address']
            author.save()
            session_message['session_name'] = form.cleaned_data['email']

            # session_name（全局变量：用户名）；story_list（阅读最多小说），story_summary（等待合作小说），
            return render(request, 'mysite/main.html', session_message)
    else:
        return render(request, "mysite/index.html", {'errorMessage': "注册页面表单出错啦！"})


def booksummary(request, title):
    novel = Novel.objects.get(title=title)
    session_message["title"] = novel.title
    session_message["summary"] = novel.summary
    return render(request, "mysite/booksummary.html", session_message)


catalog_list = ["第一章", "第二章", "第三章", "第四章", "第五章", "第六章"]


def catalog(request):
    session_message['catalog_list'] = catalog_list
    return render(request, "mysite/chapter.html", session_message)


def content(request):
    return render(request, "mysite/chapterdetail.html", session_message)


def person_info(request, num):
    if session_message["session_name"]:
        session_message["target"] = num
        return render(request, "mysite/person.html", session_message)
    else:
        get_story()
        session_message['no_yet'] = "no_yet"
        return render(request, "mysite/index.html", session_message)


# 将当前用户添加进团队
def new_group():
    # 新生成一个组
    group = Group()
    group.save()

    email = session_message['session_name']
    print(email)
    author = Author.objects.get(email=email)
    print(author)
    group.author.add(author)
    group.save()
    print("成功")
    return group


def push_success(request):
    if request.method == "POST":
        form = NovelForm(request.POST)
        print("到这儿了")
        print(form)
        print(form.cleaned_data)
        if form.is_valid():
            novel = Novel()
            novel.title = form.cleaned_data['title']
            novel.summary = form.cleaned_data['summary']
            print(session_message['session_name'])
            group = new_group()  # 创立新组，并将当前用户加入新组
            novel.group = group
            novel.save()
            session_message['title'] = form.cleaned_data['title']
            session_message['summary'] = form.cleaned_data['summary']
            return render(request, 'mysite/booksummary.html', session_message)


# 根据title，查找group，然后根据session_message中的用户信息（session_name）查找数据库中的用户信息，最后，用
# add方法将用户加入到该group中
def add_group(request, title):
    session_message['catalog_list'] = catalog_list
    return render(request, 'mysite/chapter.html', session_message)
