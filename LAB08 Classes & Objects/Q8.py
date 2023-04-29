''' A geometric sequence is a special type of sequence where the ratio of every two successive terms is a constant.
        - This ratio is known as a common ratio of the geometric sequence
        - Every term is multiplied by a constant which results in its next term
        - Geometric sequence form: a, a*r, a*r^2 
            where 'a' is the first term 
            where 'r' is the common ratio of the sequence.
        - The common ratio can either be a positive or a negative number. '''
import random
random.seed(30)

class GeometricSequence: 
    # first_term = 1 -> default
    # common ratio = 2 -> default

    def __init__(self, first_term = 1, common_ratio = 2):
        self.first_term = first_term
        self.common_ratio = common_ratio

sequence1 = GeometricSequence(0.25, 0.5)
print(type(sequence1))
print(sequence1.first_term)
print(sequence1.common_ratio)
sequence2 = GeometricSequence()
print(sequence2.first_term, sequence2.common_ratio)
print(sequence1 == sequence2)

sequence2 = GeometricSequence(-4, -0.5)
print(sequence2.first_term, sequence2.common_ratio)