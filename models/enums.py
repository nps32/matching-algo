from enum import Enum

class Cycle(Enum):
    FALL23 = 'Fall 2024'
    SPR24 = 'Spring 2023'
    FALL24 = 'Fall 2024'

class Day(Enum): 
    MON = 'Monday'
    TUE = 'Tuesday'
    WED = 'Wednesday'
    THURS = 'Thursday'
    FRI = 'Friday'
    SAT = 'Saturday'
    SUN = 'Sunday'

class Subject(Enum): 
    #Humanities 
    EN_READ = 'English Reading'
    EN_WRIT = 'English Writing'
    HIST = 'History'

    #Math
    MATH2ALG = 'Math to Algebra'
    GEO = 'Geometry'
    CALC = 'Calculus'
   

    #Sciences 
    BIO = 'Biology'
    CHEM = 'Chemistry'
    PHYSICS = 'Physics'
    CS = 'Computer Science'

    #Languages 
    SPANISH = 'Spanish'
    FRENCH = 'French'
    CHINESE = 'Chinese'
    
    #SAT Categories
    SAT = 'SAT All'
    SAT_MATH = 'SAT Math'
    SAT_READ = 'SAT Reading'
    SAT_WRIT = 'SAT Writing'

    #ACT Categories 
    ACT = 'ACT ALL'
    ACT_ENG = 'ACT English'
    ACT_READ = 'ACT Reading'
    ACT_WRIT = 'ACT Writing'
    ACT_SCI = 'ACT Science'
    ACT_MATH = 'ACT Math'
    
    COLLEGE_APP = 'College Applications'
