def annual_income(job_title: str, num_years_worked: int) -> int:
    if job_title == 'software engineer':
        if num_years_worked <= 3:
            return 100000
        else:
            return 130000
    elif job_title == 'electrical engineer':
        if num_years_worked <= 3:
            return 99000
        else:
            return 131000
    else:
        # Often times, it's not appropriate to deal with the error here.
        # You can return errors as values.
        
        # return -1
        
        # Exceptions are an alternative way of communicating errors.
        raise ValueError('error message goes here')
        

# Control flow: The order of execution of instructions in a program

def main() -> None:
    job_title = input('What is your job title?: ')
    try:
        income = annual_income(job_title, 10)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
