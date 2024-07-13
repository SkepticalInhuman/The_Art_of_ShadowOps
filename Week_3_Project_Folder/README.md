# Week 3

## Pretrained Models
Used pretrained VGG16 and InceptionnetV3 to classify images as fake or real from the xhlulu/real and fake faces dataset. Images were first rescaled Pretrained models were first loaded without their top classification layer. The output from the pretrained cnn is then flattened and fed into a neural network with 512 neurons with a dropout rate of 0.5 so as to prevent overfitting which is then fed into the output layer with one node and sigmoid activation. The layers of the pretrained model is frozen during training and only the weights of the classification layer is allowed to update. Fine tuning with top layers of the pretrained  cnn took was taking considerable amount of time to train thus all layers were frozen. Number of epoch was set to 1 since larger number of epoch would take a lot of time. Binary cross entropy was chosen as the loss function and Adam optimizer with a learning rate of 0.001 as the optimizer.

## Custom model
Built a custom inceptionnetV1 to classify fake and real images of the same dataset. An inception module is defined has convolution layers of various kernels and a max pooling layer, the outputs of all these layers are concatenated. This architecture of wider layer instead of deeper layer allows to capture different details obtained by different kernels and allows to capture features at different scales. The inceptionnet architecture is then defined making use of inception modules. Output from the inceptionnet is then fed into the neural network similar to the one used in the pretrained models case.

