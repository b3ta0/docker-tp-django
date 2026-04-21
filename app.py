"""
Django 最小化项目，可直接启动
访问会显示 Django 欢迎页
"""
import sys
from django.conf import settings
from django.urls import path
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application

# 关闭调试上线时改为 False
settings.configure(
    DEBUG=True,
    SECRET_KEY="test-secret-key-123456",
    ALLOWED_HOSTS=["*"],  # 关键：允许所有IP访问
    ROOT_URLCONF=__name__,
    MIDDLEWARE=[
        "django.middleware.common.CommonMiddleware",
    ],
)

def home(request):
    return HttpResponse("""
        <h1>✅ Django 部署成功！</h1>
        <p>服务运行正常</p>
    """)

urlpatterns = [
    path("", home),
]

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
