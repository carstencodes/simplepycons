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


class SimplelocalizeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "simplelocalize"

    @property
    def original_file_name(self) -> "str":
        return "simplelocalize.svg"

    @property
    def title(self) -> "str":
        return "SimpleLocalize"

    @property
    def primary_color(self) -> "str":
        return "#222B33"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SimpleLocalize</title>
     <path d="M9.62 1.5q1.63 0 3.017.834a6.1 6.1 0 0 1 2.175 2.197 3.5
 3.5 0 0 1 1.988-.606q1.5 0 2.55 1.06 1.05 1.062 1.05 2.577a4 4 0 0
 1-.225 1.327q1.65.34 2.738 1.667Q24 11.882 24 13.625q0 1.326-.637
 2.444a4.7 4.7 0 0 1-1.666 1.715c-1.966 1.409-6.07 3.414-11.223
 4.683-1.866.459 3.785-3.98.853-3.98q-.15 0-.24-.011L5.4 18.475a5.17
 5.17 0 0 1-2.7-.74 5.53 5.53 0 0 1-1.969-1.99A5.3 5.3 0 0 1 0
 13.02q0-1.78 1.013-3.183T3.6 7.866v-.303a6 6 0 0 1 .806-3.032A6 6 0 0
 1 6.6 2.315 5.86 5.86 0 0 1 9.62 1.5" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
