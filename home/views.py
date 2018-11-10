from django.shortcuts import render
import os
from ilio import read, write
# Create your views here.


def index(request):
    if request.method =='POST':
        code = request.POST['code']
        write('data/user_code.py', code)
        os.system('python data/user_code.py > data/output.txt 2>&1')

        content = read('data/output.txt')
        return render(request, 'index.html', {'code': code, 'output':content})

    with open('data/source_code.py', 'r') as f: content = f.read()
    return render(request, 'index.html', {'code':content})
