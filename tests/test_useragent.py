from __future__ import annotations

from MyMovieGraphQL.UserAgent import get_user_agent


def test_user_agent_contains_package_name():
    user_agent = get_user_agent()
    assert isinstance(user_agent, str)
    assert "MyMovieGraphQL" in user_agent
