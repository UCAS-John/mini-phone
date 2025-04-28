from src.profiles import profile
from src.manage import scores

if __name__ == "__main__":
    print(profile.create_profile("test_user", "test_password"))
    print(profile.login_profile("test_user", "test_password"))