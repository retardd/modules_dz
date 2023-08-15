from application.salary import calculate_salary
from application.db.people import get_employees

def main():
    get_employees()
    calculate_salary()

if __name__ == '__main__':
    print('start')
    main()

