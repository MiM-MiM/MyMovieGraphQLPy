import platform
from importlib.metadata import metadata, PackageNotFoundError
from MyMovieGraphQL import __name__ as name


def get_user_agent() -> str:
    """
    Dynamically construct User-Agent from package metadata.
    """
    try:
        pkg_meta = metadata(name)
        # fmt: off
        pkg_name = pkg_meta.get("Name", name)  # pyright: ignore[reportAttributeAccessIssue] # noqa: E501
        pkg_version = pkg_meta.get("Version", "0.0.0")  # pyright: ignore[reportAttributeAccessIssue] # noqa: E501
        repo_url = pkg_meta.get("Project-URL", "") or pkg_meta.get("Home-page")  # pyright: ignore[reportAttributeAccessIssue] # noqa: E501
        if ", " in repo_url:
            _, repo_url = repo_url.split(", ", 1)
        else:
            repo_url = repo_url.strip()
        email = pkg_meta.get("Maintainer-Email", "") or pkg_meta.get("Author-Email", "")  # pyright: ignore[reportAttributeAccessIssue] # noqa: E501
        # fmt: on
    except PackageNotFoundError:
        pkg_name = name
        pkg_version = "dev"
        repo_url = ""
        email = ""

    py_version = platform.python_version()
    os_name = platform.system()
    os_release = platform.release()
    arch = platform.machine()

    ua_parts = [f"{pkg_name}/{pkg_version}"]
    system_info = f"Python {py_version}; {os_name} {os_release}; {arch}"

    contact_parts = []
    if repo_url:
        contact_parts.append(f"+{repo_url}")
    if email:
        contact_parts.append(email)

    if contact_parts:
        system_info += f"; {'; '.join(contact_parts)}"

    return f"{ua_parts[0]} ({system_info})"
