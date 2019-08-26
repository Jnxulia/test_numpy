
"""
Author : J.nava
Example read and export data with pandas
"""
import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format

global df 
class Reader :
    df = []
    url = ""
    def __init__(self, url):
        t1 = pd.read_html(url,header=1, index_col=0)
        self.df = t1[1]
    def load_data(self,drop_columns, columns):
        if drop_columns:
            self.df = self.df.drop(drop_columns ,  axis = 1)[:-1]
        self.df.columns = columns
        self.df.replace('\s+', '',regex=True,inplace=True)
        print(self.df.head())

    def avg_column(self , column, name_avg_column):
        self.df[column] = self.df[column].astype(int)
        self.df[name_avg_column] = (100 * self.df[column]) / self.df[column].sum()
        print("suma" , self.df[column].sum())

    def export_data(self, file):
        self.df.to_csv(file)
        print ("archivo exportado {}".format(file))


if __name__ == "__main__":
    url = 'https://es.wikipedia.org/wiki/Chile'
    drop_columns = ['Mapa administrativo']
    columns = ['Población', 'Superficie', 'Densidad', 'Capital']
    leer_wikipedia = Reader(url)
    leer_wikipedia.load_data(drop_columns, columns)
    leer_wikipedia.avg_column('Población', '% de la Población')
    leer_wikipedia.export_data("test.csv")