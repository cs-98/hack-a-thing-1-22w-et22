import ipywidgets as widgets
from constants import test_categories, test_category_map
from IPython.display import display, HTML
import pandas as pd

from constants import test_categories, test_category_map
from table_renderer import render_table_html
from statistics_connector import run_statistics

def run_test_wid():
    button = widgets.Button(description="Run test!")
    button.on_click(on_click_submit)
    return button

def on_click_submit(change, output, top_accordion, test_options_widgets):
    with output:
        top_idx = top_accordion.selected_index
        mid_idx = top_accordion.children[top_idx].selected_index
        if top_idx!=None and mid_idx!=None:
            test_name = test_category_map[test_categories[top_idx]][mid_idx]
            wids = test_options_widgets[test_name].children

            run_test_b = True
            params = []
            for idx, wid in enumerate(wids):
                if idx != len(wids)-1:
                    if not wid.value:
                        str_out = '<h4>' + test_name +  ' </h4>' + '<p> Test failed: please specificy all parameters!</p>'
                        display(HTML(str_out))
                        run_test_b = False
                        break
                    else:
                        params.append(wid.value)

            if run_test_b:
                stats = run_statistics(test_name, params, df)
                stats_html = render_table_html(stats, bc=True)
                str_out = '<h4>' + test_name +  ' </h4>' + stats_html
                display(HTML(str_out))

