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


class PhpstormIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "phpstorm"

    @property
    def original_file_name(self) -> "str":
        return "phpstorm.svg"

    @property
    def title(self) -> "str":
        return "PhpStorm"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PhpStorm</title>
     <path d="M7.833
 6.611v-.055c0-1-.667-1.5-1.778-1.5H4.389v3.056h1.722c1.111-.001
 1.722-.668 1.722-1.501zM0 0v24h24V0H0zm2.167 3.111h4.056c2.389 0
 3.833 1.389 3.833 3.445v.055c0 2.333-1.778 3.5-4.056
 3.5H4.333v3H2.167v-10zM11.278 21h-9v-1.5h9V21zM18.5 10.222c0 2-1.5
 3.111-3.667 3.111-1.5-.056-3-.611-4.222-1.667l1.278-1.556c.89.722
 1.833 1.222 3 1.222.889 0 1.444-.333
 1.444-.944v-.056c0-.555-.333-.833-2-1.277C12.333 8.555 11 8 11
 6v-.056c0-1.833 1.444-3 3.5-3 1.444 0 2.723.444 3.723 1.278l-1.167
 1.667c-.889-.611-1.777-1-2.611-1-.833 0-1.278.389-1.278.889v.056c0
 .667.445.889 2.167 1.333 2 .556 3.167 1.278 3.167 3v.055z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.jetbrains.com/company/brand/logos'''

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
        yield from []
