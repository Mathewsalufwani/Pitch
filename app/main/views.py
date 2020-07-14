from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment,Upvote,Downvote
from .forms import Pitch_Form, Update_Profile,CommentsForm
from .. import db, photos
from flask_login import login_required, current_user

#Views
@main.route('/')
def index():
    '''
    View root page function that returns index page and its data
    '''

    title = 'Home - Welcome to The Pitches of The Century'
    return render_template('index.html', title = title)