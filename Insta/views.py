from django.views.generic import TemplateView   # 告诉页面从django自带的views里面的generic views去导入TemplateView

class HelloWorld(TemplateView):
    template_name = 'test.html'







