import subprocess
from setup import UnsupportedPlatformException


def setup_homebrew(platform) -> bool:
    if "Darwin" in platform:
        subprocess.run(
            [
                "/bin/bash",
                "-c",
                "\"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
            ]
        )
        return True
    return False

def setup_asdf(is_git_available, platform, shell_name, config_writer) -> bool:

    if subprocess.run(["asdf"]).returncode == 0:
        return True

    if is_git_available and "Linux" in platform:
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

        if "zsh" in shell_name:
            config_writer("\". $HOME/.asdf/asdf.sh\"")

            return True

        if "bash" in shell_name:
            settings = [
                "\". $HOME/.asdf/asdf.sh\"",
                "\". $HOME/.asdf/completions/asdf.bash\""
            ]
            map(lambda setting: config_writer(setting), settings)

            return True
    elif "Darwin" in platform:
        if setup_homebrew():
            subprocess.run(["brew", "install", "asdf"])
            config_writer("\n. $(brew --prefix asdf)/libexec/asdf.sh", platform="Darwin")
            return True
    else:
        raise UnsupportedPlatformException(
            """
            Windows is not currently supported by this tool.
            You'll have to manually setup your environment. Have fun! :)
            """
        )

def asdf_install(language) -> bool:
    subprocess.run(["asdf", "plugin-add", language]) and subprocess.run(["asdf", "install", language, "latest"])

def setup_languages(languages):
    map(lambda lang: asdf_install(lang), languages)
