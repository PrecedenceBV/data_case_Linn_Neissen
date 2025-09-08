import pandas as pd

nps_scores = pd.read_csv("/Users/precedenceintern/PycharmProjects/data_case_Linn_Neissen/data-case/nps_scores.csv", sep=";")

print(nps_scores)

total = nps_scores['Recommendation_score'].sum()
print(total)

promoters = nps_scores['Recommendation_score'].isin([9, 10]).sum()
promoters_perc = promoters / total * 100
print(promoters_perc)

detracters = nps_scores['Recommendation_score'].isin([0, 1, 2, 3, 4, 5, 6]).sum()
detracters_perc = detracters / total * 100
print(detracters)
print(detracters_perc)

#result = promoters_perc.groupby('Journey_Type')['Recommendation_score'].isin([9,10]).mean() * 100

result = nps_scores.groupby('Journey_Type').apply(
    lambda x: x['Recommendation_score'].isin([9, 10]).mean() * 100
).reset_index(name='Percentage_9_or_10')

nps = promoters_perc - detracters_perc

