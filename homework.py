#export PYTHONPATH="${PYTHONPATH}:C:/data-science-course/data-science-course/homework.py/"
import grade_average_service 

homework_assignment_grades = {
    'homework_1': 85,
    'homework_2': 100,
    'homework_3':81
}

grade_average_service.homework_calculate(homework_assignment_grades)