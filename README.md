# Back Propogation Neural Network

The purpose of the this assignment is to practice with back-propagation neural networks.

## __Description__
 
Implement a fully-connected back-propagation network using TensorFlow.   
(DO NOT use any other package such as Keras or Estimator):
Your network should include one hidden layer and one output layer.   
The input for the neural network is a two-dimensional data set which presents sample points from different classes. Use the provided sample program to create the data set(s).  

Your program should display sample points and the regions for each class with different colors.  
Your program should include the following `sliders, buttons, and drop-down box`.
## Sliders:

   1. **"Alpha"**: (Learning rate) Range should be between ` 0.000 and 1.0`. Default value = 0.1 increments=.001
   2. **"Lambda"**: (Weight regularization). Range should be between ` 0.0 and 1.0.`  Default value = 0.01 Increments=0.01
   3. **"Num. of Nodes in Hidden Layer"**: Range ` 1 to 500` . Default value=100  increment=1
   4. **"Number of Samples"**: This slider determines the number of samples which will be generated for input data. Range ` 4 to 1000`. Default value=200, increment=1.
   5. **"Number of Classes"**: This slider determines the number of classes which will be generated for input data. Range ` 2 to 10`. Default value=4 Increments=1


### __Buttons__:  

   1. **"Adjust Weights (Train)"**: When this button is pressed the training should be applied for 10 epochs. and the display should be updated after each epoch. (an epoch is one pass over all the samples.
   2. **"Reset Weights"**. When this button is pressed all weights should be reset to random numbers between -0.001 and +0.001.  and the display should be updated accordingly..
 
## __Drop-Down Selection Box__:  

   1. **"Hidden Layer Transfer Function"**. A drop-down box to allow the user to select between two transfer functions for the hidden layer (Relu, and Sigmoid). Default: Relu
   2. **"Type of generated data"**. A drop-down box to allow the user to select between four different types of generated data. The possible choices are ` "s_curve", "blobs", "swiss_roll", and "moons" `. Default: ` s_curve. ` Examples of generated data are shown below.

![s_curve](https://raw.githubusercontent.com/pyk18/Back-Propogation-Neural-Network/master/picture/readme/s_curve.png)
![swiss_roll](https://raw.githubusercontent.com/pyk18/Back-Propogation-Neural-Network/master/picture/readme/swiss_roll.png)
![blob](https://raw.githubusercontent.com/pyk18/Back-Propogation-Neural-Network/master/picture/readme/blob.png)
![moon](https://raw.githubusercontent.com/pyk18/Back-Propogation-Neural-Network/master/picture/readme/moon.png)

## __Notes__:  
>You should use a `cross entropy loss`, which uses the `softmax function`, to adjust the weights.
When your program starts it should 
> - [x] Automatically create the input data (with default values).
> - [x] Randomize the weights.
> - [x] Display the sample points and class regions (with different colors).
> - [x] The activation function of the output layer is linear.  
> - [x] Resolution of the displayed output should be 100 by 100  
> - [x] Make sure that you follow the submission guidelines to submit your code to Blackboard.
