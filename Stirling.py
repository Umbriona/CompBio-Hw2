def stirling1 ( n, m ):
  n = int(n)
  m = int(m)
#
  import numpy as np

  s1 = np.zeros ( (n,m) )

  if ( n <= 0 ):
    return s1

  if ( m <= 0 ):
    return s1

  s1[0,0] = 1
  for j in range ( 1, m ):
    s1[0,j] = 0

  for i in range ( 1, n ):

    s1[i,0] = - i * s1[i-1,0]

    for j in range ( 1, m ):
      s1[i,j] = s1[i-1,j-1] - i * s1[i-1,j]

  return s1[n-1,m-1]