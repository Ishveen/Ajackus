from rest_framework import serializers
from myapi.models import content, contentcreater,customuser


class UserProfileSerializer(serializers.ModelSerializer): 
    '''This serialization class is for contentcreater to be used while creating new customuser'''  
    class Meta:
        model = contentcreater
        fields = ['fullname', 'phone', 'pincode','user_id']
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)
    
    class Meta:
        model = customuser
        fields = ('pk','email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = customuser(**validated_data)
        user.set_password(password)
        user.save()
        contentcreater.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.fullname = profile_data.get('fullname', profile.fullname)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.address = profile_data.get('address', profile.address)
        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.pincode = profile_data.get('zip', profile.zip)
        profile.save()

        return instance


class contentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = content
        fields = '__all__'
                

  