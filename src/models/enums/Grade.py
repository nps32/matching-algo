from enum import Enum


class Grade(Enum):
    """
    Enum representing the different grade ranges for tutoring.
    """
    LE = "Lower Elementary"
    HE = "Higher Elementary"
    MI = "Middle School"
    HS = "High School"