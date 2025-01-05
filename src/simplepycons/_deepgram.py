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


class DeepgramIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "deepgram"

    @property
    def original_file_name(self) -> "str":
        return "deepgram.svg"

    @property
    def title(self) -> "str":
        return "Deepgram"

    @property
    def primary_color(self) -> "str":
        return "#13EF93"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Deepgram</title>
     <path d="M11.203 24H1.517a.364.364 0 0
 1-.258-.62l6.239-6.275a.366.366 0 0 1 .259-.108h3.52c2.723 0
 5.025-2.127 5.107-4.845a5.004 5.004 0 0 0-4.999-5.148H7.613v4.646c0
 .2-.164.364-.365.364H.968a.365.365 0 0 1-.363-.364V.364C.605.164.768
 0 .969 0h10.416c6.684 0 12.111 5.485 12.01 12.187C23.293 18.77 17.794
 24 11.202 24z" />
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
