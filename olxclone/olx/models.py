from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Advertisement(models.Model):

    CATEGORY_LIST=(

        ('Electronics','Electronics'),
        ('Furniture','Furniture'),
        ('Vehicles','Vehicles'),
        ('Properties','Properties'),
        ('Stationary','Stationary'),
        ('Fashion','Fashion'),
        ('Other','Other')

    )

    title=models.CharField(max_length=15)

    description=models.CharField(max_length=100)

    category=models.CharField(max_length=15,choices=CATEGORY_LIST)

    item_type=models.CharField(max_length=30)

    price=models.IntegerField()

    image=models.FileField()#When referencing in html, refer it as advertisement_object.image.url



    posted_on=models.DateTimeField(default=datetime.now())

    interested_count=models.IntegerField(default=0)

    my_user=models.ForeignKey(User,on_delete=models.CASCADE)


class ChatBox(models.Model):

    receiver=models.ForeignKey(User,on_delete=models.CASCADE)

    advt=models.ForeignKey(Advertisement,on_delete=models.CASCADE)

    pass

class Messages(models.Model):



    message_text=models.TextField(max_length=300)

    message_time=models.DateTimeField(default=datetime.now())

    #message_from=models.ForeignKey(User,on_delete=models.CASCADE)

    #sender_name=models.TextField(max_length=100)#To be extracted from the User model.

    sender=models.ForeignKey(User,on_delete=models.CASCADE)

    chat_box=models.ForeignKey(ChatBox,on_delete=models.CASCADE)


    pass

