from rest_framework import serializers
from chat.models import Messages, Conversations
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from users.serializers import UserProfileSerializer, ShortUserProfileSerializer
from datetime import datetime


class ConversationSerializer(serializers.ModelSerializer):

    members = ShortUserProfileSerializer(many=True)

    class Meta:
        model = Conversations
        fields = '__all__'


class ResponseMessageListSerializer(serializers.ModelSerializer):
    
    sender_id = UserProfileSerializer()
    conversation_id = ConversationSerializer()

    class Meta:
        model = Messages
        fields = '__all__'


class RequestChatSerializer(serializers.Serializer):
    text = serializers.CharField()
    conversation_id = serializers.IntegerField(
        min_value=1)

    def create(self, validated_data):
        c = Conversations.objects.get(
                id=validated_data['conversation_id'])
        m = Messages(
            conversation_id=c,
            text=validated_data['text'],
            date=datetime.now(),
            sender_id=self.context['user']
        )
        m.save()
        return m

class RequestConversationSerializer(serializers.ModelSerializer):
    conversation_name = serializers.CharField()

    def create(self, validated_data):
        c = Conversations(
            conversation=validated_data['conversation_id'],
            member=validated_data['user_id']
        )
        c.save()
        return c
