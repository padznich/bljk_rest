# -*- coding: utf-8 -*-

from flask_peewee.db import Database, ForeignKeyField
from flask_peewee.db import IntegerField, CharField, DateField, FloatField
from flask_peewee.admin import ModelAdmin

from app import app


db = Database(app)


class Summary(db.Model):

    date = DateField()
    game = CharField()
    min = IntegerField()
    plays = IntegerField()
    wagered = FloatField()
    winnings = FloatField()
    pending = FloatField()
    identifier = CharField()

    def __unicode__(self):
        return "%s: %s" % (self.id, self.date)


class Detail(db.Model):

    game_id = CharField()
    time = DateField()
    wagered = FloatField()
    result = FloatField()
    summary_id = ForeignKeyField(Summary)
    identifier = CharField()


class Description(db.Model):

    hand = CharField()
    summ = IntegerField()
    cards = CharField()
    action = CharField()
    rate = FloatField()
    win = FloatField()
    detail_id = ForeignKeyField(Detail)


class SummaryAdmin(ModelAdmin):

    columns = (
        "id",
       "date",
       "game",
       "min",
       "plays",
       "wagered",
       "winnings",
       "pending",
       "identifier"
    )


class DetailAdmin(ModelAdmin):

    columns = (
        "id",
        "time",
        "wagered",
        "result",
        "summary_id",
        "identifier"
    )
    foreign_key_lookups = {'summary_id': 'summary'}



class DescriptionAdmin(ModelAdmin):

    columns = (
        "id",
        "hand",
        "summ",
        "cards",
        "action",
        "rate",
        "win",
        "detail_id"
    )
