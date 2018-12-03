# Back-Propogation-Neural-Network
The purpose of the this assignment is to practice with back-propagation neural networks.
 
Implement a fully-connected back-propagation network using TensorFlow (DO NOT use any other package such as Keras or Estimator):

Your network should include one hidden layer and one output layer. The input for the neural network is a two-dimensional data set which presents sample points from different classes. Use the provided sample program to create the data set(s).


Your program should display sample points and the regions for each class with different colors.
Your program should include the following sliders, buttons, and drop-down box.
Sliders:
a. "Alpha": (Learning rate) Range should be between 0.000 and 1.0. Default value = 0.1 increments=.001
b. "Lambda": (Weight regularization). Range should be between 0.0 and 1.0. Default value = 0.01 Increments=0.01
c. "Num. of Nodes in Hidden Layer": Range 1 to 500. Default value=100  increment=1
d. "Number of Samples": This slider determines the number of samples which will be generated for input data. Range 4 to 1000. Default value=200, increment=1.
e. "Number of Classes": This slider determines the number of classes which will be generated for input data. Range 2 to 10. Default value=4 Increments=1


Buttons:
a. "Adjust Weights (Train)": When this button is pressed the training should be applied for 10 epochs. and the display should be updated after each epoch. (an epoch is one pass over all the samples.
b. "Reset Weights". When this button is pressed all weights should be reset to random numbers between -0.001 and +0.001.  and the display should be updated accordingly..
 
Drop-Down Selection Box
a. "Hidden Layer Transfer Function". A drop-down box to allow the user to select between two transfer functions for the hidden layer (Relu, and Sigmoid). Default: Relu
b. "Type of generated data". A drop-down box to allow the user to select between four different types of generated data. The possible choices are "s_curve", "blobs", "swiss_roll", and "moons". Default: s_curve. Examples of generated data are shown below.


Notes:
You should use a cross entropy loss, which uses the softmax function, to adjust the weights.
When your program starts it should automatically create the input data (with default values), randomize the weights, and display the sample points and class regions (with different colors).
The activation function of the output layer is linear.
Resolution of the displayed output should be 100 by 100
Make sure that you follow the submission guidelines to submit your code to Blackboard.
