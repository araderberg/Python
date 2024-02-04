###Program Name: auto_file_org.py
###Programmer: Aaliyah Raderberg
###Description: Automated File Organization

import os
import shutil
import datetime

def organize_files(source_dir, rules):
    """Organizes files based on specified rules."""

    for filename in os.listdir(source_dir):
        full_path = os.path.join(source_dir, filename)

        for rule in rules:
            if rule.matches(filename, full_path):
                destination_dir = rule.get_destination_dir(source_dir)
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)
                shutil.move(full_path, destination_dir)
                break  # Move to the next file if a rule matches

class Rule:
    """Base class for defining file organization rules."""

    def matches(self, filename, full_path):
        """Returns True if the rule matches the given file."""
        raise NotImplementedError("Subclasses must implement the matches() method")

    def get_destination_dir(self, source_dir):
        """Returns the destination directory for files matching this rule."""
        raise NotImplementedError("Subclasses must implement the get_destination_dir() method")

class ExtensionRule(Rule):
    """Organizes files based on their extensions."""

    def __init__(self, extensions, destination_dir):
        self.extensions = extensions
        self.destination_dir = destination_dir

    def matches(self, filename, full_path):
        return any(filename.endswith(ext) for ext in self.extensions)

    def get_destination_dir(self, source_dir):
        return os.path.join(source_dir, self.destination_dir)

class FilenamePatternRule(Rule):
    """Organizes files based on patterns in their names."""

    def __init__(self, pattern, destination_dir):
        self.pattern = pattern
        self.destination_dir = destination_dir

    def matches(self, filename, full_path):
        return self.pattern in filename

    def get_destination_dir(self, source_dir):
        return os.path.join(source_dir, self.destination_dir)

class DateRule(Rule):
    """Organizes files based on their creation or modification dates."""

    def __init__(self, date_format, destination_dir_format):
        self.date_format = date_format
        self.destination_dir_format = destination_dir_format

    def matches(self, filename, full_path):
        return True  # Always matches, as date handling is done in get_destination_dir()

    def get_destination_dir(self, source_dir):
        file_datetime = datetime.datetime.fromtimestamp(os.path.getmtime(full_path))
        date_str = file_datetime.strftime(self.date_format)
        return os.path.join(source_dir, self.destination_dir_format.format(date_str))

# Example usage:
source_dir ="c:/xxx/xxx/pictures"
full_path = "c:/xxx/xxx/pictures"
rules = [
    ExtensionRule([".jpg", ".jpeg", ".png"], "Photos"),
    ExtensionRule([".pdf", ".docx", ".xlsx"], "Documents"),
    FilenamePatternRule("_report_", "Reports"),
   # DateRule("%Y-%m", "Archive/{date_str}"),  # Organize files by month
]

organize_files(source_dir, rules)
