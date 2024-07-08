from repository import Repository

GUESTS_PATH = "Input/Names/invited_names.txt"
BOILERPLATE_PATH = "Input/Letters/starting_letter.txt"
OUTPUT_FOLDER_PATH = "Output/ReadyToSend/"

NAME_WILDCARD = "[name]"

guests_repository = Repository(GUESTS_PATH)
boilerplate_repository = Repository(BOILERPLATE_PATH)
output_repository = Repository(OUTPUT_FOLDER_PATH)

guests = guests_repository.get_file_content_by_lines()

boilerplate = boilerplate_repository.get_file_content()

for guest in guests:
    guest = guest.strip()
    updated_boilerplate = boilerplate.replace(NAME_WILDCARD, guest)
    output_repository.write_file(content=updated_boilerplate, filename=f"letter_for_{guest}.txt")
