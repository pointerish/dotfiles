import setup_environment
from setup_asdf import setup_asdf, setup_languages


def run():
    setup_env = setup_environment.SetupEnvironment()
    if setup_asdf(
        setup_env.is_git_available, setup_env.platform, 
        setup_env.shell_name, setup_env.write_to_config_file
        ):

        setup_languages(setup_environment.LANGUAGES)


