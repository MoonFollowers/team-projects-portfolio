from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class GomunityTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token['id'] = user.id
        token['username'] = user.nickname
        
        return token
        
