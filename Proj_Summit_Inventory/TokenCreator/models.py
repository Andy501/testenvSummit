from django.db import models
from django.contrib.auth.models import User
from Inventory_API.models import Product

# Create your models here.

###inherit from base user.
class TokenManagement(models.Model):


    #token_capture
    #procduct(inheriting from Inventory_API.products)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #token_capture = models.CharField(max_length=500)

    # class Meta:
    #     permissions = [
    #         ("change_task_status", "Can change the status of tasks"),
    #         ("close_task", "Can remove a task by setting its status as closed"),
    #     ]

#    user.has_perm('app.close_task')

    #def tokenflipper(self):
        #do_something =
        #token_capture.save(do_something)


    def __str__(self):
        return self.user