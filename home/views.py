from django.shortcuts import render
import os
# Create your views here.


def index(request):
    if request.method =='POST':
        code = request.POST['code']
        with open('data/user_code.py', 'w') as f: f.write(code)
        os.system('python data/user_code.py > data/output.txt 2>&1')

        with open('data/output.txt', 'r') as f: content = f.read()
        return render(request, 'index.html', {'code': code, 'output':content})

    with open('data/source_code.py', 'r') as f: content = f.read()
    return render(request, 'index.html', {'code':content})
