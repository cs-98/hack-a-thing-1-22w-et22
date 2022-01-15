import ipywidgets as widgets
from IPython.display import display, HTML
import pandas as pd

from constants import test_categories, test_category_map
from table_renderer import render_table_html
from statistics_connector import run_statistics
from widget_constructor import construct_selector_widgets, construct_header_widgets

def panda_stats(df: pd.DataFrame):
    """
    Constructs main display structure for PandaStats and handles logic for 
    button clicks. 
    -df - input DataFrame for initializing PandaStats
    """
    # construct selector widgets
    test_options_widgets = construct_selector_widgets(df)

    # callback function called upon clicking the submit function for any of the statistical tests
    def on_click_submit(change):
        with output:
            # get test name and currently active widgets
            top_idx = top_accordion.selected_index
            mid_idx = top_accordion.children[top_idx].selected_index
            test_name = test_category_map[test_categories[top_idx]][mid_idx]
            wids = test_options_widgets[test_name].children

            # input validation
            run_test = True
            for idx, wid in enumerate(wids):
                if idx != len(wids)-1 and not wid.value:
                    str_out = '<h4>' + test_name +  ' </h4>' + '<p> Test failed: please specificy all parameters!</p>'
                    display(HTML(str_out))
                    run_test = False
            
            # if running the test
            if run_test:
                # aggregate parameters
                params = []
                for idx, wid in enumerate(wids):
                    if idx != len(wids)-1:
                        params.append(wid.value)

                # run test
                stats = run_statistics(test_name, params, df)
                stats_html = render_table_html(stats, bc=True)
                str_out = '<h4>' + test_name +  ' </h4>' + stats_html
                display(HTML(str_out))

    # construct submit button
    def run_test_wid():
        button = widgets.Button(description="Run test!")
        button.on_click(on_click_submit)
        return button

    # put submit button and other test specific widgets in a vertical box
    for key in test_options_widgets.keys():
        children = test_options_widgets[key]
        children.append(run_test_wid())
        test_options_widgets[key] = widgets.VBox(children=children)

    # construct lower-level accordion
    children = []
    for index, opt in enumerate(test_categories):
        mid_accordion = widgets.Accordion(children=[test_options_widgets[o] for o in test_category_map[opt]])
        for i, o in enumerate(test_category_map[opt]):
            mid_accordion.set_title(i, o)    
        mid_accordion.selected_index = None 
        children.append(mid_accordion)

    # construct top-level accordion
    top_accordion = widgets.Accordion(children=children)
    top_accordion.selected_index = None
    for index, opt in enumerate(test_categories):
        top_accordion.set_title(index, opt)
    
    # create input data widget
    html = render_table_html(df)
    table = widgets.HTML(value=html, placeholder='', description='')

    # create output data widget with a clear button
    output = widgets.Output()
    clear_button = widgets.Button(description='Clear output!')
    def on_clear_click(change):
        with output:
            output.clear_output()

    clear_button.on_click(on_clear_click)
    
    # construct header widgets
    header, data_header, stats_header, output_header = construct_header_widgets()

    # package all components in a vertical box
    return widgets.VBox(children=(header, data_header, table, stats_header, top_accordion, output_header, output, clear_button))

