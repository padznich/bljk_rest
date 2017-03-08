# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import random

from bljk.models import Summary, Detail, Description


def fill_summary(_ident=4, _days=31):

    for j in range(1, _ident):
        for i in range(1, _days):

            s = Summary()
            s.date = datetime.now() - timedelta(days=i)
            s.game = "Blackjack Multihand"
            s.min = random.randint(10, 100)
            s.plays = random.randint(10, 100)
            s.wagered = random.randint(10, 100) / \
                        float(random.randint(10, 100))
            s.winnings = random.randint(10, 100) / \
                         float(random.randint(10, 100))
            s.pending = random.randint(10, 100) / \
                        float(random.randint(10, 100))
            s.identifier = str(j)

            s.save()


def fill_detail(_ident=4, _summ_id=91):

    for i in range(1, _summ_id):
        for j in range(1, _ident):
            for k in range(5):

                d = Detail()
                d.time = datetime.now() - \
                         timedelta(minutes=random.randint(1, 60))
                d.game_id = random.randint(1000, 10000)
                d.wagered = random.randint(10, 100) / \
                            float(random.randint(10, 100))
                d.result = random.randint(10, 100) / \
                             float(random.randint(10, 100))
                d.summary_id = i
                d.identifier = str(j)

                d.save()


def fill_description(_rows=6):

    for j in range(1, 2701):
        for i in range(_rows):

            d = Description()

            d.hand = "Hand"
            d.summ = random.randint(10, 21)
            d.cards = "A"
            d.action = "spam"
            d.rate = random.randint(10, 100) / \
                     float(random.randint(10, 100))
            d.win = random.randint(10, 100) / \
                     float(random.randint(10, 100))
            d.detail_id = j

            d.save()


def handler():

    fill_summary()
    fill_detail()
    fill_description()
