# Making a random change so I can add comments to the file on GitHub

from typing import Any, Dict, List
from src.models.enums.Day import Day
from src.models.enums.Subject import Subject
from src.models.enums.Cycle import Cycle
from src.models.enums.Grade import Grade
from src.models.match import Match
from src.models.tuteeApp import TuteeApp
from src.models.fellowApp import FellowApp

cycle_mapping = {"2bb261dd-2968-4c5b-bd05-731eaa7c3c87":Cycle.TEST, 
                 "613958f3-cd19-4604-902b-4fffacf28672":Cycle.SPR24}

grade_mapping = {'lowerElementary':Grade.LE, 
                 'higherElementary':Grade.HE, 
                 'middle':Grade.MI, 
                 'highSchool':Grade.HS}

day_mapping = {'Monday':Day.MON, 
               'Tuesday':Day.TUE, 
               'Wednesday':Day.WED, 
               'Thursday':Day.THURS, 
               'Friday':Day.FRI, 
               'Saturday':Day.SAT, 
               'Sunday':Day.SUN}

subject_mapping = {'englishReading': Subject.EN_READ,
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
                   'collegeApplications': Subject.COLLEGE_APP}


def convertCycle(cycle : str) -> Cycle: 

    if cycle in cycle_mapping: 
        return cycle_mapping[cycle] 
    else: 
        print(f"Warning: cycle '{cycle}' did not convert correctly. Returning null.")   
        return None 


def convertGrades(grades : List[str]) -> List[Grade]: 
    
    res = [] 
    for grade in grades: 
        if grade in grade_mapping:
            res.append(grade_mapping[grade])
        else: 
            print(f"Warning: grade '{grade}' did not convert correctly. Skipping.")

    return res 


def convertGrade(grade : str) -> Grade: 
    
    if grade in grade_mapping: 
        return grade_mapping[grade]
    else: 
        print(f"Warning: grade '{grade}' did not convert correctly. Returning null.")
        return None 


def convertAvailability(availability : List[str]) -> List[Day]: 
    
    res = [] 
    for day in availability:
        if day in day_mapping: 
            res.append(day_mapping[day])
        else: 
            print(f"Warning: Day '{day}' did not convert correctly. Skipping.")
    return res 


def convertSubjects(subjects : List[str]) -> List[Subject]: 
    
    res = []
    for subject in subjects:
        if subject in subject_mapping:
            res.append(subject_mapping[subject])
    
    return res


def convertSubject(subject : str) -> Subject: 
    
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

def convertMatchesToJson(matches : List[Match]) -> List[Any]: 
    reverse_cycle_mapping = {value: key for key, value in cycle_mapping.items()}
    reverse_grade_mapping = {value: key for key, value in grade_mapping.items()}
    reverse_subject_mapping = {value: key for key, value in subject_mapping.items()}

    res = [] 

    for match in matches: 
        res.append({
            'data':{
                'tuteeApplication': match.tutee_id, 
                'fellowApplication': match.tf_id, 
                'cycle': reverse_cycle_mapping[match.cycle], 
                'subject': reverse_subject_mapping[match.subject], 
                'grade': reverse_grade_mapping[match.grade]
            }
        })

    return res 


def updateAppsJson(data: Dict[str, Any], apps: List[Any]) -> Dict[str, Any]: 
    
    appDict = {app.id: app for app in apps}

    # Iterate through the JSON data and update matching fields
    for item in data["dataItems"]:
        appId = item.get("id")
        if appId in appDict:
            app = appDict[appId]
            item["data"]["capacity"] = app.capacity
            item["data"]["matchCount"] = app.match_count

    return data['dataItems']
