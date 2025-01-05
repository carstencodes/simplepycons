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


class NationalRailIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nationalrail"

    @property
    def original_file_name(self) -> "str":
        return "nationalrail.svg"

    @property
    def title(self) -> "str":
        return "National Rail"

    @property
    def primary_color(self) -> "str":
        return "#003366"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>National Rail</title>
     <path d="M0 12C0 5.373 5.372 0 12 0c6.627 0 11.999 5.373 11.999
 12 0 6.628-5.372 12-11.999 12-6.628 0-12-5.372-12-12Zm6.195-5.842
 6.076 2.794H2.835v1.884h9.499l-4.616 2.246H2.835v1.868h4.883l5.778
 2.795h4.333l-6.092-2.795h9.469v-1.868h-9.453l4.616-2.246h4.837V8.952h-4.868l-5.777-2.794H6.195"
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
