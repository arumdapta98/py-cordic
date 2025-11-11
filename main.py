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


def float_to_int16(value):
    """
    Converts a float in the range [-1, 1] to a 16-bit signed integer.
    """
    if not (-1 <= value <= 1):
        raise ValueError("Input float must be within the range [-1, 1]")

    # Max value for a 16-bit signed integer
    max_int16 = 32767

    # Scale the float and round to the nearest integer
    scaled_value = value * max_int16
    return int(round(scaled_value))

def to_twos_complement_binary(num, bits):
    """
    Converts an integer to its two's complement binary string representation.

    Args:
        num (int): The integer to convert.
        bits (int): The number of bits for the two's complement representation.

    Returns:
        str: The two's complement binary string.
    """
    if num >= 0:
        # For positive numbers, simply convert to binary and pad with zeros
        binary_str = bin(num)[2:].zfill(bits)
    else:
        # For negative numbers, calculate the two's complement value
        # This effectively performs (2^bits + num)
        twos_complement_val = (1 << bits) + num
        binary_str = bin(twos_complement_val)[2:].zfill(bits)
    return binary_str


def get_sin_cosine_value(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    f_sin_value = math.sin(angle_radians)
    f_cosine_value = math.cos(angle_radians)

    # i_sin_value = int(f_sin_value*(2**16))
    # i_cosine_value = int(f_cosine_value*(2**16))

    i_sin_value = float_to_int16(f_sin_value)
    i_cosine_value = float_to_int16(f_cosine_value)

    

    print(f"{angle_degrees} \t\t{angle_radians:.4f} \t\t{f_sin_value:.3f} ({i_sin_value:05d})\
              \t {to_twos_complement_binary(i_sin_value,16)} \t{f_cosine_value:.3f} ({i_cosine_value:05d})\
                      \t {to_twos_complement_binary(i_cosine_value,16)}")


if __name__ == "__main__":
    print("Demo CORDIC Algorithm")
    degrees = [0,30,45,60,90,120,135,150,180,210,225,240,270,300,315,330,360]

    print("Angle (deg)\tAngle (rad)\tSin\t\t\t\t\t\tCosine")
    for degree in degrees:
        get_sin_cosine_value(degree)




    # evaluate_cordic_calculation(angle_degrees = 30, iterations=10, debug=False)
    # evaluate_cordic_calculation(angle_degrees = 30, iterations=20, debug=False)
    # evaluate_cordic_calculation(angle_degrees = 30, iterations=30, debug=False)
    # evaluate_cordic_calculation(angle_degrees = 30, iterations=40, debug=False)
    
    #evaluate_cordic_calculation(angle_degrees = 45, iterations=20, debug=False)
    #evaluate_cordic_calculation(angle_degrees = 60, iterations=20, debug=False)
    

