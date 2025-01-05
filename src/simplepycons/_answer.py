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


class AnswerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "answer"

    @property
    def original_file_name(self) -> "str":
        return "answer.svg"

    @property
    def title(self) -> "str":
        return "Answer"

    @property
    def primary_color(self) -> "str":
        return "#0033FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Answer</title>
     <path d="M5.486 0c-1.92 0-2.881 0-3.615.373A3.428 3.428 0 0 0
 .373 1.871C-.001 2.605 0 3.566 0 5.486v9.6c0 1.92 0 2.88.373
 3.613.329.645.853 1.17 1.498 1.498.734.374 1.695.375
 3.615.375h11.657V24l.793-.396c2.201-1.101 3.3-1.652 4.105-2.473a6.852
 6.852 0 0 0 1.584-2.56C24 17.483 24 16.251 24 13.79V5.486c0-1.92
 0-2.881-.373-3.615A3.428 3.428 0 0 0 22.129.373C21.395-.001 20.434 0
 18.514 0H5.486zm1.371 10.285h10.286a5.142 5.142 0 0
 1-10.286.024v-.024z" />
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
