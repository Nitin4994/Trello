from django.shortcuts import render

# Create your views here.

from user.views import user_loginout
from user.models import User
from board.models import Board
from categorie.models import Categories
from task.models import Task
from board.views import paggination_records

def task_save(req):
    if not req.session.has_key('email'):
        return user_loginout(req)
    user = User.objects.filter(email=req.session['email']).first()

    if req.method=='POST':
        formdata = req.POST
        cateid = formdata['cateid']
        tasktitle = formdata['tasktitle']
        description = formdata['description']
        print("cateid",cateid)

        categorie = Categories.objects.filter(id=cateid).first()
        print(categorie.bordref.id)
        board = Board.objects.filter(id=categorie.bordref.id).first()
        categories = Categories.objects.filter(bordref=board.id).all()
        #tasks = Task.objects.all()
        if tasktitle == "" or description == "":
            cate_dict = {}
            categories = Categories.objects.filter(bordref=board.id).all()
            for cate in categories:
                task_list = []
                tasks = Task.objects.filter(cateref=cate.id).all()
                # print(type(tasks))
                for task in tasks:
                    task_list.append(task)
                cate_dict.update({cate: task_list})
            # print(cate_dict)

            return render(req, 'categorie.html',
                          {'user': user,
                           'board': board,
                           'categories': categories,
                           'cate_dict': cate_dict,
                           #'tasks':tasks,
                           'msg': '',
                           'error': 'Invalid Credentials...'})

        taskinfo = Task(taskTitle=tasktitle,description=description)
        taskinfo.cateref = categorie
        taskinfo.save()

        cate_dict = {}
        categories = Categories.objects.filter(bordref=board.id).all()
        for cate in categories:
            task_list = []
            tasks = Task.objects.filter(cateref=cate.id).all()
            # print(type(tasks))
            for task in tasks:
                task_list.append(task)
            cate_dict.update({cate: task_list})
        # print(cate_dict)

        return render(req, 'categorie.html',
                      {'user': user,
                       'board': board,
                       'categories': categories,
                       'cate_dict': cate_dict,
                       'msg': 'Task Saved Successfully...',
                       'error': ''})
    else:
        boards = Board.objects.filter(userref=user.id).all()
        return render(req, 'board.html',
                      {'user': user,
                       'boards': paggination_records(req, boards),
                       'msg': '',
                       'error': 'Invalid Board Id...'})


def task_delete(req,tid):
    if not req.session.has_key('email'):
        return user_loginout(req)
    user = User.objects.filter(email=req.session['email']).first()



    task = Task.objects.filter(id=tid).first()

    if task:
        print(task.cateref.id)
        categorie = Categories.objects.filter(id=task.cateref.id).first()
        board = Board.objects.filter(id=categorie.bordref.id).first()

        task.delete()

        cate_dict = {}
        categories = Categories.objects.filter(bordref=board.id).all()
        for cate in categories:
            task_list = []
            tasks = Task.objects.filter(cateref=cate.id).all()
            # print(type(tasks))
            for task in tasks:
                task_list.append(task)
            cate_dict.update({cate: task_list})
        # print(cate_dict)

        return render(req, 'categorie.html',
                      {'user': user,
                       'board': board,
                       'categories': categories,
                       'cate_dict': cate_dict,
                       'msg': 'Task Deleted Successfully...',
                       'error': ''})
    else:
        boards = Board.objects.filter(userref=user.id).all()
        return render(req, 'board.html',
                      {'user': user,
                       'boards': paggination_records(req, boards),
                       'msg': '',
                       'error': 'Invalid Board Id...'})


def task_move(req):
    if not req.session.has_key('email'):
        return user_loginout(req)
    user = User.objects.filter(email=req.session['email']).first()

    if req.method=='POST':
        formdata = req.POST
        cateid = formdata['moveCateid']
        taskid = formdata['taskid']

        print("cateid",cateid)
        print("taskid",taskid)

        if cateid == "" or taskid == "":
            boards = Board.objects.filter(userref=user.id).all()
            return render(req, 'board.html',
                          {'user': user,
                           'boards': paggination_records(req, boards),
                           'msg': '',
                           'error': 'Invalid Credentials...'})

        task = Task.objects.filter(id=taskid).first()
        categorie = Categories.objects.filter(id=cateid).first()

        board = Board.objects.filter(id=categorie.bordref.id).first()
        #categories = Categories.objects.filter(bordref=board.id).all()

        if task:
            task.cateref=categorie
            task.save()

        cate_dict = {}
        categories = Categories.objects.filter(bordref=board.id).all()
        for cate in categories:
            task_list = []
            tasks = Task.objects.filter(cateref=cate.id).all()
            # print(type(tasks))
            for task in tasks:
                task_list.append(task)
            cate_dict.update({cate: task_list})
        # print(cate_dict)

        return render(req, 'categorie.html',
                      {'user': user,
                       'board': board,
                       'categories': categories,
                       'cate_dict': cate_dict,
                       'msg': 'Task Moved Successfully...',
                       'error': ''})
    else:
        boards = Board.objects.filter(userref=user.id).all()
        return render(req, 'board.html',
                      {'user': user,
                       'boards': paggination_records(req, boards),
                       'msg': '',
                       'error': 'Invalid Credentials...'})