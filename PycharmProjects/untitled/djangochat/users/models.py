from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=10)
    birthday = models.DateField(null=True)
    number_of_friends = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Conversations(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Users)
    is_group = models.BooleanField()

    def __str__(self):
        return self.name


# class ConversationMembers(models.Model):
#     conversation_id = models.ForeignKey(
#         Conversations, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(
#         Users, on_delete=models.DO_NOTHING)

#     def __str__(self):
#         return "%s, %s" % (
#             self.conversation_id.name,
#             self.user_id.first_name
#         )

class Messages(models.Model):
    sender_id = models.ForeignKey(
        Users,
        on_delete=models.CASCADE)
    conversation_id = models.ForeignKey(
        Conversations,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return "%s (%s): %s" % (
            self.sender_id.first_name,
            self.conversation_id.name,
            self.text
        )

# class Users(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=10)
#     birthday = models.DateField(null=True)
#     number_of_friends = models.IntegerField()

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name


# class Message(models.Model):
#     sender = models.ForeignKey(
#         Users,
#         on_delete=models.CASCADE,
#         related_name="blahblah"
#     )
#     receiver = models.ForeignKey(
#         Users,
#         on_delete=models.CASCADE,
#         related_name="blahblah2"
#     )
#     text = models.TextField()
#     date = models.DateField()

#     def __str__(self):
#         return "%s -> %s: %s" % (
#             self.sender,
#             self.receiver,
#             self.text
#         )