class Hamming():
    def distance(self, A, B):
        counter = 0
        for position in range(len(A)):
            if len(A[position]) == len(B[position]) and A[position] != B[position]:
                counter += 1
        return counter
