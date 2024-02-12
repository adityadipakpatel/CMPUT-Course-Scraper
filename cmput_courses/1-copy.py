
import requests
import os
import shutil
from datetime import datetime
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

def pnc(ug_course_list, course_alphabet_list):
    tmp_list = []
    for i in ug_course_list:
        for j in course_alphabet_list:
            tmp = f"{i}{j}"
            tmp_list.append(tmp)
    return tmp_list

def main():
    final_course_list = pnc(list(range(100, 500)), ["a", "b", ""])
    course_number = 100
    while str(course_number)[0] in final_course_list:
        url = f"https://apps.ualberta.ca/catalogue/course/cmput/{course_number}"
        output_file = f"CMPUT {course_number}.html"
        download_html(url, output_file)
        course_number += 1

        if not(100 <= course_number <= 499):
            tmp_error = "ERROR"*10
            print(tmp_error)
            break

def move(source_folder, destination_folder):
    # Get the current date and time
    today_date_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create the destination folder with the specified format
    formatted_destination_folder = os.path.join(destination_folder, f"old_files_{today_date_time}")
    os.makedirs(formatted_destination_folder, exist_ok=True)

    # Iterate through all files in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith(".html"):
            # Build the full paths for the source and destination files
            source_file_path = os.path.join(source_folder, filename)
            destination_file_path = os.path.join(formatted_destination_folder, filename)

            # Move the .html file to the new destination
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved {filename} to {formatted_destination_folder}")

if __name__ == "__main__":
    #move("./", "./old_files")
    main()



























# def clean(folder_path):
#     try:
#         # Get the list of files in the specified folder
#         file_list = os.listdir(folder_path)
        
#         # Iterate through the files
#         for file_name in file_list:
#             if file_name.endswith(".html"):
#                 file_path = os.path.join(folder_path, file_name)
#                 os.remove(file_path)
#                 print(f"Removed: {file_path}")
#         print("Operation completed successfully.")
#     except Exception as e:
#         print(f"An error occurred: {e}")