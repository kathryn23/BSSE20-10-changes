from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

print("Linear Mean Absolute error is ", metrics.mean_absolute_error(Y_test, ylinear_pred))
print("Linear Mean Squared error is ", metrics.mean_squared_error(Y_test, ylinear_pred))
print("Linear Root Mean Square error is ", np.sqrt(metrics.mean_squared_error(Y_test, ylinear_pred)))
#print("other Linear Score is ", model.mean_squared_error(Y_test, y_pred))
print("Neural network Mean Absolute error is ", metrics.mean_absolute_error(Y_test, ymlp_pred))
print("Neural network Squared error is ", metrics.mean_squared_error(Y_test, ymlp_pred))
print("Neural network Root Mean Square error is ", np.sqrt(metrics.mean_squared_error(Y_test, ymlp_pred)))


model = LinearRegression()
model.fit(X_train, Y_train)
ylinear_pred = model.predict(X_test)

plt.plot(X, Y)
plt.xlabel('Year')
plt.ylabel('Monthly rainfall')
plt.show()

regressor = LinearRegression()
regressor.fit(X,Y)
print(regressor.score(X,Y) * 100)
prediction = regressor.predict()

polynomial_features= PolynomialFeatures(degree=3)
X_poly = polynomial_features.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, Y)
#print(model.score(X_poly,Y) * 100)
y_predict = model.predict(polynomial_features.fit_transform([[2011]]))
print(y_predict)

ar = [[1, 2017]]
prediction = regressor.predict(ar)
print(prediction)
