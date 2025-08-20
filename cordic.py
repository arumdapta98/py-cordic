import math

def calculate_cordic_rotation(angle_rad, iterations=20, debug=False):
    """
    Calculates sine and cosine of an angle using the CORDIC algorithm in rotation mode.

    Args:
        angle_rad (float): The angle in radians for which to calculate sine and cosine.
        iterations (int): The number of iterations for the CORDIC algorithm.
                          More iterations lead to higher precision.

    Returns:
        tuple: A tuple containing (cosine, sine) of the input angle.
    """
    x = 1.0  # Initial x-component
    y = 0.0  # Initial y-component
    z = angle_rad  # Angle to rotate

    # Precompute arctan values for efficiency
    arctan_table = [math.atan(2**(-i)) for i in range(iterations)]

    if(debug):
        # show arctan_table
        print("i\ttheta(rad)\ttheta(deg)")
        for i,theta in enumerate(arctan_table):
            print("%d\t%.6f\t%.6f"%(i,theta,theta*360/(2*math.pi)))

    # Precompute the CORDIC gain factor K_n
    # K_n approaches 1/product(sqrt(1 + 2**(-2i)))
    Kn = 1.0
    for i in range(iterations):
        Kn *= (1 / math.sqrt(1 + 2**(-2 * i)))
    
    if(debug):
        print("Kn = %f"%Kn)

   
    # Calculate cordic rotation
    if(debug):
        print('{:<6}'.format("i")+'{:<21}'.format("x")+'{:<21}'.format("y")+'{:>25}'.format("z (rad)")+'{:>30}'.format("z (deg)"))
        print(f"{i==0:<5} {x:<20} {y:<20} {z:>30} {math.degrees(z):>30}")
    for i in range(iterations):
        # Determine the direction of rotation
        if z > 0:
            d = 1  # Clockwise rotation
        else:
            d = -1 # Counter-clockwise rotation

        # Apply the CORDIC rotation
        x_new = x - d * y * (2**(-i))
        y_new = y + d * x * (2**(-i))
        z_new = z - d * arctan_table[i]

        x = x_new
        y = y_new
        z = z_new

        if(debug):
            print(f"{i+1:<5} {x:<20} {y:<20} {z:>30} {math.degrees(z):>30}")

    # Apply the CORDIC gain factor
    return x * Kn, y * Kn


