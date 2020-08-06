from tortoise import fields, models


class Todo(models.Model):
    id = fields.IntField(pk=True)
    content = fields.TextField()
    timestamp_created = fields.DatetimeField(auto_now_add=True)
    timestamp_updated = fields.DatetimeField(auto_now=True)
