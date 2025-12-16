class Solution(object):
    def fizzBuzz(self, n):
        array = []
        for i in range(n):
            string = [str(i+1)]
            if (i+1) % 3 == 0:
                string = ["Fizz"]
            if (i+1) % 5 == 0:
                string = ["Buzz"]
            if (i+1) % 15 == 0:
                string = ["FizzBuzz"]
            array = array + string

        return array
        
