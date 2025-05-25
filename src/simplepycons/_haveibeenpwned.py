#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class HaveIBeenPwnedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "haveibeenpwned"

    @property
    def original_file_name(self) -> "str":
        return "haveibeenpwned.svg"

    @property
    def title(self) -> "str":
        return "Have I Been Pwned"

    @property
    def primary_color(self) -> "str":
        return "#030304"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Have I Been Pwned</title>
     <path d="M1.89 3.872 0 13.598h4.7l1.889-9.726ZM7.171 8.56l-.98
 5.038h4.7l.98-5.038Zm5.936 1.306-.723 3.732h4.7l.722-3.732Zm6.192
 0-.723 3.732h4.7L24 9.866ZM5.912 15.09l-.979 5.038h4.7l.98-5.038z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/HaveIBeenPwned/Branding/bl'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from [
            "HIBP",
        ]
