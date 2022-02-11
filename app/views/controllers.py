"""
NAME:          views\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          18/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Views module. Renders HTML pages and passes in associated data to render on the
               dashboard.
"""

from flask import Blueprint, render_template, request
from app.database.controllers import Database

views = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# get the database class
db_mod = Database()

# Set the route and accepted methods
@views.route('/home/', methods=['GET', 'POST'])
def home():
    """Render the home page of the dashboard passing in data to populate dashboard."""
    pcts = [r[0] for r in db_mod.get_distinct_pcts()]

    if request.method == 'POST':
        # if selecting PCT for table, update based on user choice
        form = request.form
        selected_pct_data = db_mod.get_n_data_for_PCT(str(form['pct-option']), 5)

        selected_pct_bnf_data = db_mod.get_bnf_data_for_PCT(str(form['pct-option']))
    else:
        # pick a default PCT to show
        selected_pct_data = db_mod.get_n_data_for_PCT(str(pcts[0]), 5)
        selected_pct_bnf_data = db_mod.get_bnf_data_for_PCT(str(pcts[0]))


    # prepare data
    bar_data = generate_barchart_data()
    bar_values = bar_data[0]
    bar_labels = bar_data[1]
    tile_data_items = generate_data_for_tiles()

    # render the HTML page passing in relevant data
    return render_template('dashboard/index.html', tile_data=tile_data_items,
                           pct={'data': bar_values, 'labels': bar_labels},
                           pct_list=pcts, pct_data=selected_pct_data,
                           pct_bnf_data=selected_pct_bnf_data)

def generate_data_for_tiles():
    """Generate the data for the four home page titles."""
    return [db_mod.get_total_number_items(), db_mod.get_avg_ACT_cost(),
            db_mod.get_max_description(), db_mod.get_max_percent_quantity(),
            db_mod.get_unique(), db_mod.get_total_infection_drugs(),
            db_mod.get_antiB_per(), db_mod.get_antifungal_per(),
            db_mod.get_antiviral_per(), db_mod.get_antiproto_per(),
            db_mod.get_anthelmintics_per()]

def generate_barchart_data():
    """Generate the data needed to populate the barchart."""
    data_values = db_mod.get_prescribed_items_per_pct()
    pct_codes = db_mod.get_distinct_pcts()

    # convert into lists and return
    data_values = [r[0] for r in data_values]
    pct_codes = [r[0] for r in pct_codes]
    return [data_values, pct_codes]