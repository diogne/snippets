
import os

def create_dir_if_not_exists(directory="logs"):
    '''
        A directory dedicated to log files generated 
        through my modules
    '''

    check_folder = os.path.isdir(directory)

    # If folder doesn't exist, then create it.
    if not check_folder:
        os.makedirs(directory)
        print(f"created folder : {directory}")

    else:
        print(f"{directory} folder already exists.")


if __name__ == '__main__':
    create_dir_if_not_exists()