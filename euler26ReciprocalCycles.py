#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def ReciprocalCycles(n):
    #n is the number below which we need to check the longest recurring cycle
    max_number = 0
    final_answer = 1
    for number in range(1, n):
        
        new_list = []
        x = 1
        Remainder = 0
        recurring_number = 0
        while Remainder not in new_list:
            new_list.append(Remainder)
            Remainder = x % number
            x = Remainder*10
            
            recurring_number += 1
        if max_number < recurring_number:
            max_number = recurring_number
            final_answer = number
    return final_answer

final = ReciprocalCycles(1000)
print(final)

        
        