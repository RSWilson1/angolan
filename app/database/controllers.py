"""
NAME:          database\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          17/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Contains the Database class that contains all the methods used for accessing the database
"""

from numpy import average
from sqlalchemy.sql import func
from sqlalchemy.sql import desc
from flask import Blueprint

from app import db
from app.database.models import PrescribingData, PracticeData

database = Blueprint('dbutils', __name__, url_prefix='/dbutils')

class Database:
    """Class for managing database queries."""
    def get_total_number_items(self):
        """Return the total number of prescribed items."""
        return int(db.session.query(func.sum(PrescribingData.items).label('total_items')).first()[0])


    def get_prescribed_items_per_pct(self):
        """Return the total items per PCT."""
        return db.session.query(func.sum(PrescribingData.items).label('item_sum')).group_by(PrescribingData.PCT).all()


    def get_distinct_pcts(self):
        """Return the distinct PCT codes."""
        return db.session.query(PrescribingData.PCT).distinct().all()


    def get_n_data_for_PCT(self, pct, n):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData).filter(PrescribingData.PCT == pct).limit(n).all()


    def get_avg_ACT_cost(self):
        """
        Return the Average ACT cost for all drugs over all practices.
        The average cost of a Prescription drug for the NHS.
        """
        return int(db.session.query(func.avg(PrescribingData.ACT_cost).label('Average ACT Cost')).first()[0])
        #db.session.query(PrescribingData.ACT_cost.avg().label('Average ACT Cost'))


    def get_max_quant(self):
        """
        This aims to get the sum of the quanity over all practices, they are then ordered
        and the drug with the highest quantity is returned. This would be the most presribed in the UK.
        """
        return db.session.query(PrescribingData.BNF_name, \
                PrescribingData.BNF_code, func.sum(PrescribingData.quantity))\
                .group_by(PrescribingData.BNF_code).order_by(func.sum(PrescribingData.quantity)\
                .desc()).limit(1).all()[0][0]

    def get_percentage(self):
        total = db.session.query(func.sum(PrescribingData.quantity)).first()[0]
        max_quant = db.session.query(PrescribingData.BNF_name, \
                PrescribingData.BNF_code, func.sum(PrescribingData.quantity))\
                .group_by(PrescribingData.BNF_code).order_by(func.sum(PrescribingData.quantity)\
                .desc()).limit(1).all()[0][2]
        return round((max_quant/total)*100)

