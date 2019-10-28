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

# path = os.getcwd() + '/app/dataset/movies_metadata.csv'
# data = pd.read_csv(path)

def get_movie_info_min(list):

    movie_db = create_connection(Config.MOVIE_INFO_DATABASE_PATH)
    data = pd.read_sql_query('SELECT * from db where id in ' + str(tuple(list)), movie_db)
   
    movies = []
    for index in range(0, data.shape[0]):
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

    movie_db = create_connection(Config.MOVIE_INFO_DATABASE_PATH)

    data = pd.read_sql_query('SELECT * from db where id = ' + str(id), movie_db)
    
    genres = pd.read_sql_query('SELECT genre_name from genres where id = ' + str(id), movie_db)
   
    genres_list = []
    for index in range(0, genres.shape[0]):
        genres_list.append(genres.at[index, 'genre_name'])
    
    movie = Movie( 
        original_title=data.at[0,'original_title'],
        poster_path=data.at[0,'poster_path'], 
        release_date=data.at[0,'release_date'],
        genres=genres_list,
        adult=data.at[0,'adult'],
        imdb_id=data.at[0,'imdb_id'],
        original_language=data.at[0,'original_language'],
        overview=data.at[0,'overview'],
        production_companies=data.at[0,'production_companies'],
        runtime=data.at[0,'runtime'],
        cast = data.at[0, 'cast'].split(',')
    )
    
    return movie

def get_preferences(user_id):
    result = UserPreferences.query.with_entities(UserPreferences.movie_id).filter(UserPreferences.user_id == user_id).all()
    result = [r[0] for r in result]
    return result

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
    cur.execute("select * from movlens where id in("+st+")")
    rows=cur.fetchall()
    df_train=pd.DataFrame(rows,columns=colnames)
    print(df_train.shape,"   ",df_test.shape)
    print(df_train.head())
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
    pred_mov_id=list(df_test.iloc[np.where(y_pred==1)[0],1])
    # pred_mov_id=np.where(y_pred==1)[0]
    print('-----------predicted-------')
    print(pred_mov_id)
    return pred_mov_id