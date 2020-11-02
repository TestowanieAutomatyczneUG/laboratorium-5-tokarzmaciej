class Hamming():
    def distance(self, A, B):
        if len(A) == len(B) and A == B and len(A)<10:
            return 0
        elif A != B:
            return 1
