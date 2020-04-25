#Using a smaller dataset for learning linear Regression model.
#Predicting marks on the basis of duration studied.
import pandas as pd
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('marks_duration.csv')

x = dataset['duration']
X = x.values.reshape(4,1)

y = dataset['marks']
 
#Creating the model
model = LinearRegression()

#Training the model
model.fit(X,y)

#Predicting the value...
predicted_marks = model.predict([[9]])
print("Predicted Marks : " , predicted_marks[0])