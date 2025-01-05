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


class CoggleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "coggle"

    @property
    def original_file_name(self) -> "str":
        return "coggle.svg"

    @property
    def title(self) -> "str":
        return "Coggle"

    @property
    def primary_color(self) -> "str":
        return "#9ED56B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Coggle</title>
     <path d="M3.684 0A3.683 3.683 0 0 0 0 3.684v10.92c2.052-.535
 3.606-1.577 5.158-3.13h7.367v7.368c-1.88 1.88-5.438 4.598-8.052
 5.158h15.843A3.683 3.683 0 0 0 24 20.316V8.881c-1.544.537-3.087
 1.575-4.63 3.119l-4.74 4.736V9.37H7.265l3.683-3.685c2.35-2.35
 5.96-5.119 8.58-5.684H3.684z" />
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
