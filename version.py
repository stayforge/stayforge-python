import subprocess
import re


def get_latest_version_from_commits():
    try:
        # Run `git log` to retrieve all commit messages
        result = subprocess.run(
            ["git", "log", "--all", "--grep", "[vV]*[0-9]\\.[0-9]\\.[0-9]", "--format=%s"],
            stdout=subprocess.PIPE, text=True, check=True
        )

        # Retrieve all commit messages as a list
        commit_messages = result.stdout.strip().split("\n")

        # Define regex pattern to match version numbers (both v1.0.0 and 1.0.0)
        pattern = r"([0-9]+\.[0-9]+\.[0-9]+)"

        # Search for the latest version in git commit messages
        for message in commit_messages:
            match = re.search(pattern, message)
            if match:
                return match.group(0)  # Return the first matched version
        return None  # No version found
    except subprocess.CalledProcessError as e:
        print(f"Error while running git command: {e}")
        return None


# Get the latest version
latest_version = get_latest_version_from_commits()
if latest_version:
    print(f"The latest version from commits is: {latest_version}")
else:
    print("No version found in commit history.")
