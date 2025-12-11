class Solution(object):
    def divide(self, dividend, divisor):
        abs_divid = abs(dividend)
        abs_divis = abs(divisor)
        signed = False
        min_range, max_range = -2**31, 2**31-1

        if abs_divid != dividend:
            signed = not signed
        if abs_divis != divisor:
            signed = not signed
        count = abs_divid // abs_divis if not signed else -(abs_divid // abs_divis)
        if count < min_range:
            return min_range
        elif count > max_range:
            return max_range
        return count
        
        """ if dividend == 0:
            return 0 
        min_range, max_range = -2**31, 2**31-1
        count = 0
        signed = False

        if divisor == 1:
            if dividend < min_range:
                return min_range
            elif dividend > max_range:
                return max_range
            else:
                return dividend
        elif divisor == -1:
            dividend = -dividend
            if dividend < min_range:
                return min_range
            elif dividend > max_range:
                return max_range
            else:
                return dividend
            

        abs_divid = abs(dividend)
        abs_divis = abs(divisor)

        if abs_divid != dividend:
            signed = not signed
        if abs_divis != divisor:
            signed = not signed

        

        while abs_divid >= abs_divis:
            abs_divid = abs_divid - abs_divis
            count += 1
        count = count if not signed else -count
        if count < min_range:
            return min_range
        elif count > max_range:
            return max_range
        return count
        """
        
