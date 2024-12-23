import os
import subprocess
import re


def get_git_tags_sorted_and_filtered():
    try:
        result = subprocess.run(
            ['git', 'tag', '--sort=-creatordate'],
            capture_output=True,
            text=True,
            check=True
        )
        tags = result.stdout.strip().split('\n')

        #  x.x.x
        pattern_stable = r'^\d+\.\d+\.\d+$'
        _stable_tags = [tag for tag in tags if re.match(pattern_stable, tag)]

        # x.x.x.devX
        pattern_dev = r'^\d+\.\d+\.\d+\.dev\d+$'
        _dev_tags = [tag for tag in tags if re.match(pattern_dev, tag)]

        # x.x.x.aX
        pattern_a = r'^\d+\.\d+\.\d+\.a\d+$'
        _a_tags = [tag for tag in tags if re.match(pattern_dev, tag)]

        return _stable_tags, _dev_tags, _a_tags
    except subprocess.CalledProcessError as e:
        print(f"Error executing git command: {e}")
        return None


def get_branch_name():
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            capture_output=True,
            text=True,
            check=True
        )

        branch_n = result.stdout.strip()
        return branch_n
    except subprocess.CalledProcessError as e:
        print(f"Error executing git command: {e}")
        return None


tags, dev_tags, a_tags = get_git_tags_sorted_and_filtered()

latest_main_version = tags[0]

branch_name = get_branch_name()

if branch_name == 'main':
    sub_version = ""
if branch_name == 'alpha':
    latest_a = a_tags[0]
    numeric = re.search(r'\.a(\d+)', latest_a).group(1) if re.search(r'\.a(\d+)', latest_a) else 1
    sub_version = f"a{numeric + 1}"
else:
    latest_dev = dev_tags[0]
    numeric = int(re.search(r'\.dev(\d+)', latest_dev).group(1) if re.search(r'\.dev(\d+)', latest_dev) else 1)
    sub_version = f"dev{numeric + 1}"

version = __version__ = f"{latest_main_version}{sub_version}"

script_dir = os.path.dirname(os.path.abspath(__file__))
version_file_path = os.path.join(script_dir, "version")
with open(version_file_path, "w") as f:
    f.write(f"{version}")
