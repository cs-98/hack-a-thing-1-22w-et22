from typing import List
import ipywidgets as widgets
from IPython.display import display, HTML
import pandas as pd

from constants import test_categories, test_category_map
from table_renderer import render_table_html
from statistics_connector import run_statistics
from submit_widget import run_test_wid

def panda_stats(df):
    # construct selector widgets
    test_options_widgets = construct_selector_widgets(df)

    for key in test_options_widgets.keys():
        children = test_options_widgets[key]
        children.append(run_test_wid())
        test_options_widgets[key] = widgets.VBox(children=children)

    children = []
    for index, opt in enumerate(test_categories):
        mid_accordion = widgets.Accordion(children=[test_options_widgets[o] for o in test_category_map[opt]])
        for i, o in enumerate(test_category_map[opt]):
            mid_accordion.set_title(i, o)    
        mid_accordion.selected_index = None 
        children.append(mid_accordion)

    top_accordion = widgets.Accordion(children=children)
    top_accordion.selected_index = None
    for index, opt in enumerate(test_categories):
        top_accordion.set_title(index, opt)
    
    html = render_table_html(df)
    table = widgets.HTML(value=html, placeholder='', description='')

    output = widgets.Output()
    clear_button = widgets.Button(description='Clear output!')

    def on_clear_click(change):
        with output:
            output.clear_output()

    clear_button.on_click(on_clear_click)
    
    header, data_header, stats_header, output_header = construct_header_widgets()
    return widgets.VBox(children=(header, data_header, table, stats_header, top_accordion, output_header, output, clear_button))


def construct_selector_widgets(df: pd.DataFrame):
    """
    Constructs widgets for selecting tests. 
    -df - input DataFrame to evaluate
    """
    df_number = df.select_dtypes(include='number')
    df_cat  = df.select_dtypes(include='category')

    cat_wid = lambda : widgets.Dropdown(
        options=df_cat.columns,
        value=None,
        description='Grouping:',
        disabled=False,
    );

    cont_wid = lambda description: widgets.Dropdown(
        options=df_number.columns,
        value=None,
        description=description,
        disabled=False,
    );

    opt_wid = lambda : widgets.Dropdown(
        options=["pearson", "spearman", 'kendall'],
        value=None,
        description='Method:',
        disabled=False,
    );

    test_options_widgets = {"One-way ANOVA": [cat_wid(), cont_wid("Dependent:")], \
                            "Independent T-test": [cat_wid(), cont_wid("Dependent:")], \
                            "Correlation": [cont_wid("Var. 1:"), cont_wid("Var. 2:"), opt_wid()],\
                            "Linear Regression": [cont_wid("Independent"), cont_wid("Dependent")],\
                            "Wilcoxon Signed-Rank Test": [cat_wid(), cont_wid("Dependent")]}

    return test_options_widgets

def construct_header_widgets():
    header = widgets.HTML(
        value="<h1>PandaStats</h1>",
        placeholder='',
        description='',
    )

    stats_header = widgets.HTML(
        value="<h3>Statistical Tests</h3>",
        placeholder='',
        description='',
    )

    output_header = widgets.HTML(
        value="<h3>Test Output</h3>",
        placeholder='',
        description='',
    )

    data_header = widgets.HTML(
        value="<h3>Input Data</h3>",
        placeholder='',
        description='',
    )

    return header, data_header, stats_header, output_header
