import requests
import os
#https://apps.ualberta.ca/catalogue/course/cmput/101

def download_html(url, output_file):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the HTML content to a file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"HTML file downloaded successfully to {output_file}")
        else:
            print(f"Failed to download HTML. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Example usage:
    allowed_course_list = ["1","2","3","4"]
    course_number = 100
    while str(course_number)[0] in allowed_course_list:
        url = f"https://apps.ualberta.ca/catalogue/course/cmput/{course_number}"
        output_file = f"CMPUT/CMPUT {course_number}.html"
        download_html(url, output_file)
        course_number += 1

        if not(100 <= course_number <= 499):
            tmp_error = "exit "*10
            print(tmp_error)
            break

def clear():
    import subprocess
    subject = "CMPUT"
    command = f"find . -type f -name '*{subject}*' -delete"
    try:
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def mkdir():
    import subprocess
    subject = "CMPUT"
    command = f"mkdir CMPUT"
    try:
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    clear()
    mkdir()
    main()
