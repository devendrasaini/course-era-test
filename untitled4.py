# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FBU2eNgUrZ2DWYtGfvv1sfUM3gPh_Tr8
"""

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("http://13.234.66.67/summer19/datasets/bank.csv")

df.head(5)

df.groupby('Gender').size().plot('bar',label='Gender')

plt.scatter(df.iloc[0:,6             ],df.iloc[0:,8        ])

df.groupby('Geography').size().plot('pie',label='Country',autopct='%d%%')
