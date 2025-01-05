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


class PoetryIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "poetry"

    @property
    def original_file_name(self) -> "str":
        return "poetry.svg"

    @property
    def title(self) -> "str":
        return "Poetry"

    @property
    def primary_color(self) -> "str":
        return "#60A5FA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Poetry</title>
     <path d="M21.604 0a19.144 19.144 0 0 1-5.268 13.213L2.396
 0l13.583 13.583a19.149 19.149 0 0 1-13.583 5.624V0h19.208Zm-1.911
 17.297A24.455 24.455 0 0 1 7.189 24l-4.053-4.053a19.91 19.91 0 0 0
 13.37-5.838l3.187 3.188Z" />
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
