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
        """Generate the total number of items prescribed for infections.
        This uses the bnf code starting with 05 for infections.
        """
        total = db.session.query(func.sum(PrescribingData.items)).filter(
            PrescribingData.BNF_code.startswith("05%")).scalar()
        return total

    def get_antiB_per(self):
        """Generate the % Antibiotics prescribed of all infections treatments.
        This uses the bnf code starting with 0501 for infections.
        """
        total = self.get_total_infection_drugs()
        query_antibio = db.session.query(func.sum(PrescribingData.items)).filter(
            PrescribingData.BNF_code.startswith("0501%")).scalar()
        antibio_bnfs_per = (query_antibio/total)*100
        return round(antibio_bnfs_per, 2)

    def get_antifungal_per(self):
        """Generate the % antifungal prescribed of all infections treatments.
        This uses the bnf code starting with 0502 for infections.
        """
        total = self.get_total_infection_drugs()
        query_antifungal = db.session.query(func.sum(PrescribingData.items)).filter(
            PrescribingData.BNF_code.startswith("0502%")).scalar()
        antifungal_bnfs_per = (query_antifungal/total)*100
        return round(antifungal_bnfs_per, 2)

    def get_antiviral_per(self):
        """Generate the % antiviral prescribed of all infections treatments.
        This uses the bnf code starting with 0503 for infections.
        """
        total = self.get_total_infection_drugs()
        query_antiviral = db.session.query(func.sum(PrescribingData.items)).filter(
        PrescribingData.BNF_code.startswith("0503%")).scalar()
        antiviral_bnfs_per = (query_antiviral/total)*100
        return round(antiviral_bnfs_per, 2)

    def get_antiproto_per(self):
        """Generate the % antiprotozoals prescribed of all infections treatments.
        This uses the bnf code starting with 0504 for infections.
        """
        total = self.get_total_infection_drugs()
        query_antiproto = db.session.query(func.sum(PrescribingData.items)).filter(
        PrescribingData.BNF_code.startswith("0504%")).scalar()
        antiproto_bnfs_per = (query_antiproto/total)*100
        return round(antiproto_bnfs_per, 2)

    def get_anthelmintics_per(self):
        """Generate the % anthelmintics prescribed of all infections treatments.
        This uses the bnf code starting with 0505 for infections.
        """
        total = self.get_total_infection_drugs()
        query_anthelmintics = db.session.query(func.sum(PrescribingData.items)).filter(
        PrescribingData.BNF_code.startswith("0505%")).scalar()
        antihelmintics_bnfs_per = (query_anthelmintics/total)*100
        return round(antihelmintics_bnfs_per, 2)

    def get_total_inf_drugs_PCT(self):
        return db.session.query(PrescribingData).filter(
            PrescribingData.BNF_code.startswith("05%")).all().group_by(
                                                PrescribingData.PCT).all()