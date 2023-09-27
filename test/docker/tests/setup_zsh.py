import subprocess
import os
import pytest

USER_HOME = os.environ.get("USER_HOME", "/home/xotosphere")
USER_NAME = os.environ.get("USER_NAME", "xotosphere")
USER_GROUP = os.environ.get("USER_GROUP", "dockerterm")
ZSH_CUSTOM = os.path.join(USER_HOME, ".oh-my-zsh/custom")
ZSH_PLUGINS = os.path.join(ZSH_CUSTOM, "plugins")
ZSH_THEMES = os.path.join(ZSH_CUSTOM, "themes")

def test_oh_my_zsh_installed():
    try:
        cmd_output = subprocess.check_output(['zsh', '--version'], stderr=subprocess.STDOUT, text=True)
        assert "zsh" in cmd_output
    except subprocess.CalledProcessError:
        pytest.fail("oh my zsh not installed")

def test_tmux_configured():
    try:
        cmd_output = subprocess.check_output(['tmux', '-V'], stderr=subprocess.STDOUT, text=True)
        assert "tmux" in cmd_output
    except subprocess.CalledProcessError:
        pytest.fail("tmux not installed")
