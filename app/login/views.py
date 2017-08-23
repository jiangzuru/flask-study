from . import login
from flask import render_template, flash
from .forms import LoginForm

@login.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit() and form.validate():
		return form.email.data
	return render_template('/login/login.html', form=form)
