def quicksort(x):
      if len(x) < 2:
          return x
      else:
          pivot = x[0]
          less = [i for i in x[1:] if i <= pivot]
          greater = [i for i in x[1:] if i > pivot]
          return quicksort(less) + [pivot] + quicksort(greater)

class Mediana:

    def __init__(self, n=3):
        self.cola = [None for _ in range(n)]
        self.n = n

    def add(self, valor):
        for i in range(self.n-1, 0, -1):
            self.cola[i] = self.cola[i-1]
        self.cola[0] = valor

    def medicion(self):
        if self.cola[self.n-1] == None:
            return self.cola[0]
        return quicksort(self.cola)[(self.n-1)/2]
