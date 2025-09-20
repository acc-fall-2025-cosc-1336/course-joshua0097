def get_letter_grade(grade: int) -> str:
    """
    Converts a numerical grade to a letter grade.
    Uses standard US grading scale.
    Args:
        grade (int): Numerical grade (0-100)
    Returns:
        str: Letter grade (A, B, C, D, F)
    """
    if not (0 <= grade <= 100):
        return "out of range. Must be between 0 and 100."
    if   grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'
    
        