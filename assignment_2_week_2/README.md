# Assignment 2 Week 2
## logistic_regression.ipynb
1.Contains logistic regression function from sklearn and a custom logistic regression function. Both models are trained on the iris dataset. The iris dataset is a datset corresponding to iris flower species, has 4 input features, 3 target classes and 150 observations.


2.Initially iris dataset was loaded and split into train and test data. Logistic regression function from sklearn was then fit onto the training data. The accuracy was obtained by running the trained model on the test data. 100% accuracy was obtained.


Custom Logistic_regression class is then defined. _init_is the constructor of the class and initializes the object with 2 parameters 'learning_rate' and 'iterations'. Softmax function is then defined and weights and bias is set to zero with size equal to the input data.'self.k = len(np.unique(y))' determines the number of unique classes. One-hot encoding of the labels is performed to facilitate gradient computation. The loop is then run for the number of iterations specified. Linear combination of input features and weights plus the bias term is calculated, softmax is then applied to get the predicted probabilities. Gradient with respect to weights and bias is calculted and the weights and bias is then updated using gradient descent. predict function computes linear model, apllies softmax and returns the class with highest probability. 100% accuracy was obtained.


## tensorflow_neural_networks.ipynb
1.Neural networks with required architecture and optimizer is built and displayed. Custm neural function with one hidden layer is also built and trained on custom dataset.


2.Neural networks were built with different number of neurons and different number of hidden layers as specified. The models were compiled using Adam and a custom compiler. 


Learning rate = 0.001 is set as the default value for the compiler. **kwargs is used  to pass a keyworded, variable-length argument list. super(CustomOptimizer, self).__init__(**kwargs, name='CustomOptimizer') calls the constructor of the parent Optimizer class, passing along any additional keyword arguments and setting the name of the optimizer to 'CustomOptimizer'. get_updates function calculates the updated parameters by computing the gradient of the loss with respect to each parameter. The update operations are created for each parameter and stored in self.updates. The update operation is gradient descent with an additional term of 0.02 to provide momentum.


Custom neural network without using tensorflow was created. It has one hidden layer and 10 neurons. Forward propogation, backward propogation are done using matrix multiplications. The model is run for 1000 iterations and gradient descent is used to update the weights. inputs = np.array([[0.2, 0.5], [0.1, 0.785], [0.9, 0.9], [0.653, 0.4]])                          
target = np.array([[0,0], [0,1], [1,0], [1,1]]) is the custom dataset used to train the model. Initially weights are set to zero and learning rate = 0.1. cross entropy loss and accuracy for every 100 iterations is printed.


3.Building a custom optimizer was very hard to achieve and frequently ran into errors but after a lot of debugging was able to create somewhat of a custom optimizer.
