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
        return round(db.session.query(func.avg(PrescribingData.ACT_cost).label('Average ACT Cost')).first()[0], 2)

    def get_max_description(self):
        """Return the description with the max quantity prescription which is the BNF name"""
        return db.session.query(PrescribingData.BNF_name,
                                func.max(PrescribingData.quantity))[0][0]

    def get_max_percent_quantity(self):
        """Return the percentage the most prescribed prescription represents. Calculate the absolut total of all
        prescriptions. Round the percentage to 2 decimal places."""

        abs_total = int(db.session.query(func.sum(PrescribingData.quantity)).first()[0])
        max_quantity = int(db.session.query(PrescribingData.BNF_name,
                                func.max(PrescribingData.quantity))[0][1])
        percentage = (max_quantity / abs_total) * 100
        return str(round(percentage, 2))

    def get_unique(self):
        """Return the number of unique prescriptions"""
        # return db.session.query(PrescribingData.BNF_code).distinct().all()
        return int(db.session.query(func.count(PrescribingData.BNF_code.distinct()).label('sum_qty')).first()[0])
        # return db.session.query(func.count(distinct(PrescribingData.BNF_code)).label("sum distinct").first()[0])
