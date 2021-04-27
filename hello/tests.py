from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from .apps import HelloConfig
from website import settings

from .views import index, about


class AppTest(TestCase):

    def test_app_should_be_hello(self):
        self.assertEqual(HelloConfig.name, 'hello', "Приложение должно называться hello")


class HomePageTest(TestCase):

    def test_index_route(self):
        """  
        Добавить привязки путей / и /hello к представлению views.index
        в файлах urls.py и /hello/urls.py
        """
        root = resolve('/')
        self.assertEqual(root.func, index)
        hello = resolve('/hello/')
        self.assertEqual(hello.func, index)

    def test_html_in_index(self):
        """
        Создайть функцию представления с именем index в файле views.py, который должен
        возвращать HttpResponse с валидным html
        """
        request = HttpRequest()
        response = index(request)
        content = response.content.decode("utf-8")
        self.assertRegex(content, r'<!doctype\s+html>', msg="Должен быть задан doctype")
        self.assertRegex(content, r'<title>[^<]*</title>', msg="Должен быть задан тег title")
        self.assertRegex(content, r'<body>[\s\S]*?</body>', msg="Должен быть задан тег body")
        self.assertRegex(content, r'<html>[\s\S]+?</html>', msg="Должен быть тег html")

    def test_title_in_index(self):
        """
        Создайть функцию представления с именем index в файле views.py, который должен
        возвращать HttpResponse с заголовком (title) "Учим django"
        """
        request = HttpRequest()
        response = index(request)
        content = response.content.decode("utf-8")
        self.assertRegex(content, r'<title>\s*Учим django\s*</title>',
                         msg="title должен содержать текст Учим django")

    def test_h1_in_index(self):
        """
        Создайть функцию представления с именем index в файле views.py, который должен
        возвращать HttpResponse с заголовком (title) "Учим django"
        """
        request = HttpRequest()
        response = index(request)
        content = response.content.decode("utf-8")
        self.assertRegex(content, r'<h1>\s*Добро пожаловать\s*</h1>',
                         msg="Должен быть задан заголовок h1")

    def test_link_to_about(self):
        """
        Добавить гипертекстовую ссылку (тег a) на страницу about в HttpResponse представления index
        """
        request = HttpRequest()
        response = index(request)
        content = response.content.decode("utf-8")
        self.assertRegex(content, r'<a\s+href=["\']/hello/about/?["\']\s*>[^<]+</a>',
                         msg="Должна быть гипертекстовая ссылка на страницу about")


class AboutPageTest(TestCase):

    def test_about_route(self):
        """
        Привязать это представление к /hello/about в файле /hello/urls.py
        """
        found = resolve('/hello/about/')
        self.assertEqual(found.func, about)

    def test_html_in_about(self):
        """
        Создать второй метод представления about, который должен возвращать HttpResponse с
        Вашим резюме. Добавить заголовок (title) О нас
        """
        request = HttpRequest()
        response = about(request)
        content = response.content.decode("utf-8")
        self.assertRegex(content, r'<!doctype\s+html>', msg="Должен быть задан doctype")
        self.assertRegex(content, r'<title>[^<]*</title>', msg="Должен быть задан тег title")
        self.assertRegex(content, r'<body>[\s\S]*?</body>', msg="Должен быть задан тег body")
        self.assertRegex(content, r'<html>[\s\S]+?</html>', msg="Должен быть задан тег html")

    def test_title_in_about(self):
        """
        Создайть функцию представления с именем index в файле views.py, который должен
        возвращать HttpResponse с заголовком (title) "О нас"
        """
        request = HttpRequest()
        response = about(request)
        content = response.content.decode("utf-8")
        self.assertRegex(content, r'<title>\s*О\s+нас\s*</title>',
                         msg="title должен содержать текст О нас")

    def test_link_about_to_index(self):
        """
        В HttpResponse представления about добавить гипертекстовую ссылку На главную,
        на страницу index
        """
        request = HttpRequest()
        response = about(request)
        content = response.content.decode("utf-8")
        self.assertRegex(content, r'<a\s+href=["\']/hello/?["\']>[^<]+</a>',
                         msg="Должна быть ссылка на страницу /hello")
