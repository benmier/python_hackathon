from system.core.model import Model
from flask import Flask, flash, redirect, render_template, session

class User(Model):
	def __init__(self):
		super(User, self).__init__()
  
	def insert_likes(self,like):
		like = like.replace("'","''")
		like = like.replace("/","")
		like = like.encode('utf8')
		# print like
		like_id = self.db.query_db("SELECT like_id FROM facebook_likes WHERE name='{}' ORDER BY like_id LIMIT 1".format(like))
		if like_id==[]:
			query = "INSERT IGNORE INTO facebook_likes (name) VALUES ('{}')".format(like)
			self.db.query_db(query)
		like_id = self.db.query_db("SELECT like_id FROM facebook_likes WHERE name='{}' ORDER BY like_id LIMIT 1".format(like))
		user_like_id = self.db.query_db("SELECT user_like_ids FROM user_has_likes WHERE user_like_ids='{}' AND like_user_ids='{}'".format(like_id[0]['like_id'],2))
		if user_like_id==[]:
			query2 = "INSERT INTO user_has_likes (like_user_ids,user_like_ids) VALUES ('{}','{}')".format(2,like_id[0]['like_id'])
			return self.db.query_db(query2)
		else:
			return "banana"

	def matches(self,user1_id,user2_id):
		all_matches = []
		query = ("SELECT * FROM user_has_likes R1, user_has_likes R2,facebook_likes \
									WHERE R1.like_user_ids!=R2.like_user_ids AND like_id=R1.user_like_ids \
									AND R1.user_like_ids=R2.user_like_ids \
									AND R1.like_user_ids=%s \
									AND R2.like_user_ids=%s \
									GROUP BY R2.user_like_ids")
		data = [user1_id,user2_id]
		matched_likes = self.db.query_db(query,data)
		for i in matched_likes:
			all_matches.append(i['name'])
		return matched_likes

 	def all_users(self):
 		return self.db.query_db("SELECT * FROM users")