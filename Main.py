#importing necessary libraries
import pandas as pd
from matplotlib import pyplot as plt


#reading the dataset
df = pd.read_csv('HR_comma_sep.csv')

#displaying the first few rows of the dataset
print(df.head())

#plotting the scatter plot
plt.scatter(df.satisfaction_level,df.left, marker='*', color='red')
plt.xlabel('Satisfaction Level')
plt.ylabel('Left Company')
plt.title('Satisfaction Level vs Left Company')
plt.show()

#Training the model
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
model = LogisticRegression()
x_train, x_test, y_train, y_test = train_test_split(df[['satisfaction_level']], df['left'], test_size=0.1, random_state=42)

#fitting the model
model.fit(x_train, y_train)

#predicting the results
y_pred = model.predict(x_test)

#displaying the predicted results
print("Predicted values:", y_pred)

#calculating the accuracy
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of the model:", accuracy)