"""
Tests for the auth module: password change and reset functionality.
"""

import pytest
import auth


@pytest.fixture(autouse=True)
def clear_users():
    """Reset the in-memory user store before each test."""
    auth._users.clear()
    yield
    auth._users.clear()


class TestRegisterAndAuthenticate:
    def test_register_and_login(self):
        auth.register_user("alice", "secret")
        assert auth.authenticate("alice", "secret") is True

    def test_wrong_password(self):
        auth.register_user("alice", "secret")
        assert auth.authenticate("alice", "wrong") is False

    def test_unknown_user(self):
        assert auth.authenticate("nobody", "x") is False

    def test_duplicate_registration_raises(self):
        auth.register_user("alice", "secret")
        with pytest.raises(ValueError, match="already exists"):
            auth.register_user("alice", "other")

    def test_invalid_role_raises(self):
        with pytest.raises(ValueError, match="Invalid role"):
            auth.register_user("alice", "secret", role="superuser")


class TestChangePassword:
    def test_change_password_succeeds(self):
        auth.register_user("alice", "oldpass")
        auth.change_password("alice", "oldpass", "newpass")
        assert auth.authenticate("alice", "newpass") is True
        assert auth.authenticate("alice", "oldpass") is False

    def test_change_password_wrong_old_password(self):
        auth.register_user("alice", "oldpass")
        with pytest.raises(ValueError, match="Authentication failed"):
            auth.change_password("alice", "wrongpass", "newpass")

    def test_change_password_empty_new_password(self):
        auth.register_user("alice", "oldpass")
        with pytest.raises(ValueError, match="must not be empty"):
            auth.change_password("alice", "oldpass", "")


class TestPasswordReset:
    def setup_method(self):
        auth.register_user("admin", "adminpass", role=auth.ROLE_ADMIN)
        auth.register_user("bob", "bobpass", role=auth.ROLE_USER)

    def test_admin_can_generate_reset_token(self):
        token = auth.generate_reset_token("admin", "adminpass", "bob")
        assert isinstance(token, str)
        assert len(token) == 32

    def test_reset_password_with_valid_token(self):
        token = auth.generate_reset_token("admin", "adminpass", "bob")
        auth.reset_password("bob", token, "newbobpass")
        assert auth.authenticate("bob", "newbobpass") is True
        assert auth.authenticate("bob", "bobpass") is False

    def test_token_invalidated_after_use(self):
        token = auth.generate_reset_token("admin", "adminpass", "bob")
        auth.reset_password("bob", token, "newbobpass")
        with pytest.raises(ValueError, match="Invalid or expired reset token"):
            auth.reset_password("bob", token, "anotherpass")

    def test_non_admin_cannot_generate_reset_token(self):
        auth.register_user("charlie", "charliepass", role=auth.ROLE_USER)
        with pytest.raises(PermissionError, match="Admin role required"):
            auth.generate_reset_token("charlie", "charliepass", "bob")

    def test_wrong_admin_password_raises(self):
        with pytest.raises(ValueError, match="Authentication failed"):
            auth.generate_reset_token("admin", "wrongpass", "bob")

    def test_invalid_token_raises(self):
        auth.generate_reset_token("admin", "adminpass", "bob")
        with pytest.raises(ValueError, match="Invalid or expired reset token"):
            auth.reset_password("bob", "badtoken", "newpass")

    def test_reset_nonexistent_user_raises(self):
        with pytest.raises(ValueError, match="does not exist"):
            auth.generate_reset_token("admin", "adminpass", "nobody")

    def test_reset_empty_new_password_raises(self):
        token = auth.generate_reset_token("admin", "adminpass", "bob")
        with pytest.raises(ValueError, match="must not be empty"):
            auth.reset_password("bob", token, "")


class TestGetUserRole:
    def test_get_user_role(self):
        auth.register_user("alice", "pass", role=auth.ROLE_USER)
        assert auth.get_user_role("alice") == auth.ROLE_USER

    def test_get_admin_role(self):
        auth.register_user("admin", "pass", role=auth.ROLE_ADMIN)
        assert auth.get_user_role("admin") == auth.ROLE_ADMIN

    def test_get_role_unknown_user(self):
        with pytest.raises(ValueError, match="does not exist"):
            auth.get_user_role("nobody")
