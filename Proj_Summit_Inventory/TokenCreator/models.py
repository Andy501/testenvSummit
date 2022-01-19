from django.db import models
from django.contrib.auth.models import User
from Inventory_API.models import Product


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.



#
#
#
# ###inherit from base user.
# class TokenManagement(models.Model):
#     # for user in User.objects.all():
#     #     Token.objects.get_or_create(user=user)
#
#     #token_capture
#     #procduct(inheriting from Inventory_API.products)
#     logged_users = models.OneToOneField(User, on_delete=models.CASCADE)
#     #token_capture = models.CharField(max_length=500)
#
#     # class Meta:
#     #     permissions = [
#     #         ("change_task_status", "Can change the status of tasks"),
#     #         ("close_task", "Can remove a task by setting its status as closed"),
#     #     ]
#
# #    user.has_perm('app.close_task')
#
#     #def tokenflipper(self):
#         #do_something =
#         #token_capture.save(do_something)
#
#
#     def __str__(self):
#         return self.user
#
#
#
#     # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
#     # def create_auth_token(sender, instance=None, created=False, **kwargs):
#     #     if created:
#     #         Token.objects.create(user=instance)
#     #

