# job_title: software engineer, electrical engineer
# years_worked: int

# returns: your expected annual salary
def salary(job_title: str, years_worked: int) -> int:
    job_title = 'software engineer'

    if job_title == 'software engineer':
        # Proceed to check the person's years worked, and return
        # an appropriate salary
        if years_worked <= 3:
            return 100000
        else:
            return 130000
    else:
        # Proceed to check the person's years worked, and return
        # an appropriate salary
        if years_worked <= 3:
            return 99000
        else:
            return 131000


def main() -> None:
    job = input('What is your job title?: ')
    years_worked = int(input('How many years have you worked?: '))
    user_salary = salary(job, years_worked)

    print(job_title)

    print(f'Your expected annual salary is {user_salary}')
    

if __name__ == '__main__':
    main()
