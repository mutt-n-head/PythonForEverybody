from numpy import dot, exp, array, random


class NeuralNet:

    def __init__(self):
        random.seed(1)
        self.synaptic_weights = 2 * random.random((3, 1)) - 1

    def __sigmoid(self, x):
        return 1/(1 + exp(-x))

    def __gradient(self, x):
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, num_of_passes):

        # Need to calculate the dot product to get initial value.
        for iteration in range(num_of_passes):
            # outputs = dot(training_inputs, self.synaptic_weights)
            # outputs = self.__sigmoid(outputs)
            outputs = self.think(training_inputs)

            # Calculate the error of it.
            error = training_outputs - outputs

            # Get gradient adjusted outputs
            gradient_adj_outputs = self.__gradient(outputs)

            # Multiply the error times the gradient adj outputs
            error_with_gradient = error * gradient_adj_outputs

            # Derive adjust array
            adjustments = dot(training_inputs.T, error_with_gradient)
            self.synaptic_weights += adjustments

    def think(self, inputs):
        # Pass inputs through our neural network (our single neuron).
        # return self.__sigmoid(dot(inputs, self.synaptic_weights))
        outputs = dot(inputs, self.synaptic_weights)
        outputs = self.__sigmoid(outputs)

        return outputs


neural_network = NeuralNet()
training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T

neural_network.train(training_set_inputs, training_set_outputs, 10000)

print('New weights are ', neural_network.synaptic_weights)
print("Considering new situation [1, 0, 0] -> ?: ", neural_network.think(array([1, 0, 0])))
