import os
import argv
import platform
import subprocess
from typing import List
from setup_environment import SetupEnvironment
LANGUAGES = ["erlang", "elixir", "python", "nodejs"]

class UnsupportedPlatformException(Exception):
    pass


def setup_homebrew(self) -> bool:
    if "Darwin" in self.platform:
        subprocess.run(
            [
                "/bin/bash",
                "-c",
                "\"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
            ]
        )
        return True
    return False

def setup_asdf(self) -> bool:
    if subprocess.run(["asdf"]).returncode == 0:
        return True

    if self.is_git_available and "Linux" in self.platform:
        subprocess.run(
            [
                "git",
                "clone",
                "https://github.com/asdf-vm/asdf.git",
                "~/.asdf",
                "--branch",
                "v0.10.2"
            ]
        )

        if "zsh" in self.shell_name:
            self._write_to_config_file("\". $HOME/.asdf/asdf.sh\"")

            return True

        if "bash" in self.shell_name:
            settings = [
                "\". $HOME/.asdf/asdf.sh\"",
                "\". $HOME/.asdf/completions/asdf.bash\""
            ]
            map(lambda setting: self._write_to_config_file(setting), settings)

            return True
    elif "Darwin" in self.platform:
        if self.setup_homebrew():
            subprocess.run(["brew", "install", "asdf"])
            self._write_to_config_file("\n. $(brew --prefix asdf)/libexec/asdf.sh", platform="Darwin")
            return True
    else:
        raise UnsupportedPlatformException(
            """
            Windows is not currently supported by this tool.
            You'll have to manually setup your environment. Have fun! :)
            """
        )

def asdf_install(self, language) -> bool:
    subprocess.run(["asdf", "plugin-add", language]) and subprocess.run(["asdf", "install", language, "latest"])

def setup_languages(self):
    map(lambda lang: self.asdf_install(lang), LANGUAGES)
