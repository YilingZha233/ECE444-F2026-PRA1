class utils:
    # Reverse function that takes in integer and output reversed integer
    def reversed (self, number):
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError("Input type should be an integer")
        sign = 1 if number > 0 else (-1)
        number = abs(number)
        # Reversed the string version of integer number
        reversed_number = int(str(number)[::-1])
        return sign * reversed_number
    
    def formatter (self, number):
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError("Input type should be an integer")
        # return integer in base2 and base8
        return bin(number), oct(number)
    
        
        