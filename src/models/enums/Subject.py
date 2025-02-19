from enum import Enum


class Subject(Enum):
    """
    Enum representing subjects to be tutored in.
    """
    # Humanities
    EN_READ = 'English Reading'
    EN_WRIT = 'English Writing'
    HIST = 'History'

    # Math
    MATH2ALG = 'Math to Algebra'
    GEO = 'Geometry'
    CALC = 'Calculus'

    # Sciences
    BIO = 'Biology'
    CHEM = 'Chemistry'
    PHYSICS = 'Physics'
    CS = 'Computer Science'

    # Languages
    SPANISH = 'Spanish'
    FRENCH = 'French'
    CHINESE = 'Chinese'

    # SAT Categories
    SAT = 'SAT All'
    SAT_MATH = 'SAT Math'
    SAT_READ = 'SAT Reading'
    SAT_WRIT = 'SAT Writing'

    # ACT Categories
    ACT = 'ACT ALL'
    ACT_ENG = 'ACT English'
    ACT_READ = 'ACT Reading'
    ACT_WRIT = 'ACT Writing'
    ACT_SCI = 'ACT Science'
    ACT_MATH = 'ACT Math'

    COLLEGE_APP = 'College Applications'