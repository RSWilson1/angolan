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
        return int(db.session.query(func.sum(PrescribingData.items).label('total_items')).scalar())


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
        return round(db.session.query(func.avg(PrescribingData.ACT_cost).label('Average ACT Cost')).scalar(), 2)

    def get_max_description(self):
        """Return the description with the max quantity prescription which is the BNF name"""
        return db.session.query(PrescribingData.BNF_name,
                                func.max(PrescribingData.quantity))[0][0]

    def get_max_percent_quantity(self):
        """Return the percentage the most prescribed prescription represents. Calculate the absolute total of all
        prescriptions. Round the percentage to 2 decimal places."""

        abs_total = int(db.session.query(func.sum(PrescribingData.quantity)).scalar())
        max_quantity = int(db.session.query(PrescribingData.BNF_name,
                                func.max(PrescribingData.quantity))[0][1])
        percentage = (max_quantity / abs_total) * 100
        return str(round(percentage, 2))

    def get_unique(self):
        """Return the number of unique prescriptions"""
        return int(db.session.query(func.count(
            PrescribingData.BNF_code.distinct()).label('sum_qty')).scalar())

    def get_total_infection_drugs(self):
        #all_inf_bnfs = db.session.query(PrescribingData).filter(PrescribingData.BNF_code.startswith("05%")).all()
        #total = len(all_inf_bnfs)
        subquery = db.session.query(PrescribingData).filter(
            PrescribingData.BNF_code.startswith("05%")).subquery()
        #total = db.session.query(func.sum(subquery.items)).first()[0]
        #query = db.session.query(func.sum(PrescribingData.items)).filter(PrescribingData.BNF_code.in_(subquery)).scalar()
        total = db.session.query(func.sum(PrescribingData.items)).filter(PrescribingData.BNF_code.startswith("05%")).scalar()
        return query

    def get_antiB_per(self):
        total = self.get_total_infection_drugs()
        #antibio_bnfs = db.session.query(func.sum(PrescribingData.quantity)).filter(PrescribingData.BNF_code.startswith("0501%")).all()
        #antibio_bnfs_per = (antibio_bnfs/total)*100
        #subquery = db.session.query(PrescribingData).filter(
        #    PrescribingData.BNF_code.startswith("0501%")).subquery()
        #query = db.session.query(func.sum(subquery.c.items)).scalar()
        #antibio_bnfs_per = (query/total)*100
        return total

    def get_antifungal_per(self):
        total = self.get_total_infection_drugs()
        #antifungal_bnfs = len(db.session.query(PrescribingData).filter(PrescribingData.BNF_code.startswith("0502%")).all())
        #antifungal_bnfs_per = (antifungal_bnfs/total)*100
        #return round(antifungal_bnfs_per, 2)
        subquery = db.session.query(PrescribingData).filter(
            PrescribingData.BNF_code.startswith("0502%")).subquery()
        query = db.session.query(func.sum(subquery.c.quantity)).scalar()
        antifungal_bnfs_per = (query/total)*100
        return round(antifungal_bnfs_per, 2)

    def get_antiviral_per(self):
        total = self.get_total_infection_drugs()
        #antiviral_bnfs = len(db.session.query(PrescribingData).filter(PrescribingData.BNF_code.startswith("0503%")).all())
        #antiviral_bnfs_per = (antiviral_bnfs/total)*100
        #return round(antiviral_bnfs_per, 2)
        subquery = db.session.query(PrescribingData).filter(
            PrescribingData.BNF_code.startswith("0503%")).subquery()
        query = db.session.query(func.sum(subquery.c.quantity)).scalar()
        antiviral_bnfs_per = (query/total)*100
        return round(antiviral_bnfs_per, 2)

    def get_antiproto_per(self):
        total = self.get_total_infection_drugs()
        #antiproto_bnfs = len(db.session.query(PrescribingData).filter(PrescribingData.BNF_code.startswith("0504%")).all())
        #antiproto_bnfs_per = (antiproto_bnfs/total)*100
        #return round(antiproto_bnfs_per, 2)
        subquery = db.session.query(PrescribingData).filter(
            PrescribingData.BNF_code.startswith("0504%")).subquery()
        query = db.session.query(func.sum(subquery.c.quantity)).scalar()
        antiproto_bnfs_per = (query/total)*100
        return round(antiproto_bnfs_per, 2)

    def get_anthelmintics_per(self):
        total = self.get_total_infection_drugs()
        #anthelmintics_bnfs = len(db.session.query(PrescribingData).filter(PrescribingData.BNF_code.startswith("0505%")).all())
        #anthelmintics_bnfs_per = (anthelmintics_bnfs/total)*100
        #return round(anthelmintics_bnfs_per, 2)
        subquery = db.session.query(PrescribingData).filter(
            PrescribingData.BNF_code.startswith("0505%")).subquery()
        query = db.session.query(func.sum(subquery.c.quantity)).scalar()
        antihelmintics_bnfs_per = (query/total)*100
        return round(antihelmintics_bnfs_per, 2)

    def get_total_inf_drugs_PCT(self):
        return db.session.query(PrescribingData).filter(
            PrescribingData.BNF_code.startswith("05%")).all().group_by(
                                                PrescribingData.PCT).all()