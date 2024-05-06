import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def init_weights_biases(num_input_nodes, num_hidden_nodes, num_output_nodes):
    """
    Initialize weights and biases for the neural network.
    """
    parameter_dictionary = {}
    # Initialize weights and biases for the hidden layer
    parameter_dictionary["hidden_weights"] = np.random.randn(num_hidden_nodes, num_input_nodes)
    parameter_dictionary["hidden_biases"] = np.zeros((num_hidden_nodes, 1))
    # Initialize weights and biases for the output layer
    parameter_dictionary["output_weights"] = np.random.randn(num_output_nodes, num_hidden_nodes)
    parameter_dictionary["output_biases"] = np.zeros((num_output_nodes, 1))
    return parameter_dictionary

def forward_propagate(features, parameter_dictionary):
    hidden_layer_values = np.dot(parameter_dictionary["hidden_weights"], features) + parameter_dictionary["hidden_biases"]
    hidden_layer_outputs = sigmoid(hidden_layer_values)
    output_layer_values = np.dot(parameter_dictionary["output_weights"], hidden_layer_outputs) + parameter_dictionary["output_biases"]
    output_layer_outputs = sigmoid(output_layer_values)
    output_vals = {"hidden_layer_outputs": hidden_layer_outputs, "output_layer_outputs": output_layer_outputs}
    return output_vals

def backprop(feature_array, labels, output_vals, weights_biases_dict, verbose=False):
    num_examples = labels.shape[1]
    hidden_layer_outputs = output_vals["hidden_layer_outputs"]
    output_layer_outputs = output_vals["output_layer_outputs"]
    output_weights = weights_biases_dict["output_weights"]
    raw_error = output_layer_outputs - labels
    output_weights_gradient = np.dot(raw_error, hidden_layer_outputs.T) / num_examples
    output_bias_gradient = np.sum(raw_error, axis=1, keepdims=True) / num_examples
    blame_array = np.dot(output_weights.T, raw_error)
    hidden_outputs_squared = np.power(hidden_layer_outputs, 2)
    propagated_error = np.multiply(blame_array, 1 - hidden_outputs_squared)
    hidden_weights_gradient = np.dot(propagated_error, feature_array.T) / num_examples
    hidden_bias_gradient = np.sum(propagated_error, axis=1, keepdims=True) / num_examples
    gradients = {
        "hidden_weights_gradient": hidden_weights_gradient,
        "hidden_bias_gradient": hidden_bias_gradient,
        "output_weights_gradient": output_weights_gradient,
        "output_bias_gradient": output_bias_gradient
    }
    return gradients

def update_weights_biases(parameter_dictionary, gradients, learning_rate):
    updated_parameters = {}
    for key in parameter_dictionary.keys():
        if key in gradients:
            updated_parameters[key] = parameter_dictionary[key] - learning_rate * gradients[key]
        else:
            updated_parameters[key] = parameter_dictionary[key]
    return updated_parameters

def find_loss(output_layer_outputs, labels):
    num_examples = labels.shape[1]
    loss = (-1 / num_examples) * np.sum(np.multiply(labels, np.log(output_layer_outputs)) +
                                        np.multiply(1 - labels, np.log(1 - output_layer_outputs)))
    return loss

def train_neural_network(file_name, num_hidden_nodes, num_epochs, learning_rate):
    # Read file to array
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Skip the first row if it contains header information
    data = [line.strip().split() for line in lines[1:]]

    # Parse the remaining data
    features = np.array([[float(x) for x in row[:-1]] for row in data]).T
    labels = np.array([[float(row[-1])] for row in data]).T

    # Initialize weights and biases
    parameter_dictionary = init_weights_biases(num_input_nodes=2, num_hidden_nodes=num_hidden_nodes, num_output_nodes=1)

    # Train the network
    for epoch in range(num_epochs):
        # Forward propagation
        output_vals = forward_propagate(features, parameter_dictionary)
        # Calculate loss
        loss = find_loss(output_vals["output_layer_outputs"], labels)
        print(f"Epoch {epoch}: Loss = {loss}")
        # Backpropagation
        gradients = backprop(features, labels, output_vals, parameter_dictionary)
        # Update weights and biases
        parameter_dictionary = update_weights_biases(parameter_dictionary, gradients, learning_rate)

    return parameter_dictionary

if __name__ == "__main__":
    learning_rates = [0.3, 0.6, 0.1, 0.001]
    num_epochs = 10000  # You can adjust the number of epochs as needed

    for learning_rate in learning_rates:
        print(f"Training with learning rate: {learning_rate}")
        trained_parameters = train_neural_network("/eccs/home/ljanda22/CS365/lab-d/xor.txt", num_hidden_nodes=2, num_epochs=num_epochs, learning_rate=learning_rate)
        print("Trained parameters:", trained_parameters)
