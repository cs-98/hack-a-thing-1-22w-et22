"""
Stores constants for:
-supported test categories
-supported tests
-color scheming for table display
"""

# supported test cateogires
cat_cont_test = "ANOVA and T-test"
cont_cont_test = "Correlation and regression"
non_param_test = "Non-parametric"

# supported test labels
anova = "One-way ANOVA"
ttest =  "Independent T-test"
corr = "Correlation"
regression = "Linear Regression"
wilcoxon = "Wilcoxon Signed-Rank Test"

# test hierarchy 
test_categories = [cat_cont_test, cont_cont_test, non_param_test]
test_category_map = {test_categories[0]: [anova, ttest], \
                        test_categories[1]: [corr, regression], \
                        test_categories[2]: [wilcoxon]}


# table colors
odd_color = '#f7f7f7'
even_color = '#ffffff'
highlight_color = '#e0e0e0'