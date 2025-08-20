import math
from cordic import *

def evaluate_cordic_calculation(angle_degrees, iterations, debug):
    angle_radians = math.radians(angle_degrees)
    cos_val, sin_val = calculate_cordic_rotation(angle_radians, iterations, debug)

    print("")
    print(f"Angle: {angle_degrees} degrees ({angle_radians:.4f} radians) - iterations: {iterations}")
    print(f"CORDIC Sine: {sin_val:.10f}")
    print(f"CORDIC Cosine: {cos_val:.10f}")
    print(f"Math.sin: {math.sin(angle_radians):.10f}")
    print(f"Math.cos: {math.cos(angle_radians):.10f}")
    print(f"Error Sine: {abs(sin_val-math.sin(angle_radians)):.10f}")
    print(f"Error Cosine: {abs(cos_val-math.cos(angle_radians)):.10f}")


    


if __name__ == "__main__":
    print("Demo CORDIC Algorithm")
    evaluate_cordic_calculation(angle_degrees = 30, iterations=10, debug=False)
    evaluate_cordic_calculation(angle_degrees = 30, iterations=20, debug=False)
    evaluate_cordic_calculation(angle_degrees = 30, iterations=30, debug=False)
    evaluate_cordic_calculation(angle_degrees = 30, iterations=40, debug=False)
    
    #evaluate_cordic_calculation(angle_degrees = 45, iterations=20, debug=False)
    #evaluate_cordic_calculation(angle_degrees = 60, iterations=20, debug=False)
    

