import time

from django.http import HttpResponse

from TestModel.models import Test


# 数据库操作
def testdb(request):
    test = Test(name='hello_django', create_time=time.time())
    test.save()
    return HttpResponse("<p>数据添加成功！</p>")
