from ekamapp import db
from ekamapp.models import Event, Post, User

def get_user_by_event(event_id):
    try:
        users = User.query.filter_by(event_id=event_id).all()
        if not users:
            raise ValueError("No users found for the given event ID.")
        return users
    except Exception as e:
        raise e
    
def get_all_users():
    try:
        users = User.query.all()
        if not users:
            raise ValueError("No users found.")
        return users
    except Exception as e:
        raise e
    
def get_event_by_id(post_id):
    try:
        post = Post.query.get_or_404(post_id)
        return post
    except Exception as e:
        raise e

def delete_event(post):
    try:
        db.session.delete(post)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def update_event(post, title, content):
    try:
        post.title = title
        post.content = content
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def create_event(event):
    try:
        event = Event()
        db.session.add(event)
        db.session.commit()
        return event
    except Exception as e:
        db.session.rollback()
        raise e
    
def get_all_users():
    try:
        users = User.query.all()
        if not users:
            raise ValueError("No users found.")
        return users
    except Exception as e:
        raise e
def get_post_by_id(post_id):
    try:
        post = Post.query.get_or_404(post_id)
        return post
    except Exception as e:
        raise e

def delete_post(post):
    try:
        db.session.delete(post)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def update_post(post, title, content):
    try:
        post.title = title
        post.content = content
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def create_post(title, multifiles, video_url, content, author):
    try:
        post = Post(title=title, multifiles=multifiles, video_url=video_url, content=content, author=author)
        db.session.add(post)
        db.session.commit()
        return post
    except Exception as e:
        db.session.rollback()
        raise e
