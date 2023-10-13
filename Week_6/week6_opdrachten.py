import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import r2_score, mean_squared_error

np.random.seed(2)

x = np.random.uniform(0, 10, 200)
y = 2 * x**2 -5 * x + 3 + np.random.normal(0, 10, 200)

inputValues = {
    'x' : x[:],
    'y' : y[:]
}

df = pd.DataFrame(inputValues)
print(df)
# fig, (ax1, ax2) = plt.subplots(2)
# # Plot the dataset
# ax1.scatter(x, y)
# ax1.set_xlabel('x')
# ax1.set_ylabel('y')
# ax1.set_title('Dataset')

# Split data
inputValuesTrain = {
    'x' : x[:160],
    'y' : y[:160]
}
data_train = pd.DataFrame(inputValuesTrain)
inputValuesTest = {
    'x' : x[160:],
    'y' : y[160:]
}
data_test = pd.DataFrame(inputValuesTest)

train_x = x[:160]
train_y = y[:160]
test_x = x[160:]
test_y = y[160:]

train_x = data_train['x']
train_x_sq = pd.DataFrame(data_train['x']**2)
# train_x_p3 = pd.DataFrame(data_train['x']**3)
# train_x_p4 = pd.DataFrame(data_train['x']**4)

train_x_poly = pd.concat([train_x, train_x_sq], axis = 1)
X_train = sm.add_constant(train_x_poly)
model = sm.OLS(data_train['y'], X_train)
results_train = model.fit()

test_x = data_test['x']
test_x_sq = pd.DataFrame(data_test['x']**2)
# test_x_p3 = pd.DataFrame(data_test['x']**3)
# test_x_p4 = pd.DataFrame(data_test['x']**4)

test_x_poly = pd.concat([test_x, test_x_sq], axis = 1)
X_test = sm.add_constant(test_x_poly)
model = sm.OLS(data_test['y'], X_test)
results_test = model.fit()

predicted_train_y = results_train.predict(X_train)
predicted_test_y = results_test.predict(X_test)

r_squared = results_train.rsquared
print(r_squared)

r_squared_test = r2_score(data_test['y'], predicted_test_y)
print(r_squared_test)
if r_squared_test > r_squared:
    print(f'Feest')
else:
    print(f'Big sad')
    
mse_train = mean_squared_error(df['y'], predicted_train_y)
mse_test = mean_squared_error(df['y'], predicted_test_y)

plt.scatter(data_train['x'], data_train['y'])
plt.scatter(data_train['x'], predicted_train_y, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Danoontje')
plt.show()




# Plot trainingsdata
# ax2.scatter(train_x, train_y)
# ax2.set_xlabel('x')
# ax2.set_ylabel('y')
# ax2.set_title('Trainings dataset')
# plt.show()


