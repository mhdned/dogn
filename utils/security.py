import hashlib

import jwt

from configs.config import config


def hash_password(password: str) -> str:
    # Encode the password as bytes
    password_bytes = password.encode("utf-8")

    # Create a SHA-1 hash object
    sha1_hash = hashlib.sha1()

    # Update the hash object with the password bytes
    sha1_hash.update(password_bytes)

    # Get the hexadecimal representation of the hash
    hashed_password = sha1_hash.hexdigest()

    return hashed_password


def generate_token(payload):
    """
    Generate JWT token with given payload.
    """
    return jwt.encode(payload, config["SECRET_KEY"], algorithm="HS256")


def decode_token(token):
    """
    Decode JWT token and return the payload.
    """
    try:
        return jwt.decode(token, config["SECRET_KEY"], algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        # Handle token expiration
        print("Token has expired.")
        return "expired"
    except jwt.InvalidTokenError:
        # Handle invalid token
        print("Invalid token.")
        return "invalid"
