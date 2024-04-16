from pii_data_handler import encrypt_data
from website.models import User


def get_user_by_email(email: str) -> str | None:
    """
    Retrieve a user from the database based on their encrypted email address.
    """
    # Validate email input
    if not email:
        raise ValueError("Email address cannot be empty")

    # Encrypt the email address
    encrypted_email = encrypt_data(email)

    try:
        # Perform database query
        user = User.query.filter_by(email=encrypted_email, is_deleted=False).first()

        # Check if user is found
        if user:
            return user
        else:
            raise FileNotFoundError(f"No user found with email: {email}")

    except Exception as err:
        print(err)
        # Log the error
        # logging.error(f"Error retrieving user by email: {err}")
        # Optionally re-raise the error for higher-level handling
        # raise

    return None
