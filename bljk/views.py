# -*- coding: utf-8 -*-

from flask_peewee.rest import RestAPI
from flask_peewee.admin import Admin
from flask_peewee.auth import Auth

from app import app
from models import Summary, Detail, Description, db
from models import SummaryAdmin, DetailAdmin, DescriptionAdmin


auth = Auth(app, db)

# REST API
api = RestAPI(app)
api.register(Summary)
api.register(Detail)
api.register(Description)
api.setup()

# REST ADMIN
admin = Admin(app, auth)
admin.register(Summary, SummaryAdmin)
admin.register(Detail, DetailAdmin)
admin.register(Description, DescriptionAdmin)
admin.setup()


if __name__ == "__main__":
    auth.User.create_table(fail_silently=True)
    admin = auth.User(
        username='admin',
        email='',
        admin=True,
        active=True
    )
    admin.set_password('admin')
    admin.save()

    # Summary.create_table(fail_silently=True)
    # Detail.create_table(fail_silently=True)
    # Description.create_table(fail_silently=True)
