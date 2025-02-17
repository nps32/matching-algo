"""
The functions defined in this file are used by the requester class to interact with JSON request data, 
serializing TuteeApp and FellowApp objects for matching and de-serializing TuteeApp, FellowApp, & Match
objects to update the Wix CMS. 
"""

from typing import Any, Dict, List
from src.models.enums.Day import Day
from src.models.enums.Subject import Subject
from src.models.enums.Cycle import Cycle
from src.models.enums.Grade import Grade
from src.models.match import Match
from src.models.tuteeApp import TuteeApp
from src.models.fellowApp import FellowApp

# Mappings for converting string identifiers to enum values
cycle_mapping = {
    '2bb261dd-2968-4c5b-bd05-731eaa7c3c87': Cycle.TEST,
    '613958f3-cd19-4604-902b-4fffacf28672': Cycle.SPR24
}

grade_mapping = {
    'lowerElementary': Grade.LE,
    'higherElementary': Grade.HE,
    'middle': Grade.MI,
    'highSchool': Grade.HS
}

day_mapping = {
    'Monday': Day.MON,
    'Tuesday': Day.TUE,
    'Wednesday': Day.WED,
    'Thursday': Day.THURS,
    'Friday': Day.FRI,
    'Saturday': Day.SAT,
    'Sunday': Day.SUN
}

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


def convertCycle(cycle: str) -> Cycle:
    """
    Converts a string identifier to a Cycle enum
    """
    if cycle in cycle_mapping:
        return cycle_mapping[cycle]
    raise ValueError(f"'{cycle}' cannot be converted to a Cycle enum.")


def convertGrades(grades: List[str]) -> List[Grade]:
    """
    Converts a list of grade level strings to a list of Grade enums.
    """
    return [grade_mapping[grade] if grade in grade_mapping else 
            ValueError(f"'{grade}' cannot be converted to a Grade enum.") for grade in grades]


def convertGrade(grade: str) -> Grade:
    """
    Converts a single grade level string to a Grade enum.
    """
    if grade in grade_mapping:
        return grade_mapping[grade]
    raise ValueError(f"'{grade}' cannot be converted to a Grade enum.")


def convertAvailability(availability: List[str]) -> List[Day]:
    """
    Converts a list of availability day strings to a list of Day enums.
    """
    return [day_mapping[day] if day in day_mapping else 
            ValueError(f"'{day}' cannot be converted to a Day enum.") for day in availability]


def convertSubjects(subjects: List[str]) -> List[Subject]:
    """
    Converts a list of subject strings to a list of Subject enums.
    """
    return [subject_mapping[subject] if subject in subject_mapping else 
            ValueError(f"'{subject}' cannot be converted to a Subject enum.") for subject in subjects]


def convertSubject(subject: str) -> Subject:
    """
    Converts a single subject string to a Subject enum."
    """
    if subject in subject_mapping:
        return subject_mapping[subject]
    raise ValueError(f"'{subject}' cannot be converted to a Subject enum.")


def convertJsonToFellows(data: Dict[str, Any]) -> List[FellowApp]:
    """
    Converts JSON data into a list of FellowApp objects.
    """
    fellows = []

    for item in data['dataItems']:
        item_data = item.get('data', {})
        fellow = FellowApp(
            id=item.get('id'),
            cycle=convertCycle(item_data.get('cycle')),
            availability=convertAvailability(item_data.get('availabilities', [])),
            grades=convertGrades(item_data.get('gradeLevels', [])),
            subjects=convertSubjects(item_data.get('subjects', [])),
            match_count=item_data.get('matchCount'),
            capacity=item_data.get('tuteeCapacity'),
            returning=item_data.get('isReturningFellow', False),
            wants_prev_tutee=item_data.get('wantsPreviousTutee', False),
            prev_tutee_name=item_data.get('previousTuteeName'),
            prev_tutee_id=item_data.get('previousTuteeId')
        )
        fellows.append(fellow)

    return fellows


def convertJsonToTutees(data: Dict[str, Any]) -> List[TuteeApp]:
    """
    Converts JSON data into a list of TuteeApp objects.
    """
    tutees = []

    for item in data['dataItems']:
        item_data = item.get('data', {})
        tutee = TuteeApp(
            id=item.get('id'),
            cycle=convertCycle(item_data.get('cycle', Cycle.TEST)),
            availability=convertAvailability(item_data.get('availabilities', [])),
            grade=convertGrade(item_data.get('studentGrade')),
            subject1=convertSubject(item_data.get('subject1')),
            eval1=item_data.get('evaluation1'),
            subject2=convertSubject(item_data.get('subject2')),
            eval2=item_data.get('evaluation2'),
            subject3=convertSubject(item_data.get('subject3')),
            eval3=item_data.get('evaluation3'),
            match_count=item_data.get('matchCount', 0),
            capacity=item_data.get('subjectCount', 0),
            wants_prev_fellow=item_data.get('wantsPreviousFellow', False),
            prev_fellow_name=item_data.get('previousFellowName'),
            prev_fellow_id=item_data.get('previousFellowEmail')
        )
        tutees.append(tutee)

    return tutees


def convertMatchesToJson(matches: List[Match]) -> List[Any]:
    """
    Converts a list of Match objects into a JSON-compatible format, so it can be posted to Wix CMS
    """
    reverse_cycle_mapping = {value: key for key, value in cycle_mapping.items()}
    reverse_grade_mapping = {value: key for key, value in grade_mapping.items()}
    reverse_subject_mapping = {value: key for key, value in subject_mapping.items()}

    return [
        {
            'data': {
                'tuteeApplication': match.tutee_id,
                'fellowApplication': match.tf_id,
                'cycle': reverse_cycle_mapping[match.cycle],
                'subject': reverse_subject_mapping[match.subject],
                'grade': reverse_grade_mapping[match.grade]
            }
        } for match in matches
    ]


def updateAppsJson(data: Dict[str, Any], apps: List[Any]) -> Dict[str, Any]:
    """
    Updates application JSON data with match count from matched applications to update Wix CMS Data.
    Function can accept a list of Tutee or Fellows. 
    """
    # Create dict from list for quicker access
    app_dict = {app.id: app for app in apps}

    # Match application ids in JSON with applications in dict
    for item in data["dataItems"]:
        app_id = item.get("id")
        if app_id in app_dict:
            item["data"]["matchCount"] = app_dict[app_id].match_count

    return data['dataItems']