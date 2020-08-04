import numpy as np
import pandas as pd
import collections
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle 


class VideoModel():
    
    def __init__(self):
        self.vector = CountVectorizer()
        self.nb = MultinomialNB()

    def get_data(self, file_name):
        file = os.path.join('data', file_name)
        df = pd.read_csv(file)
        return df

    def get_category(self, category_file):
        file = os.path.join('data', category_file)
        category_json = pd.read_json(file)
        category_dic = [{'id': item['id'], 'title': item['snippet']['title']} for item in category_json['items']]
        return category_dic

    def train_model(self, df):
        columns = ['title', 'category_id']
        new_videos = df[columns]
        file = os.path.join('data', "new_video.csv")
        new_videos.to_csv(file, index=False)
        new_videos = pd.read_csv(file, header=0, names=['Title','Category_ID'])
        counts = self.vector.fit_transform(new_videos['Title'].values)
        targets = new_videos['Category_ID'].values
        self.nb.fit(counts, targets)
        self.save_model_pickel(self.nb)

    def predict(self, titles):
        Pkl_Filename = "youtube_model.pkl"
        with open(os.path.join('save_model', Pkl_Filename), 'rb') as file:  
            pickled_model = pickle.load(file)

        titles_counts = self.vector.transform(titles)
        predict = pickled_model.predict(titles_counts)

        category_dic = self.get_category('video_category.json')
        category_list = []
        for category_id in predict:
            matching = [x for x in category_dic if x["id"] == str(category_id)]
            if matching:
                category_list.append(matching[0]["title"])

        title_dfs = []
        for i in range(0, len(titles)):
            title_category = {'Title': titles[i],  'Category': category_list[i]}
            title_dfs.append(title_category)

        df = pd.DataFrame(predict)
        title_df = pd.DataFrame(title_dfs)
        pre_final_df = pd.concat([df, title_df], axis=1)
        pre_final_df.columns = (['Categ_ID', 'Video Title', 'Predicted Video Type'])
        result_df = pre_final_df.drop(['Categ_ID'],axis=1)
        cols = result_df.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        result_df = result_df[cols]
        return result_df


    def save_model_pickel(self, model):
        Pkl_Filename = "youtube_model.pkl"
        with open(os.path.join('save_model', Pkl_Filename), 'wb') as file:
            pickle.dump(model, file)




