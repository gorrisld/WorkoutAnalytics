#Test to edit a profile
import pytest

from userProfile import UserProfile

@pytest.fixture
def user_profile():
    # Create a UserProfile object for testing
    profile = UserProfile("John Doe", "password123", 70, 5)
    return profile

def test_edit_profile(user_profile):
    # Check initial values
    assert user_profile.name == "John Doe"
    assert user_profile.password == "password123"
    assert user_profile.heightIn == 70
    assert user_profile.heightFt == 5

    # Edit the profile
    user_profile.editProfile("Jane Smith", "newpassword", 68, 6)

    # Check updated values
    assert user_profile.name == "Jane Smith"
    assert user_profile.password == "newpassword"
    assert user_profile.heightIn == 68
    assert user_profile.heightFt == 6