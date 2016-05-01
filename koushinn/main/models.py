# -*- coding: utf-8 -*-

from datetime import datetime
from koushinn import db
from koushinn.utils import CRUDMixin


class PushRecord(db.Model, CRUDMixin):
    __tablename__ = 'push_records'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.Text(), index=True)
    is_auto = db.Column(db.Boolean(), default=True)
    created_time = db.Column(db.DateTime(), default=datetime.utcnow)
    pushed_time = db.Column(db.DateTime(), nullable=True, default=None)
    delete = db.Column(db.Boolean(), default=False)
    is_success = db.Column(db.Boolean(), default=True)


class WaitingList(db.Model, CRUDMixin):
    __tablename__ = 'wating_list'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.Text(), index=True, unique=True)
    image = db.Column(db.String(64))
    plan_time = db.Column(db.DateTime(), nullable=True, default=None)
    created_time = db.Column(db.DateTime(), default=datetime.utcnow)
    cutting_weight = db.Column(db.SmallInteger(), default=0)
