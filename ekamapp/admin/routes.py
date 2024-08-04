from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from ekamapp import bcrypt
from ekamapp.models import User
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')
import uuid
import requests.cookies
from ekamapp import app,db
from twilio.twiml.messaging_response import MessagingResponse 
from flask import jsonify, render_template,url_for,flash,redirect,request,make_response,session
from ekamapp.models import  User   
@admin_bp.route("/debug_cookies")
def debug_cookies():
    user_id = request.cookies.get('user_id')
    user_name = request.cookies.get('user_name')
    return f'user_id: {user_id}, user_name: {user_name}'


@admin_bp.route("/getusers")
def get_all_users():
    users = User.query.all()
    for user in users:
        print(f"User ID: {user.id}, Username: {user.name}, gender: {user.gender}, whatsapp: {user.whatsapp}")
    return jsonify([user.to_dict() for user in users])

@admin_bp.route('/')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    return render_template('admin/dashboard.html')

@admin_bp.route('/users')
@login_required
def admin_users():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    users = User.query.all()
    return render_template('admin/users.html', users=users)