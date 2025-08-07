class User:
    """Represents a basic user in the system."""
    
    def __init__(self, name: str, email: str):
        """
        Initializes a User with name and email.
        
        Args:
            name (str): The user's name
            email (str): The user's email address
        """
        self.name = name
        self.email = email
    
    def __str__(self) -> str:
        """String representation of the User."""
        return f"User: {self.name} ({self.email})"


class Owner(User):
    """Represents an owner (special type of User with additional privileges)."""
    
    def __str__(self) -> str:
        """String representation of the Owner (overrides User.__str__)."""
        return f"Owner: {self.name} ({self.email})"