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


class AsanaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "asana"

    @property
    def original_file_name(self) -> "str":
        return "asana.svg"

    @property
    def title(self) -> "str":
        return "Asana"

    @property
    def primary_color(self) -> "str":
        return "#F06A6A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Asana</title>
     <path d="M18.78 12.653c-2.882 0-5.22 2.336-5.22 5.22s2.338 5.22
 5.22 5.22 5.22-2.34 5.22-5.22-2.336-5.22-5.22-5.22zm-13.56 0c-2.88
 0-5.22 2.337-5.22 5.22s2.338 5.22 5.22 5.22 5.22-2.338
 5.22-5.22-2.336-5.22-5.22-5.22zm12-6.525c0 2.883-2.337 5.22-5.22
 5.22-2.882 0-5.22-2.337-5.22-5.22 0-2.88 2.338-5.22 5.22-5.22 2.883 0
 5.22 2.34 5.22 5.22z" />
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
