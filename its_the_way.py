import os


def start_with_deep(dir_path: str) -> list[str]:
    return [file for file in os.listdir(dir_path) if file.startswith("deep")]


if __name__ == '__main__':
    start_with_deep("C:\\Users\\dvirp\\OneDrive - edu.hac.ac.il\\Documents\\GitHub\\Notebooks-master\\week05\\images")
