def bounded_int_exclusive(low, high):
    def checker(value):
        return value > low and value < high

    return checker

def bounded_int_inclusive(low, high):
    def checker(value):
        return value >= low and value <= high

    return checker

def valid_port():
    return bounded_int_inclusive(1, 65535)
