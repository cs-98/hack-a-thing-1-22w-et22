
import ipywidgets as widgets
import pandas as pd
from constants import anova, ttest, corr, regression, wilcoxon

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

    test_options_widgets = {anova: [cat_wid(), cont_wid("Dependent:")], \
                            ttest: [cat_wid(), cont_wid("Dependent:")], \
                            corr: [cont_wid("Var. 1:"), cont_wid("Var. 2:"), opt_wid()],\
                            regression: [cont_wid("Independent"), cont_wid("Dependent")],\
                            wilcoxon: [cat_wid(), cont_wid("Dependent")]}

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
