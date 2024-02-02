import requests
import os
#https://apps.ualberta.ca/catalogue/course/cmput/101

def save_course_name_into_text_file(url, output_file):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save to the file
            with open(output_file, "a") as fh:
                tmp_txt = f"CMPUT {(url.split('/'))[-1]},\n"
                fh.write(tmp_txt)
            print(f"course number appended successfully to {output_file}")
        else:
            print(f"Failed with Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Example usage:
    allowed_course_list = ["1","2","3","4"]
    course_number = 100
    while str(course_number)[0] in allowed_course_list:
        url = f"https://apps.ualberta.ca/catalogue/course/cmput/{course_number}"
        output_file = f"CMPUT_COURSES_LIST.csv"
        save_course_name_into_text_file(url, output_file)
        course_number += 1

        if not(100 <= course_number <= 499):
            tmp_error = "exit "*10
            print(tmp_error)
            break

def clear():
    import subprocess
    command = f"rm CMPUT_COURSES_LIST.csv"
    try:
        subprocess.run(command, shell=True, check=True)
        print("file deleted successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def mk_touch():
    import subprocess
    command = f"touch CMPUT_COURSES_LIST.csv"
    try:
        subprocess.run(command, shell=True, check=True)
        print("file created successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    clear()
    mk_touch()
    main()

