from typing import Any, Dict, List
from src.models.enums.Day import Day
from src.models.enums.Subject import Subject
from src.models.enums.Cycle import Cycle
from src.models.enums.Grade import Grade
from src.models.tuteeApp import TuteeApp
from src.models.fellowApp import FellowApp


def convertCycle(cycle : str) -> Cycle: 

    cycle_mapping = {"2bb261dd-2968-4c5b-bd05-731eaa7c3c87":Cycle.TEST, 
                     "613958f3-cd19-4604-902b-4fffacf28672":Cycle.SPR24}

    if cycle in cycle_mapping: 
        return cycle_mapping[cycle] 
    else: 
        print(f"Warning: cycle '{cycle}' did not convert correctly. Returning null.")   
        return None 


def convertGrades(grades : List[str]) -> List[Grade]: 
    
    grade_mapping = {'lowerElementary':Grade.LE, 
                     'higherElementary':Grade.HE, 
                     'middle':Grade.MI, 
                     'highSchool':Grade.HS}
    
    res = [] 
    for grade in grades: 
        if grade in grade_mapping:
            res.append(grade_mapping[grade])
        else: 
            print(f"Warning: grade '{grade}' did not convert correctly. Skipping.")

    return res 


def convertGrade(grade : str) -> Grade: 
    
    grade_mapping = {'lowerElementary':Grade.LE, 
                     'higherElementary':Grade.HE, 
                     'middle':Grade.MI, 
                     'highSchool':Grade.HS} 
    
    if grade in grade_mapping: 
        return grade_mapping[grade]
    else: 
        print(f"Warning: grade '{grade}' did not convert correctly. Returning null.")
        return None 


def convertAvailability(availability : List[str]) -> List[Day]: 
    
    day_mapping = {'Monday':Day.MON, 
                   'Tuesday':Day.TUE, 
                   'Wednesday':Day.WED, 
                   'Thursday':Day.THURS, 
                   'Friday':Day.FRI, 
                   'Saturday':Day.SAT, 
                   'Sunday':Day.SUN}
    
    res = [] 
    for day in availability:
        if day in day_mapping: 
            res.append(day_mapping[day])
        else: 
            print(f"Warning: Day '{day}' did not convert correctly. Skipping.")
    return res 


def convertSubjects(subjects : List[str]) -> List[Subject]: 
    
    subject_mapping = {
        'englishReading': Subject.EN_READ,
        'englishWriting': Subject.EN_WRIT,
        'history': Subject.HIST,
        'mathToAlgebra': Subject.MATH2ALG,
        'geometry': Subject.GEO,
        'calculus': Subject.CALC,
        'biology': Subject.BIO,
        'chemistry': Subject.CHEM,
        'physics': Subject.PHYSICS,
        'computerScience': Subject.CS,
        'spanish': Subject.SPANISH,
        'french': Subject.FRENCH,
        'chinese': Subject.CHINESE,
        'satAll': Subject.SAT,
        'satMath': Subject.SAT_MATH,
        'satReading': Subject.SAT_READ,
        'satWriting': Subject.SAT_WRIT,
        'actAll': Subject.ACT,
        'actEnglish': Subject.ACT_ENG,
        'actReading': Subject.ACT_READ,
        'actWriting': Subject.ACT_WRIT,
        'actScience': Subject.ACT_SCI,
        'actMath': Subject.ACT_MATH,
        'collegeApplications': Subject.COLLEGE_APP
    }
    
    res = []
    for subject in subjects:
        if subject in subject_mapping:
            res.append(subject_mapping[subject])
    
    return res


def convertSubject(subject : str) -> Subject: 
    
    subject_mapping = {
        'englishReading': Subject.EN_READ,
        'englishWriting': Subject.EN_WRIT,
        'history': Subject.HIST,
        'mathToAlgebra': Subject.MATH2ALG,
        'geometry': Subject.GEO,
        'calculus': Subject.CALC,
        'biology': Subject.BIO,
        'chemistry': Subject.CHEM,
        'physics': Subject.PHYSICS,
        'computerScience': Subject.CS,
        'spanish': Subject.SPANISH,
        'french': Subject.FRENCH,
        'chinese': Subject.CHINESE,
        'satAll': Subject.SAT,
        'satMath': Subject.SAT_MATH,
        'satReading': Subject.SAT_READ,
        'satWriting': Subject.SAT_WRIT,
        'actAll': Subject.ACT,
        'actEnglish': Subject.ACT_ENG,
        'actReading': Subject.ACT_READ,
        'actWriting': Subject.ACT_WRIT,
        'actScience': Subject.ACT_SCI,
        'actMath': Subject.ACT_MATH,
        'collegeApplications': Subject.COLLEGE_APP
    }
    
    if subject in subject_mapping:
        return subject_mapping[subject]
    else: 
        print(f"Warning: Subject '{subject}' did not convert correctly. Returning null.")
        return None 


def convertJsonToFellows(data: Dict[str, Any]) -> List[FellowApp]: 

    fellows = []

    for item in data['dataItems']:
        data = item.get('data', {})
        fellow = FellowApp(
            id = item.get('id', None), 
            cycle = convertCycle(data.get('cycle', None)),
            availability = convertAvailability(data.get('availabilities', [])),
            grades = convertGrades(data.get('gradeLevels', [])),
            subjects = convertSubjects(data.get('subjects', [])), 
            match_count = data.get('matchCount', None),
            capacity = data.get('tuteeCapacity', None),
            returning = data.get('isReturningFellow', False),
            wants_prev_tutee = data.get('wantsPreviousTutee', False),
            prev_tutee_name = data.get('previousTuteeName', None), 
            prev_tutee_id = data.get('previousTuteeId', None)
        )
        fellows.append(fellow)

    return fellows


def convertJsonToTutees(data: Dict[str, Any]) -> List[TuteeApp]:
    tutees = []

    for item in data['dataItems']:
        data = item.get('data', {})
        tutee = TuteeApp(
            id = item.get('id', None),
            cycle = convertCycle(data.get('cycle', Cycle.TEST)),
            availability = convertAvailability(data.get('availabilities', [])),
            grade = convertGrade(data.get('studentGrade', None)),
            subject1 = convertSubject(data.get('subject1', None)),
            eval1 = data.get('evaluation1', None),
            subject2 = convertSubject(data.get('subject2', None)),
            eval2 = data.get('evaluation2', None),
            subject3 = convertSubject(data.get('subject3', None)),
            eval3 = data.get('evaluation3', None),
            match_count = data.get('matchCount', 0),
            capacity = data.get('subjectCount', 0),
            wants_prev_fellow = data.get('wantsPreviousFellow', False),
            prev_fellow_name = data.get('previousFellowName', None),
            prev_fellow_id = data.get('previousFellowEmail', None)
        )
        tutees.append(tutee)

    return tutees