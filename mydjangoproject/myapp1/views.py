from django.shortcuts import render
from myapp1.models import Worker

def index_page(request):

    all_worker = Worker.objects.all()


    #for i in all_worker:
        #print(f'Фамилия: {i.second_name}, Имя: {i.name}, Зарплата: {i.salary}, ID: {i.id}')

    return render(request, 'index.html', context={'data': all_worker})
