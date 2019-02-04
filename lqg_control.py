import numpy
from scipy import linalg

def GetLQGController( A, B, C, ro ):
  """Solve the discrete time lqr controller.
   
  x[k+1] = A*x[k] + B*u[k]
    
  cost = sum x[k].T*Q*x[k] + u[k].T*R*u[k]
  """
  #ref Bertsekas, p.151
 
  Q = numpy.dot( numpy.transpose( C ), C )
  R = ro * numpy.eye( len(B[ 0 ]) )
  #first, try to solve the ricatti equation
  X = linalg.solve_discrete_are( A, B, Q, R )
  #compute the LQR gain
  G = linalg.inv( numpy.transpose( B ) @ X @ B + R ) @ ( numpy.transpose( B ) @ X @ A )
  
  return G


if __name__ == '__main__':
  A = numpy.matrix( [ [ 0, 1 ], [ 0, 0 ] ] )
  B = numpy.matrix( [ [ 0.5 ], [ 0.5 ] ] )
  C = numpy.matrix( [ [ 1, 0 ] ] )
  controller = GetLQGController( A, B, C )
