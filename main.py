import math

mean = 41.46153846
standard = 12.64068757

intervals = 50 #    ONLY THIS NEEDS TO CHANGE, NOTHING ELSE FOR THE INTERVALS
width = (2*standard)/intervals

def function(val, mean=mean, standard=standard):
    answer = (1/standard) * (1/math.sqrt(math.pi * 2))
    
    answer *= (math.e)**(-0.5 * (((val-mean)/standard)**2))
    
    return answer * width
    

rightRiemann = mean+standard

values = []


while intervals > 0:
    values.append(rightRiemann)
    rightRiemann -= width
    intervals -= 1



print(sum(list(map(function, values))))

