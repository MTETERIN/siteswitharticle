from django.http import HttpResponse
from django.template import loader
import csv
from .models import Recommendations

def rowcreate(request):
    Recommendations.objects.all().delete()
    with open('Startdata.csv') as f:
        reader = csv.reader(f)
        index = 0
        for row in reader:
            index += 1
            if index <= 76:
                continue
            else:
                tools, created = Recommendations.objects.get_or_create(
                    creators_title=row[0],
                    link=row[1],
                )
            if index == 88:
                break;

    template = loader.get_template('article/index.html')
    context = {
        'latest_question_list': [],
    }
    return HttpResponse(template.render(context, request))