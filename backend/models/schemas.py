from marshmallow import Schema, fields

class UserSchema(Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'date')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
