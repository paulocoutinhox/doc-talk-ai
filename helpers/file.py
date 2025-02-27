import os


def get_root_folder():
    """Get the root folder path."""

    return os.getenv(
        "DB_TALK_AI_ROOT",
        os.path.dirname(
            os.path.abspath(os.path.join(__file__, "..")),
        ),
    )


def get_data_folder():
    """Get the data folder path."""
    return os.path.join(get_root_folder(), "data")


def get_chroma_db_folder():
    """Get the chroma db folder path."""
    return os.path.join(get_data_folder(), "chroma-db")


def get_uploads_folder():
    """Get the uploads folder path."""
    return os.path.join(get_data_folder(), "uploads")


def create_uploads_folder():
    """Create the uploads folder."""
    folder = get_uploads_folder()
    os.makedirs(folder, exist_ok=True)
