from django.shortcuts import render
import os
# Create your views here.


def index(request):
    if request.method =='POST':
        code = request.POST['code']
        open('data/user_code.py', 'w').write(code)
        os.system('python data/user_code.py 2> data/error.txt')

        f = open('data/error.txt', 'r').read()
        if len(f) == 0:
            os.system('python data/user_code.py > output.txt')
            f = open('output.txt', 'r').read()
        return render(request, 'index.html', {'code': code, 'output':f})

    code = open('data/source_code.py', 'r').read()
    return render(request, 'index.html', {'code':code})
