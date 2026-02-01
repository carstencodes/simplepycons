#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class ConvexIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "convex"

    @property
    def original_file_name(self) -> "str":
        return "convex.svg"

    @property
    def title(self) -> "str":
        return "Convex"

    @property
    def primary_color(self) -> "str":
        return "#EE342F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Convex</title>
     <path d="M15.09 18.916c3.488-.387 6.776-2.246 8.586-5.348-.857
 7.673-9.247 12.522-16.095 9.545a3.47 3.47 0 0
 1-1.547-1.314c-1.539-2.417-2.044-5.492-1.318-8.282 2.077 3.584 6.3
 5.78 10.374 5.399m-10.501-7.65c-1.414 3.266-1.475 7.092.258
 10.24-6.1-4.59-6.033-14.41-.074-18.953a3.44 3.44 0 0 1
 1.893-.707c2.825-.15 5.695.942 7.708 2.977-4.09.04-8.073 2.66-9.785
 6.442m11.757-5.437C14.283 2.951 11.053.992 7.515.933c6.84-3.105
 15.253 1.929 16.17 9.37a3.6 3.6 0 0 1-.334 2.02c-1.278 2.594-3.647
 4.607-6.416 5.352 2.029-3.763 1.778-8.36-.589-11.847" />
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
