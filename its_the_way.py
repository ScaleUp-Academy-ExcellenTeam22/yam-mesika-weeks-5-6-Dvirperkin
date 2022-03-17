import os


def end_with_deep(path: str):
    return [file for file in os.listdir(path) if file.startswith("deep")]


end_with_deep("C:\\Users\\dvirp\\OneDrive - edu.hac.ac.il\\Documents\\GitHub\\Notebooks-master\\week05\\images")
