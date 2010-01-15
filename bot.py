from django.core.management import setup_environ
import settings
setup_environ(settings)

from trivia.models import *
a = Question.objects.get(question__icontains="baddog")
print a.answer
