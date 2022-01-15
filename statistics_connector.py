import pingouin as pg
import constants

def run_statistics(test_name, params, df):
    """
    Returns output from calling the test defined by test_name from pingouin
    with input from params and df.
    Currently supports:
    -ANOVA
    -t-test
    -correlation
    -simple linear regression
    -wilcoxon signed-rank test.
    """

    stats = None

    match test_name:

        case constants.anova:
            stats = pg.anova(df, dv=params[1], between=params[0])

        case constants.ttest:
            dfs = dict(tuple(df.groupby(params[0])))
            keys = list(dfs.keys())
            stats = pg.ttest(dfs[keys[0]][params[1]],dfs[keys[1]][params[1]])

        case constants.corr:
            stats = pg.corr(df[params[0]], df[params[1]], method=params[2])

        case constants.regression:
            stats = pg.linear_regression(df[params[0]], df[params[1]])

        case constants.wilcoxon:
            dfs = dict(tuple(df.groupby(params[0])))
            keys = list(dfs.keys())
            stats = pg.wilcoxon(dfs[keys[0]][params[1]],dfs[keys[1]][params[1]])

    return stats
