import datetime

from rest_framework import serializers
from TokenCreator.models import TokenManagement





####Try inheriet from django base user
#User (inherit from base user)
#Token #cached in db
#call model method through serializer

#call __str__

class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = TokenManagement
        fields = "__all__"


    def get_customer(self, instance):
        return datetime.datetime.now().year - 1983
