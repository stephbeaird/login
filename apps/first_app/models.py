from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator(self, postData):
        errors = []
        if len(postData['First_Name']) < 2 or  len(postData['Last_Name']) < 2:
            errors.append("First and Last must be 2 or more characters.")
        
        if not EMAIL_REGEX.match(postData['Email']):
            errors.append("Email is not valid.")
        
        if len(postData['Password']) < 8 or len(postData['Confirm_Password']) < 8:
            errors.append("Password must be 8 or more characters.")
        
        if postData['Password'] != postData['Confirm_Password']:
            errors.append("Passwords must match.")
        
        try:
            User.object.get(email=postData['email'])
            errors.append("Email already taken.")
        except:
            pass
        
        try:
            validate_email(postData['email'])
        except ValidationError as e:
            errors.append("Email must be in valid format.")
        else:
            print("Email worked!")
        
            if errors:
                return {'err_messages': errors}
        
            else:
                hash_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
                user = User.objects.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = hash_pw)        
                return {'new_user': user}

        # except:
        #     pass

    def login(self, postData):
        try:
            user = User.objects.get(email = postData['email'])
            if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                return {'logged_user': user}
            else:
                return {'err_messages': ['Email/Password invalid. Please try again.']}
        except:
            return {'err_messages': ['Email does not exist. Please register']}

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
            
    objects = UserManager()

