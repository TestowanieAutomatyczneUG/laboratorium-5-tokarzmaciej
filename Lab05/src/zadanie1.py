class Hamming():
    def distance(self, A, B):
        if len(A) == len(B) and A == B:
            return 0
