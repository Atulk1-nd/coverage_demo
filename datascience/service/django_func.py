
def create_logger(argument=5):
    with open("django_func.log", "w") as f:
        f.write(f"This is a placeholder for the django_func.log file.{argument}\n")
