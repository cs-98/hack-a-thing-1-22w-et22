# PandaStats
## Technology Exploration

I wanted to explore methods to integrate graphical user interfaces with code in Jupyter Notebook. Specifically, I explored the `jupyter-widgets` library and documentation on developing custom widgets and using existing widgets. 

## Project Purpose

Scientists and social scientists often analyze their data and run statistical tests in Python and Jupyter Notebook. Running many statistical tests in Python in an organized fashion, however, can be challenging. When using existing statistics packages, it is easy to ignore important parameters or input incorrect data, especially when testing many different hypotheses.

Alternatively, GUI-based statistics softwares like SPSS are easy to use and force the user to deliberately select different parameters important to statistical tests, leading to fewer errors. However, these softwares are rarely used in practice because no one wants to run statistics with a third-party software when they are already analyzing their data in Python.

Here, I demonstrate a prototype for PandaStats a GUI-based widget for conducting statistical analyses in Jupyter Notebook. PandaStats accesses the benefits of running statistical tests in SPSS and Python while avoiding their downsides. Specifically, PandaStats has the potential to reduce errors in statistics by forcing users to deliberately select parameters and input variables via a GUI. At the same time, PandaStats can be easily integrated with existing analysis code because it is a widget that can be run in the Jupyter Notebook environment.

## Technology Fit
This prototype code works for a limited set of use cases and parameters described here. Specifically, it supports five statistical tests: one-way anovas, independent sample t-tests, simple linear regressions, correlations, and pairwise wilcoxon signed-rank tests. A more complete version of this idea would support more tests but also provide more robust parameter options for tests. Also, input validation was not completely implemented, so incorrect inputs may return value erorrs.  

To test the protyped code, see the jupyter notebook `panda_stats_test.ipynb`. It requires Python with version above 3.10 and `pandas`, `pingouin`, and `ipywidgets` as dependencies. 

Specific test cases are described in the notebook and below. 

## PandaStats Use Cases
I include a few examples of the PandaStats display and results of running different statistical tests for two different datasets. 

These test cases are more fully described in the associated jupyter notebook. 

### Dataset 1 - PandaStats Display Before Running Tests
![Dataset 1](https://github.com/cs-98/hack-a-thing-1-22w-et22/blob/main/screenshots/pre_analysis1.png?raw=true)

### Dataset 1 - t-test
![Dataset 1](https://github.com/cs-98/hack-a-thing-1-22w-et22/blob/main/screenshots/ttest1.png?raw=true)

### Dataset 1 - regression
![Dataset 1](https://github.com/cs-98/hack-a-thing-1-22w-et22/blob/main/screenshots/regression1.png?raw=true)

### Dataset 1 - wilcoxon
![Dataset 1](https://github.com/cs-98/hack-a-thing-1-22w-et22/blob/main/screenshots/wilcoxon1.png?raw=true)

### Dataset 2 - PandaStats Display Before Running Tests
![Dataset 2](https://github.com/cs-98/hack-a-thing-1-22w-et22/blob/main/screenshots/pre_analysis2.png?raw=true)


### Dataset 2 - ANOVA
![Dataset 2](https://github.com/cs-98/hack-a-thing-1-22w-et22/blob/main/screenshots/anova2.png?raw=true)

### Dataset 2 - Spearman Correlation
![Dataset 2](https://github.com/cs-98/hack-a-thing-1-22w-et22/blob/main/screenshots/corrspear2.png?raw=true)

### Dataset 2 - Pearson Correlation
![Dataset 2](https://github.com/cs-98/hack-a-thing-1-22w-et22/blob/main/screenshots/corrpear2.png?raw=true)








## Author

Ethan Trepka

## Acknowledgments
`jupyter-widgets` used for widget display, documentation linked [here](https://ipywidgets.readthedocs.io/en/latest/index.html)

`pingouin` used for statistics, documentation linked [here](https://pingouin-stats.org/index.html). 

`pandas` used for data types, documentation linked [here](https://pandas.pydata.org/docs/).

