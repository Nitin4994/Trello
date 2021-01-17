from django.shortcuts import render

# Create your views here.

from user.views import user_loginout
from user.models import User
from board.models import Board


from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
def paggination_records(req, all_records):     #pagination
    page = req.GET.get('page')
    paginator = Paginator(all_records, 5)  # 12-->show 5 records only
    try:
        boards = paginator.page(page)  # 1
    except PageNotAnInteger:
        boards = paginator.page(1)
    except EmptyPage:
        boards = paginator.page(paginator.num_pages)
    return boards

def board(req):
    if not req.session.has_key('email'):
        return user_loginout(req)

    user = User.objects.filter(email=req.session['email']).first()
    boards = Board.objects.filter(userref=user.id).all()
    return render(req, 'board.html',
                  {'user': user,
                   'boards':paggination_records(req,boards),
                   'msg': '',
                   'error': ''})

def board_save(req):
    if not req.session.has_key('email'):
        return user_loginout(req)
    user = User.objects.filter(email=req.session['email']).first()

    if req.method=='POST':
        formdata = req.POST
        boardname = formdata['boardName']

        boards = Board.objects.filter(userref=user.id).all()
        if boardname == "":
            return render(req, 'board.html',
                          {'user': user,
                           'boards': paggination_records(req,boards),
                           'msg': '',
                           'error': 'Invalid credentials...'})
        bordinfo = Board(boardName=boardname)
        bordinfo.userref=user
        bordinfo.save()

        return render(req, 'board.html',
                      {'user': user,
                       'boards': paggination_records(req,boards),
                       'msg': 'Board Saved Successfully...',
                       'error': ''})
    else:

        user = User.objects.filter(email=req.session['email']).first()
        boards = Board.objects.filter(userref=user.id).all()
        return render(req, 'board.html',
                      {'user': user,
                       'boards': paggination_records(req,boards),
                       'msg': '',
                       'error': ''})

def board_delete(req,bid):
    if not req.session.has_key('email'):
        return user_loginout(req)
    user = User.objects.filter(email=req.session['email']).first()


    board = Board.objects.filter(id=bid).first()
    if board:
        board.delete()
        boards = Board.objects.filter(userref=user.id).all()
        return render(req, 'board.html',
                      {'user': user,
                       'boards': paggination_records(req, boards),
                       'msg': 'Board Deleted Successfully...',
                       'error': ''})
    else:
        boards = Board.objects.filter(userref=user.id).all()
        return render(req, 'board.html',
                      {'user': user,
                       'boards': paggination_records(req, boards),
                       'msg': '',
                       'error': 'Invalid Board Id...'})

