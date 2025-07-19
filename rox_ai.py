import numpy
from turtle import*



def ai():

     def sigmoid(x):
          return 1/ (1 + numpy.exp(-x))

     trainig_inputs = numpy.array([[1,1,1],
                                   [1,1,1],
                                   [1,1,1],
                                   [1,1,1]])

     trainig_outputs = numpy.array([[1,1,1,1]]).T

     numpy.random.seed(1)
     synaptic_weights = 2 * numpy.random.random((3,1)) - 1
     print('Рандомні ваги: ')

                                   
     print(synaptic_weights)
     for i in range(20000):
          input_layer = trainig_inputs
          outputs = sigmoid(numpy.dot(input_layer,synaptic_weights))
          zero = trainig_outputs - outputs
          sdjustments = numpy.dot(input_layer.T,zero * (outputs * (1 - outputs)))

          synaptic_weights += sdjustments


     print('Ваги після вивчення')
     print(synaptic_weights)

     print('Результат після вивчення:')
     print(outputs)


     out =  sum(outputs)/4
     print(out)
     rox_graffic = Turtle()
     if out == 0.5:
          rox_graffic.forward(100)
          rox_graffic.color('red')
     elif out >= 0.5:
          rox_graffic.left(90)
          rox_graffic.color('green')
          rox_graffic.forward(100)
     elif out <= 0.5:
          rox_graffic.right(90)
          rox_graffic.color('black')
          rox_graffic.forward(100)
print('Rox ai')
ai()


def ai2():
     def sigmoid(x):
          return 1 / (1 + numpy.exp(-x))

     trainig_inputs = numpy.array([[0, 1, 1],
                                   [1, 1, 0],
                                   [1, 1, 1],
                                   [0, 0, 0]])

     trainig_outputs = numpy.array([[0, 1, 0, 1]]).T

     numpy.random.seed(1)
     synaptic_weights = 2 * numpy.random.random((3, 1)) - 1
     print('Нові рандомні ваги: ')

     print(synaptic_weights)
     for i in range(20000):
          input_layer = trainig_inputs
          outputs = sigmoid(numpy.dot(input_layer, synaptic_weights))
          zero = trainig_outputs - outputs
          sdjustments = numpy.dot(input_layer.T, zero * (outputs * (1 - outputs)))

          synaptic_weights += sdjustments

     print('Нові ваги після вивчення')
     print(synaptic_weights)

     print('Новий результат після вивчення:')
     print(outputs)


print('  ')
print('  ')
print('  ')
print('  ')

ai2()