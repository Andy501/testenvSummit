from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    qty = models.IntegerField()
    in_stock = models.BooleanField(default=False)
    delete_now  = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name


    # def soft_delete(self):
    #     self.delete_ = True
    #     self.save()


    class Meta:
        abstract = False

class TokenizedPermission(models.Model):
    token_capture = models.TextField()
    token_updated_time = models.TimeField()
    token_life = models.IntegerField() #will not accept entry for token 10 minutes old or more.



    # def token_life_time(self):
    #     token_time = self.updated_time - time.now()  ####need import clock.
    #     #if time <0 or greater than 10 request a new token.
    #     print(token_time)
    #     self.token_life.save(token_time)