from django.shortcuts import render

# Create your views here.

from user.views import user_loginout
from user.models import User
from board.models import Board
from board.views import paggination_records
from categorie.models import Categories
from task.models import Task

def categorie(req,bid):
    if not req.session.has_key('email'):
        return user_loginout(req)
    user = User.objects.filter(email=req.session['email']).first()

    board = Board.objects.filter(id=bid).first()
    #tasks = Task.objects.all()
    #print(tasks)


    if board:
        #print(board.id)
        cate_dict = {}
        categories = Categories.objects.filter(bordref=board.id).all()
        for cate in categories:
            task_list = []
            tasks = Task.objects.filter(cateref=cate.id).all()
            #print(type(tasks))
            for task in tasks:
                task_list.append(task)
            cate_dict.update({cate:task_list})
        #print(cate_dict)
        return render(req, 'categorie.html',
                      {'user': user,
                       'board': board,
                       'categories':categories,
                       'cate_dict':cate_dict,
                       #'tasks':tasks,
                       'msg': '',
                       'error': ''})
    else:
        boards = Board.objects.filter(userref=user.id).all()
        return render(req, 'board.html',
                      {'user': user,
                       'boards': paggination_records(req, boards),
                       'msg': '',
                       'error': 'Invalid Board Id...'})

def categorie_save(req):
    if not req.session.has_key('email'):
        return user_loginout(req)
    user = User.objects.filter(email=req.session['email']).first()

    if req.method=='POST':
        formdata = req.POST
        boardid = formdata['boardid']
        categorie = formdata['categorie']

        board = Board.objects.filter(id=boardid).first()
        categories = Categories.objects.filter(bordref=board.id).all()
        print(board.boardName)
        if categorie == "":

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
                           'msg': '',
                           'error': 'Invalid Categorie...'})
        categorieinfo = Categories(cateName=categorie)
        categorieinfo.bordref = board
        categorieinfo.save()

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
                       'msg': 'Categorie Saved Successfully...',
                       'error': ''})
    else:
        boards = Board.objects.filter(userref=user.id).all()
        return render(req, 'board.html',
                      {'user': user,
                       'boards': paggination_records(req, boards),
                       'msg': '',
                       'error': ''})

def categorie_delete(req,cid):
    if not req.session.has_key('email'):
        return user_loginout(req)
    user = User.objects.filter(email=req.session['email']).first()

    categorie = Categories.objects.filter(id=cid).first()
    if categorie:
        board = Board.objects.filter(id=categorie.bordref.id).first()


        categorie.delete()

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
                       'msg': 'Categorie Deleted Successfully...',
                       'error': ''})
    else:
        boards = Board.objects.filter(userref=user.id).all()
        return render(req, 'board.html',
                      {'user': user,
                       'boards': paggination_records(req, boards),
                       'msg': '',
                       'error': 'Invalid Categorie Id...'})

