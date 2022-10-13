import os
import platform
import subprocess


LANGUAGES = ["erlang", "elixir", "python", "nodejs"]


class UnsupportedPlatformException(Exception):
    pass

class SetupEnvironment:
    def __init__(self):
        self.platform: str = platform.system()
        self.shell_name: str = os.environ["SHELL"]
        self.is_git_available: bool = self.verify_git()

    def write_to_config_file(self, commands, platform="Linux"):
        if platform == "Linux":
            subprocess.run(["echo", "-e", commands, ">>", "~/.zshrc"])
        else:
            subprocess.run(["echo", "-e", commands, ">>", "${ZDOTDIR:-~}/.zshrc"])

    def verify_git(self) -> bool:
        return subprocess.run(["git"]).returncode == 0
