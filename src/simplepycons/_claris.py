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


class ClarisIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "claris"

    @property
    def original_file_name(self) -> "str":
        return "claris.svg"

    @property
    def title(self) -> "str":
        return "Claris"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Claris</title>
     <path d="M11.56 0a3.34 3.34 0 00-.57.043L22.947 12 10.99
 23.957c.132.022.307.043.57.043 6.626 0 12-5.375
 12-12s-5.374-12-12-12zm-1.535 2.414C4.738 2.414.44 6.713.44 12s4.3
 9.588 9.586 9.588c.264 0 .44-.023.57-.045L1.054 12l9.543-9.543a3.337
 3.337 0 00-.57-.043zm.746 2.457c-.263 0-.438.021-.57.043L17.287
 12l-7.086 7.086c.132.022.307.045.57.045 3.927 0 7.13-3.204
 7.13-7.131s-3.203-7.129-7.13-7.129zm-.416 2.434A4.701 4.701 0 005.66
 12a4.701 4.701 0 004.695 4.695c.264 0 .44-.023.57-.045L6.274
 12l4.653-4.65a3.296 3.296 0 00-.57-.045Z" />
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
