from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)
		self.load_model('User')
 
	def index(self):
		#get request
		#load all products
		return self.load_view('index.html')

	def show(self):
		
		return self.load_view('show/show.html')

	def edit(self):
		#get request
		#find one and render edit view
		return self.load_view('edit.html')

	def new(self):
		#get request
		#renders the create page
		return self.load_view('new.html')

	def create(self):
		for like in request.form:
			self.models['User'].insert_likes(like)
		session['matches'] = self.models['User'].matches(1,2)
		print session['matches']
		#post request
		#creates a record in the DB
		return "banana"

	def update(self,id):
		#post request
		#updates a record in the DB
		return redirect('/show/id')

	def destroy(self,id): 
		#post request
		#destroys a record in the DB
		return redirect('/')


