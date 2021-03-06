from typing import List, Optional, Tuple

import IPython.terminal.prompts as prompts
from prompt_toolkit.application import get_app
from prompt_toolkit.key_binding.vi_state import InputMode
from pygments.token import _TokenType, Token
from pygments.style import Style  
from pygments.token import ( 
    Comment,
    Error,
    Keyword,
    Name,
    Number,
    Operator,
    String,
    Text,
    Token,
)

from dataclasses import dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class Color:
    """Absolute colors as defined by gruvbox: https://git.io/JvV8i."""

    dark0_hard: str = "#1d2021"
    dark0: str = "#282828"
    dark0_soft: str = "#32302f"
    dark1: str = "#3c3836"
    dark2: str = "#504945"
    dark3: str = "#665c54"
    dark4: str = "#7c6f64"
    dark4_256: str = "#7c6f64"

    gray_245: str = "#928374"
    gray_244: str = "#928374"

    light0_hard: str = "#f9f5d7"
    light0: str = "#fbf1c7"
    light0_soft: str = "#f2e5bc"
    light1: str = "#ebdbb2"
    light2: str = "#d5c4a1"
    light3: str = "#bdae93"
    light4: str = "#a89984"
    light4_256: str = "#a89984"

    bright_red: str = "#fb4934"
    bright_green: str = "#b8bb26"
    bright_yellow: str = "#fabd2f"
    bright_blue: str = "#83a598"
    bright_purple: str = "#d3869b"
    bright_aqua: str = "#8ec07c"
    bright_orange: str = "#fe8019"

    neutral_red: str = "#cc241d"
    neutral_green: str = "#98971a"
    neutral_yellow: str = "#d79921"
    neutral_blue: str = "#458588"
    neutral_purple: str = "#b16286"
    neutral_aqua: str = "#689d6a"
    neutral_orange: str = "#d65d0e"

    faded_red: str = "#9d0006"
    faded_green: str = "#79740e"
    faded_yellow: str = "#b57614"
    faded_blue: str = "#076678"
    faded_purple: str = "#8f3f71"
    faded_aqua: str = "#427b58"
    faded_orange: str = "#af3a03"


class GruvboxStyle(Style):
    """An opinionated terminal colorscheme for IPython using gruvbox colors."""

    styles: Dict[Any, str] = {
        Comment: Color.gray_245,
        Error: Color.bright_red,
        Keyword.Namespace: Color.bright_blue,
        Keyword.Constant: Color.bright_orange,
        Keyword.Type: Color.bright_yellow,
        Keyword: Color.bright_red,
        Name.Builtin.Pseudo: Color.bright_blue,
        Name.Builtin: Color.bright_yellow,
        Name.Class: Color.bright_yellow,
        Name.Decorator: f"{Color.bright_green} bold",
        Name.Exception: Color.bright_red,
        Name.Function: Color.bright_aqua,
        Name.Variable.Magic: Color.bright_orange,
        Name: Color.light1,
        Number: Color.bright_purple,
        Operator.Word: Color.bright_red,
        Operator: Color.light1,
        String.Affix: Color.light1,
        String.Escape: Color.bright_orange,
        String.Interpol: Color.bright_orange,
        String: Color.bright_green,
        Text: Color.light1,
        Token.Punctuation: Color.light1,
        }
config = get_config()

class Prompt(prompts.Prompts):
    """Custom IPython prompt."""

    _after: str = "??? "
    _continuation: str = "??? "

    def in_prompt_tokens(self) -> List[Tuple[_TokenType, str]]:
        """Return in prompt."""
        if get_app().vi_state.input_mode == InputMode.INSERT:
            prompt_token = prompts.Token.InsertPrompt
            after = self._after
        else:
            prompt_token = prompts.Token.NavPrompt
            after = f"*{self._after}"

        return [
            (prompt_token, after),
        ]

    def continuation_prompt_tokens(
        self, width: Optional[int] = None
    ) -> List[Tuple[_TokenType, str]]:
        """Return continuation prompt."""
        if width is None:
            width = self._width()

        if get_app().vi_state.input_mode == InputMode.INSERT:
            token = prompts.Token.InsertPrompt
        else:
            token = prompts.Token.NavPrompt

        return [(token, " " * (width - 2) + self._continuation)]

    def out_prompt_tokens(self) -> List[Tuple[_TokenType, str]]:
        """Return out prompt."""
        return []


config.TerminalIPythonApp.display_banner = True
config.TerminalInteractiveShell.confirm_exit = False
config.TerminalInteractiveShell.editing_mode = "vi"
config.TerminalInteractiveShell.editor = "nvim"
config.TerminalInteractiveShell.true_color = True
config.TerminalInteractiveShell.prompts_class = Prompt
config.TerminalInteractiveShell.autoindent = False
config.TerminalInteractiveShell.auto_match = False
config.TerminalInteractiveShell.highlighting_style = GruvboxStyle
config.TerminalInteractiveShell.highlighting_style_overrides = {
    Token.InsertPrompt: Color.neutral_blue,
    Token.NavPrompt: Color.neutral_blue,
    Token.InsertPromptNum: f"{Color.neutral_blue} bold",
    Token.NavPromptNum: f"{Color.neutral_blue} bold",
}
