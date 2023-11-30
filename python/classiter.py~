import math

class NextPrime:

    def __init__(self):

        self.k=1


    def __next__(self):
        
        while True:
            self.k=self.k+1
            for d in range(2,int(math.sqrt(self.k))+1):
                if self.k%d == 0:
                    break
            else:
                return self.k



class PrimeIterator:

    def __iter__(self):

        return NextPrime()

