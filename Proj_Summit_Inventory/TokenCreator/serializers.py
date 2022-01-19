import datetime

from rest_framework import serializers





####Try inheriet from django base user
#User (inherit from base user)
#Token #cached in db
#call model method through serializer

#call __str__

# class TokenSerializer(serializers.ModelSerializer):
#     token_grab = serializers.SerializerMethodField()
#
#     class Meta:
#         model = TokenManagement
#         fields = "__all__"
#
#
#     def get_token(self, instance):
#         print(datetime.datetime.now().year - 1983)
#         return datetime.datetime.now().year - 1983
