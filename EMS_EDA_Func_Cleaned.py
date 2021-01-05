#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import random
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from datetime import timedelta
import seaborn as sns


# In[2]:


def pd_dttm_import(want_cols):
    '''Parameters: takes in list of column names wanted that will be
    used in pandas .read_csv method

    Results: Outputs the indices of the columns names that are date
    values and uses resulting list of indices as parse_dates parameter
    in pandas .read_csv method'''
    dt_ind = []
    for i in want_cols:
        if 'dttm' in i.lower() or 'date' in i.lower():
            dt_ind.append(want_cols.index(i))
    return dt_ind


# In[8]:


def to_time_delta(df, time2, time1):
    '''
    Function takes a dataframe, and two datetime columns of the datafrom and returns the seconds difference
    between the two events.

    Parameters:
    df (pandas.DataFrame) : Pandas dataframe to use
    time2 (pandas.Series) : Pandas column from dataframe df (suggest later event)
    time1 (pandas.Series) : Pandas column from dataframe df (suggest earlier event)

    Returns:
    Pandas.Series : The seconds difference between the events for each row in df
    '''
    return (df[time2] - df[time1]).apply(lambda x: timedelta.total_seconds(x) if not isinstance(x, pd._libs.tslibs.nattype.NaTType) else None)


# Graphing work

# In[6]:


#plot time difference between two events across rows
#comparing average commute time between districts
def plot_time_diff_by_cat(df, col, time_col, vals=None):
    '''
    Function takes a dataframe, categorical column, and time value columns and outputs a graph of the mean time per
    category value. Can additionally filter by specific categories with the vals parameter.

    Parameters:
    df (pandas.DataFrame) : Pandas dataframe to use
    col (pandas.Series) : Column from pandas dataframe df (will be x-axis)
    time_col (pandas.Series) : Columns from pandas dataframe (will be averaged - must be num)
    vals (array-type) : array of specific values from col that user would like to graph

    Returns:
    Plots values, returns no object to assign to variable
    '''
    fig, ax = plt.subplots(figsize=(20,20))
    plt.xticks(rotation=90, fontsize=15)
    plt.yticks(fontsize=15)
    ax.set_xlabel(col, fontsize=20)
    ax.set_ylabel(f'Time (s)', fontsize=20)
    ax.set_title(f'{time_col} by {col}', fontsize=20)
    x=[]
    y=[]
    if vals == None:
        for i in df[col].unique():
            time_frame[(time_frame['time_delta'] > 0) & (time_frame['time_delta'] < (int(mn) + 3*int(st)))].hist(ax=ax[i])
            x.append(i)
            y.append(np.mean(df[df[col] == i][time_col]))
    else:
        for i in vals:
            x.append(i)
            y.append(np.mean(df[df[col] == i][time_col]))

    return ax.bar(x,y)



# In[20]:


def sub_occ_bar_graph(df, high_cat, low_cat, title, vals1=None, vals2=None):
    #Takes in dataframe(df), higher level category/feature(high_cat), lower level feature(low_cat)
    #returns bar graph of the count of categories in the low_cat for each high_cat value

    if vals1 == None:
        fig, ax = plt.subplots(figsize=(15,15))
        plt.xticks(rotation=90, fontsize=15)
        plt.yticks(fontsize=15)
        ax.set_xlabel(high_cat, fontsize=20)
        ax.set_ylabel('Occurences', fontsize=20)
        ax.set_title(f'{title}', fontsize=20)
        if vals2 == None:
            ax = sns.countplot(x=high_cat, hue=low_cat, data=df)
        else:
            ax = sns.countplot(x=high_cat, hue=low_cat, data=df[df[low_cat].isin(vals2)])
        plt.setp(ax.get_legend().get_texts(), fontsize=22)
        plt.setp(ax.get_legend().get_title(), fontsize=25)
    else:
        fig, ax = plt.subplots(figsize=(15,15))
        plt.xticks(rotation=90, fontsize=15)
        plt.yticks(fontsize=15)
        ax.set_xlabel(high_cat, fontsize=20)
        ax.set_ylabel('Occurences', fontsize=20)
        ax.set_title(f'{title}', fontsize=20)
        if vals2 == None:
            ax = sns.countplot(x=high_cat, hue=low_cat, data=df[df[high_cat].isin(vals1)])
        else:
            ax = sns.countplot(x=high_cat, hue=low_cat, data=df[(df[high_cat].isin(vals1)) & (df[high_cat].isin(vals1))])
        plt.setp(ax.get_legend().get_texts(), fontsize=22)
        plt.setp(ax.get_legend().get_title(), fontsize=25)



# In[3]:


#example of creating time sampled data
#plt.plot(df['Call Date','On Scene DtTm','Dispatch DtTm'].resample('Y', on='Call Date').mean())


# In[54]:


def data_to_3std(series):
    #will want to limit
    st = np.std(series)
    mn = np.mean(series)
    return series[series < (int(mn) + 3*int(st))]

def mann_whit_u(df, cat_col, cat_val, time, title1, title2):
    df1 = df[df[cat_col].isin(cat_val)]
    df2 = df[~df[cat_col].isin(cat_val)]
    print(f'Average for High Homeless Pop Areas: {df1[time].mean()}')
    print(f'Average for else: {df2[time].mean()}')
    fig, ax = plt.subplots(2,1)
    ax[0].hist(data_to_3std(df1[time]))
    ax[0].set_title(title1)
    ax[0].set_xlabel('Time(s)')
    ax[1].hist(data_to_3std(df2[time]))
    ax[1].set_title(title2)
    ax[1].set_xlabel('Time(s)')
    fig.tight_layout()
    #over all time
    res = stats.mannwhitneyu(df1[time].sample(frac=1), df2[time].sample(frac=1), alternative='two-sided')
    print(f'P-Value: {res.pvalue}')

print('Imported Successfully!')

