from os.path import exists
"""
Generate_invitation module
"""


def generate_invitations(template_content, attendees):
    """
    generates personalized invitation files from a template
    """
    if not exists("template.txt"):
        raise FileNotFoundError("Template file not found")

    with open('template.txt', 'r') as file:
        template_content = file.read()

    if not template_content:
        raise ValueError("Template is empty, no output files generated.")

    if not attendees:
        raise ValueError("No data provided, no output files generated.")

    if not isinstance(template_content, str):
        print("Template must be a string")
        return

    if not isinstance(attendees, list):
        print("Attendees must be a list of dictionaries")
        return

    for attendee in attendees:
        for key, value in attendee.items():
            if not value or str(value).strip() == "":
                attendee[key] = "N/A"

    for index, attendee in enumerate(attendees, start=1):
        invit = template_content
        for key, value in attendee.items():
            placeholder = f"{{{key}}}"
            invit = invit.replace(placeholder, str(value))
            output_filename = f"output_{index}.txt"
            with open(output_filename, 'w') as file:
                file.write(invit)
