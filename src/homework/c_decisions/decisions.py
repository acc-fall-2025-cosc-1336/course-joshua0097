def get_letter_grade_if(grade: int) -> str:
    """
    Converts a numerical grade to a letter grade using if-elif-else statements.
    Args:
        grade (int): Numerical grade (0-100)
    Returns:
        str: Letter grade (A, B, C, D, F)
    """
    if not (0 <= grade <= 100):
        return "Out of range. Must be between 0 and 100."
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
def get_letter_grade_switch(grade: int) -> str:
    """
    Converts a numerical grade to a letter grade using a switch-like approach.
    Args:
        grade (int): Numerical grade (0-100)
    Returns:
        str: Letter grade (A, B, C, D, F)
    """
    if not (0 <= grade <= 100):
        return "Out of range. Must be between 0 and 100."
    switcher = {
        range(90, 101): 'A',
        range(80, 90): 'B',
        range(70, 80): 'C',
        range(60, 70): 'D',
        range(0, 60): 'F'
    }
    
    for key in switcher:
        if grade in key:
            return switcher[key]
    
    return "Invalid grade"    
        