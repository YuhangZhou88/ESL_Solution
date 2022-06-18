from statsmodels.stats.contingency_tables import mcnemar

# define contingency table
table = [[1434, 18],
         [33, 51]]

result = mcnemar(table, exact=False, correction=False)

print('statistic=%.3f, p-value=%.3f' % (result.statistic, result.pvalue))

# interpret the p-value
alpha = 0.05
if result.pvalue > alpha:
    print('Same proportions of errors (fail to reject H0)')
else:
    print('Different proportions of errors (reject H0)')