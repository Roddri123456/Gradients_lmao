#Made by Rodrigo Hernández Gutiérrez and thanks pyninja for the help
import matplotlib.pyplot as plt
import numpy as np

#Set data
X = [2,5,3]
Y = [2,4,5]

#Set initial values of bias, eta and iterations
bias = 0
eta = 0.1
n_iterations = 1000

#Computing de descent gradient
for iteration in range(n_iterations):
    #calculate the gradient
    gradients = (1/3)*((-2*(2-(bias + (0.4*2)))) + (-2*(5-(bias + (0.4*3)))) + (-2*(4-(bias + (0.4*5)))))
    bias = bias - eta*gradients
    #plot bias change
    y_predict = []
    for x in X:
        y_predict.append(bias + (0.4*x))
    plt.plot(X,y_predict, color = 'blue')
    #calculation of Error Cuadratico Medio "ERM"
    errors = []
    for i in range(len(X)):
        errors.append((Y[i] - (bias+(0.4*X[i])))**2)
    mse = (1/3)*np.sum(errors)
    print(f"MSE: {mse} and Bias: {bias}")



#plot data points for x and y limits

plt.scatter(X,Y, c= 'red', s=20)
plt.xlim((0,6))
plt.ylim((0,6))
plt.show()