from sklearn.metrics.pairwise import cosine_similarity
from DataSet.Corona_modify import cleansing
import pandas as pd
from DataSet.Corona_robust import C_Rbst
class Corona_compare:

    def __init__(self, nutri):
        self.data = nutri

    def cleansing(self, nutri):
        nutri.iloc[:, 1:] = nutri.trans_rbst(nutri.data)
        return nutri

    def calc(self,nutrition):

        raw = nutrition
        figure = C_Rbst(nutrition)
        robusted = cleansing(raw, figure)

        similarity = []
        Relationship = []
        for x in range(len(robusted) - 1):
            for y in range(x, len(robusted) - 1):
                Co_Si = cosine_similarity([robusted.iloc[x, 1:]],[robusted.iloc[y + 1,1:]])
                similarity.append(Co_Si[0][0])
                Country=robusted.iloc[x, 0]+"-"+robusted.iloc[y + 1, 0]
                Relationship.append(Country)
        result = pd.DataFrame()
        result = result.assign(Country_Relationship=Relationship,Cosine_Similarity=similarity).round(3).\
            sort_values(by=['Cosine_Similarity'], axis=0,ascending=False)
        result.reset_index(drop=True, inplace=True)
        print(result.head(10))
