def calculate_offset(reference_x, detected_x):
    """
    Returns horizontal distance between frame center and object center.
    """
    return detected_x - reference_x

def generate_command(offset, tolerance=40):
    """
    Returns movement command based on offset.
    """
    if abs(offset) <= tolerance:
        return "FORWARD"
    elif offset < 0:
        return "MOVE LEFT"
    else:
        return "MOVE RIGHT"
