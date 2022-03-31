import os


def start_with_deep(dir_path: str) -> list[str]:
    """
    @param dir_path - A path to directory.
    @return - A list the files that start with "deep" in thair name in the given directory.
    """
    return [file for file in os.listdir(dir_path) if file.startswith("deep")]


if __name__ == '__main__':
    start_with_deep("C:\\Users\\dvirp\\OneDrive - edu.hac.ac.il\\Documents\\GitHub\\Notebooks-master\\week05\\images")
