import pandas as pd
from random import randint
import os
import sqlite3
from keras.models import Sequential
from keras.layers import Dense,Dropout
import numpy as np
from app.models import UserPreferences, Movie
from app import db
from config import Config

path = os.getcwd() + '/app/dataset/movies_metadata.csv'
data = pd.read_csv(path)

def get_movie_info_min(list):
    movies = []
    for index in list:
        movies.append(Movie(id=data.loc[index,'id'], original_title=data.loc[index,'original_title'], release_date=data.loc[index,'release_date'], poster_path=data.loc[index,'poster_path']))
    return movies


def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return connection

def get_movie_info(id):

    id = int(id)
    movie = Movie( 
        id=id,
        original_title=data.loc[id,'original_title'],
        poster_path=data.loc[id,'poster_path'], 
        release_date=data.loc[id,'release_date'],
        adult=data.loc[id,'adult'],
        genres=data.loc[id,'genres'],
        imdb_id=data.loc[id,'imdb_id'],
        original_language=data.loc[id,'original_language'],
        overview=data.loc[id,'overview'],
        production_companies=data.loc[id,'production_companies'],
        runtime=data.loc[id,'runtime']
    )
    print(movie)
    return movie

def set_preferences(user_id, movie_ids):
    for movie_id in movie_ids:
        preference = UserPreferences(movie_id=movie_id, user_id=user_id)
        db.session.add(preference)
    db.session.commit()

def predict(movshown, movsel):
    
    movie_db = create_connection(Config.MOVIE_DATABASE_PATH)
    cur = movie_db.cursor()
    cur.execute("PRAGMA table_info('movlens')")
    rows = cur.fetchall()
    colnames=[]
    for row in rows:
        colnames.append(row[1])
    st=""
    for x in movshown:
        st+=str(x)+","
    st=st[:-1]
    cur.execute("select * from movlens where id not in("+st+")")
    rows=cur.fetchall()
    df_test=pd.DataFrame(rows,columns=colnames)
    st=""
    for x in movshown:
        st+=str(x)+","
    st=st[:-1]
    cur.execute("select * from movlens where id in("+st+")");
    rows=cur.fetchall()
    df_train=pd.DataFrame(rows,columns=colnames)
    print(df_train.shape,"   ",df_test.shape)
    y_train=[]
    for i in df_train.index:
        if df_train['id'][i] in movsel:
            y_train.append([1])
        else:
            y_train.append([0])
    print(y_train)
    y_train=pd.DataFrame(y_train)
    X_train=df_train.drop(['original_title','id','genres'],axis=1)
    X_test=df_test.drop(['original_title','id','genres'],axis=1)
    model=Sequential()
    model.add(Dense(units=256,activation='relu',kernel_initializer='random_uniform',input_dim=20))
    model.add(Dense(units=128,activation='relu',kernel_initializer='random_uniform'))
    model.add(Dropout(0.2))
    model.add(Dense(units=16,activation='relu',kernel_initializer='random_uniform'))
    model.add(Dropout(0.2))
    # model.add(Dense(units=16,activation='relu',kernel_initializer='random_uniform'))
    model.add(Dense(units=1,activation='sigmoid'))
    model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    hist=model.fit(X_train,y_train,epochs=40,batch_size=5)
    y_pred=model.predict_classes(X_test)
    print(sum(y_pred==1))
    # pred_mov_id=list(df_test.iloc[np.where(y_pred==1)[0],1])
    pred_mov_id=np.where(y_pred==1)[0]
    print(pred_mov_id)
    return pred_mov_id