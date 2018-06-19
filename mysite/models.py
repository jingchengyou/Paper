from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30, default=None)
    email = models.EmailField(max_length=30, unique=True, default=None)
    telephone = models.CharField(max_length=15, unique=True)  # 填入时需要验证合法性
    nickname = models.CharField(max_length=30, unique=True)  # 填入时需要验证合理性，如敏感词、字母开头等
    address = models.CharField(max_length=100)
    register_time = models.DateTimeField(auto_now_add=True)  # 作者注册系统时间


#  产生上传文件的路径
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Group(models.Model):
    # first_person = models.ForeignKey(Author, on_delete=models.CASCADE)  # 团队创始人
    create_time = models.DateTimeField(auto_now_add=True)
    # 多对多关系
    author = models.ManyToManyField(Author)


class Novel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)  # 小说初次创建时间
    summary = models.TextField(max_length=1000)
    title = models.CharField(max_length=30, unique=True)
    # 外键
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Chapter(models.Model):
    title = models.CharField(max_length=30)
    upload = models.FileField(upload_to=user_directory_path)
    publish_time = models.DateTimeField(auto_now_add=True)  # 文件初次上传时间
    # 外键（多对一）
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)


# Comment主要指读者对某个章节的评论
class Comment(models.Model):
    content = models.TextField(max_length=500)
    create_time = models.DateTimeField(auto_now_add=True)  # 评论产生时间
    # 外键
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)


# Session主要指作者之间对话的信息内容
class Session(models.Model):
    content = models.TextField(max_length=500)
    create_time = models.DateTimeField(auto_now_add=True)  # 会话产生时间
    # 外键
    author = models.ForeignKey(Author, on_delete=models.CASCADE)








