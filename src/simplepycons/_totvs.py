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


class TotvsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "totvs"

    @property
    def original_file_name(self) -> "str":
        return "totvs.svg"

    @property
    def title(self) -> "str":
        return "TOTVS"

    @property
    def primary_color(self) -> "str":
        return "#363636"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TOTVS</title>
     <path d="M12 0C5.385 0 0 5.339 0 12c0 6.614 5.385 12 12 12 6.614
 0 12-5.386 12-12S18.614 0 12 0ZM8.648 3.813c1.275-.068 10.697 2.302
 11.43 2.943.614.85.614 9.118 0 9.685-.284.095-2.127-.283-4.205-.755 0
 2.031-.143 3.966-.426
 4.203-.756.236-10.772-2.267-11.527-2.928-.615-.85-.615-9.119
 0-9.686.283-.094 2.079.284 4.205.756
 0-2.031.142-3.969.425-4.205a.448.448 0 0 1 .098-.013Zm-.523
 4.265c-.048 2.362.095 4.961.425 5.434.426.378 4.158 1.418 7.276
 2.174.047-2.41-.095-5.008-.426-5.481-.425-.378-4.157-1.418-7.275-2.127Z"
 />
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
