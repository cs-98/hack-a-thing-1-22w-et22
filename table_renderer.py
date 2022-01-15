import pandas as pd
from constants import even_color, odd_color, highlight_color

def render_table_html(df: pd.DataFrame, num_rows: int = 5, bc: bool = False):
  """
  Returns html representation of a pandas dataframe.
  Similar to df.head().
  -Gets first num_rows rows of the dataframe.
  -If bc is True, renders with uniform background, otherwise striates.
  """
  # get first num_rows rows
  df = df.iloc[:num_rows]

  # table body construction
  html_body = ""
  for index, row in df.iterrows():
    html_row = f'<th>{index}</th>'
    for col in df:
      html_row += f'<td>{row[col]}</td>'
    if bc:
      back_color = even_color
    else:
      back_color = even_color if index % 2 == 0 else odd_color
    html_body += f"""<tr onMouseOver="this.style.backgroundColor='{highlight_color}'"
        onMouseOut="this.style.backgroundColor='{back_color}'">{html_row}</tr>"""
  html_body = f'<tbody>{html_body}</tbody>'

  # table head construction
  html_head = f'<th></th>'
  for col in df:
    html_head += f'<th>{col}</th>'
  html_head = f'<tr style="text-align: right;">{html_head}</tr>'
  html_head = f'<thead>{html_head}</thead>'
  
  # table construction
  html = f'<table border="1">{html_head}{html_body}</table>'

  return html
