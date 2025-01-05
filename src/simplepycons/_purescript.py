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


class PurescriptIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "purescript"

    @property
    def original_file_name(self) -> "str":
        return "purescript.svg"

    @property
    def title(self) -> "str":
        return "PureScript"

    @property
    def primary_color(self) -> "str":
        return "#14161A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PureScript</title>
     <path d="M19.166 4.6l-1.24 1.24 3.97 3.97-3.97 3.97 1.24 1.24
 4.58-4.6a.87.87 0 0 0 0-1.23zM6.955 6.74l1.87
 1.75h8.23l-1.87-1.75zm-2.1 2.24l-4.6 4.6a.87.87 0 0 0 0 1.23l4.6 4.59
 1.23-1.24-3.97-3.97 3.97-3.97-1.24-1.24zm3.97 2.14l-1.87
 1.76h8.23l1.87-1.76zm-1.87 4.39l1.87 1.75h8.23l-1.87-1.75z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/purescript/logo/tree/1e7a5'''

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
