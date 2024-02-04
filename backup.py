###Program Name: backup.py
###Programmer: Aaliyah Raderberg
###Description: Automated Data Backup System

import os
import shutil
import datetime
import logging

def create_backup(source_dir, destination_dir):
    """Creates a backup of the specified source directory."""

    try:
        # Create a timestamped backup directory
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        backup_dir = os.path.join(destination_dir, f"backup_{timestamp}")

        # Copy files to the backup directory
        shutil.copytree(source_dir, backup_dir)

        logging.info(f"Backup created successfully at {backup_dir}")

    except Exception as e:
        logging.error(f"Error during backup creation: {e}")

def main():
    """Main function to initiate the backup process."""

    logging.basicConfig(filename='backup.log', level=logging.INFO)

    source_dir = "/path/to/your/source/directory"  # Replace with your source directory
    destination_dir = "/path/to/your/backup/destination"  # Replace with your backup destination

    create_backup(source_dir, destination_dir)

if __name__ == "__main__":
    main()
