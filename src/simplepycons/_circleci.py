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


class CircleciIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "circleci"

    @property
    def original_file_name(self) -> "str":
        return "circleci.svg"

    @property
    def title(self) -> "str":
        return "CircleCI"

    @property
    def primary_color(self) -> "str":
        return "#343434"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CircleCI</title>
     <path d="M8.963 12c0-1.584 1.284-2.855 2.855-2.855 1.572 0 2.856
 1.284 2.856 2.855 0 1.572-1.284 2.856-2.856 2.856-1.57
 0-2.855-1.284-2.855-2.856zm2.855-12C6.215 0 1.522 3.84.19
 9.025c-.01.036-.01.07-.01.12 0 .313.252.576.575.576H5.59c.23 0
 .433-.13.517-.333.997-2.16 3.18-3.672 5.712-3.672 3.466 0 6.286 2.82
 6.286 6.287 0 3.47-2.82 6.29-6.29 6.29-2.53
 0-4.714-1.5-5.71-3.673-.097-.19-.29-.336-.517-.336H.755c-.312
 0-.575.253-.575.576 0 .037.014.072.014.12C1.514 20.16 6.214 24 11.818
 24c6.624 0 12-5.375 12-12 0-6.623-5.376-12-12-12z" />
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
