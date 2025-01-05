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


class MarvelappIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "marvelapp"

    @property
    def original_file_name(self) -> "str":
        return "marvelapp.svg"

    @property
    def title(self) -> "str":
        return "MarvelApp"

    @property
    def primary_color(self) -> "str":
        return "#1FB6FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MarvelApp</title>
     <path d="M10.339 8.13c1.373 0-1.162 7.076-.845 10.138.317 3.063
 3.696 2.218 3.485.423-.423-3.063 1.69-12.672 3.696-12.672 1.478
 0-1.69 6.547-1.056 10.665.422 2.64 4.012 1.901 3.59.106-1.162-5.386
 2.64-10.56 2.112-14.361C21.11.845 20.159 0 19.209 0c-3.379 0-6.125
 6.97-6.125 6.97s.423-3.908-2.428-4.119C6.643 2.64 2.525 12.777 2.63
 21.964c.106 2.957 3.696 2.429 3.485.106-.211-4.12 2.112-13.94
 4.225-13.94z" />
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
