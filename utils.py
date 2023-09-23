class utils:
    @staticmethod
    def reverse (num: int):
        #check that int
        if (not isinstance(num, int) or isinstance(num, bool)):
            raise ValueError("Expected an integer")
        #reverse
        num = str(num)[::-1]
        num = int(num)
        return num
    @staticmethod
    def formatter (num: int):
        #chec that int
        if (not isinstance(num, int) or isinstance(num, bool)):
            raise ValueError("Expected an integer")
        #base 2 and 8    
        bin_num = bin(num)
        oct_num = oct(num)
        return (bin_num, oct_num)

