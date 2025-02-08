def search_in_file(search_term):
    """
        Search for plants in the file that match the given search term.

        Parameters:
        search_term (str): The term to search for in the plant data.

        Returns:
        list: A list of dictionaries representing the matching plants, or 'fail' if no matches are found.
        """
    matches = []
    current_entry = {}
    with open('plants.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line == '--------------------':
                if current_entry:
                    if any(search_term.lower() in value.lower() for value in current_entry.values()):
                        matches.append(current_entry)
                    current_entry = {}
            else:
                if ':' in line:
                    key, value = line.split(':', 1)
                    current_entry[key.strip()] = value.strip()
        # Check the last entry if the file does not end with the delimiter
        if current_entry and any(search_term.lower() in value.lower() for value in current_entry.values()):
            matches.append(current_entry)
    return matches if matches else 'fail'


def get_all_plants():
    """
        Retrieve all plants from the file.

        Returns:
        list: A list of dictionaries representing all the plants in the file.
        """
    plants = []
    try:
        with open('plants.txt', 'r') as file:
            content = file.read().strip()
            plant_entries = content.split('--------------------\n')

            for entry in plant_entries:
                lines = entry.strip().split('\n')
                if not lines[0]:
                    continue  # Skip empty entries

                plant_data = {}
                for line in lines:
                    if line:
                        key, value = line.split(': ', 1)
                        plant_data[key.strip()] = value.strip()
                if plant_data:
                    plants.append(plant_data)
    except FileNotFoundError:
        print("The file 'plants.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return plants


def update_plant_in_file(original_plant, updated_plant):
    """
       Update the details of a specific plant in the file.

       Parameters:
       original_plant (dict): The dictionary representing the original plant data.
       updated_plant (dict): The dictionary representing the updated plant data.
       """
    with open('plants.txt', 'r') as file:
        lines = file.readlines()

    plant_index = None
    current_entry = {}
    entry_start_line = 0

    for i, line in enumerate(lines):
        if line.strip() == '--------------------':
            if current_entry == original_plant:
                plant_index = entry_start_line
                break
            current_entry = {}
            entry_start_line = i + 1
        else:
            if ':' in line:
                key, value = line.split(':', 1)
                current_entry[key.strip()] = value.strip()

    if plant_index is not None:
        updated_lines = [f"{key}: {value}\n" for key, value in updated_plant.items()]
        updated_lines.append('--------------------\n')

        end_index = plant_index + len(updated_lines)
        lines[plant_index:end_index] = updated_lines

        with open('plants.txt', 'w') as file:
            file.writelines(lines)


def delete_plant_from_file(plant_to_delete):
    """
        Delete a specific plant from the file.

        Parameters:
        plant_to_delete (dict): The dictionary representing the plant to be deleted.
        """
    try:
        # Read the entire file
        with open("plants.txt", "r") as file:
            lines = file.readlines()

        # Open the file for writing
        with open("plants.txt", "w") as file:
            delete_flag = False

            for line in lines:
                # Check if the line starts with a delimiter indicating a new plant
                if line.strip() == '--------------------':
                    if delete_flag:
                        delete_flag = False
                    else:
                        file.write(line)
                elif delete_flag:
                    continue
                else:
                    # Check if the line contains data for the plant to delete
                    if any(line.startswith(f"{key}: {value}") for key, value in plant_to_delete.items()):
                        delete_flag = True
                    else:
                        file.write(line)

    except Exception as e:
        print(f"Error while deleting plant: {e}")
