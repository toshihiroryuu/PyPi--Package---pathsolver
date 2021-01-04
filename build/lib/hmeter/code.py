import gradio as gr

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report 
from sklearn.linear_model import SGDClassifier

from sklearn.svm import SVC

df = pd.read_csv('https://raw.githubusercontent.com/toshihiroryuu/Machine_learning/master/ML_001_Heart_faliure/Dataset/heart_failure_clinical_records.csv')

Y = df['DEATH_EVENT']
X = df[['age', 'ejection_fraction','serum_creatinine','time']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, stratify = Y, test_size=0.2, random_state=52)

model = SVC(kernel='linear', C = .01, gamma = 0.2)
model.fit(X_train, Y_train)

Y_predict = model.predict(X_test)

def calculate(Age, time, ejection_fraction, serum_creatinine):

      test = [[Age, time, ejection_fraction, serum_creatinine]]
      test = pd.DataFrame(test, columns =['age', 'ejection_fraction','serum_creatinine','time'], dtype = float)
      return int(model.predict(test))


def hlaunch():

      iface = gr.Interface(
      fn=calculate,
      inputs=[gr.inputs.Slider(0, 100), gr.inputs.Slider(0, 300), gr.inputs.Slider(0, 80), gr.inputs.Slider(0, 10)],
      outputs=["number"])
      iface.launch(share=True)