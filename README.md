import os

def update_readme(course_name, assignment_name, status):
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        raise FileNotFoundError("README.md not found in the repository.")
    
    with open(readme_path, "r+") as readme_file:
        readme_content = readme_file.readlines()
        updated_content = []
        assignment_found = False
        for line in readme_content:
            if assignment_name.lower() in line.lower():
                updated_content.append(f"{assignment_name} - {status.capitalize()}\n")
                assignment_found = True
            else:
                updated_content.append(line)
        
        if not assignment_found:
            updated_content.append(f"{assignment_name} - {status.capitalize()}\n")
        
        readme_file.seek(0)
        readme_file.writelines(updated_content)
        readme_file.truncate()

def main():
    course_name = "SkyPro"
    assignment_name = "Домашнее задание \"Знакомство с языком Python\""
    status = "выполнено"
    
    try:
        update_readme(course_name, assignment_name, status)
        print("README.md updated successfully.")
    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
