import secrets
import string

SPECIALS = "#*&!@$%"

class PasswordGenerator:
    def __init__(self, length=12, use_digits=True, use_special=True, use_upper=True, use_lower=True):
        self.length = length
        self.use_digits = use_digits
        self.use_special = use_special
        self.use_upper = use_upper
        self.use_lower = use_lower

    def generate(self):
        characters = ""
        if self.use_lower:
            characters += string.ascii_lowercase
        if self.use_upper:
            characters += string.ascii_uppercase
        if self.use_digits:
            characters += string.digits
        if self.use_special:
            characters += SPECIALS

        if not characters:
            raise ValueError("At least one character set must be enabled")

        password = []
        if self.use_lower:
            password.append(secrets.choice(string.ascii_lowercase))
        if self.use_upper:
            password.append(secrets.choice(string.ascii_uppercase))
        if self.use_digits:
            password.append(secrets.choice(string.digits))
        if self.use_special:
            password.append(secrets.choice(SPECIALS))
        password += [secrets.choice(characters) for _ in range(self.length - len(password))]
        secrets.SystemRandom().shuffle(password)
        return ''.join(password)