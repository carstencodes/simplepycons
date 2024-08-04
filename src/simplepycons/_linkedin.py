#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class LinkedinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "linkedin"

    @property
    def original_file_name(self) -> "str":
        return "linkedin.svg"

    @property
    def title(self) -> "str":
        return "LinkedIn"

    @property
    def primary_color(self) -> "str":
        return "#0A66C2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LinkedIn</title>
     <path d="M20.447
 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136
 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85
 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144
 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0
 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782
 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0
 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24
 22.271V1.729C24 .774 23.2 0 22.222 0h.003z" />
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
