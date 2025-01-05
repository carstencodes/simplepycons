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


class CodingNinjasIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codingninjas"

    @property
    def original_file_name(self) -> "str":
        return "codingninjas.svg"

    @property
    def title(self) -> "str":
        return "Coding Ninjas"

    @property
    def primary_color(self) -> "str":
        return "#DD6620"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Coding Ninjas</title>
     <path d="M23.198 0c-.499.264-1.209.675-1.79.984a542.82 542.82 0
 000 6.242c.995-.526 1.761-.834 1.79-2.066V0zM8.743.181C7.298.144
 5.613.65 4.47 1.414c-1.17.8-1.987 1.869-2.572 3.179A16.787 16.787 0
 00.9 8.87c-.15 1.483-.128 3.079.025 4.677.27 1.855.601 3.724 1.616
 5.456 1.57 2.62 4.313 4.109 7.262 4.19 3.41.246 7.233.53
 11.411.807.022-2.005.01-5.418
 0-6.25-3.206-.21-7.398-.524-11.047-.782-.443-.043-.896-.056-1.324-.172-1.086-.295-1.806-.802-2.374-1.757-.643-1.107-.875-2.832-.797-4.294.11-1.27.287-2.41
 1.244-3.44.669-.56 1.307-.758 2.161-.84 5.17.345 7.609.53
 12.137.858.032-1.133.01-3.46 0-6.229C16.561.752 12.776.474
 8.743.181zm-.281 9.7c.174.675.338 1.305.729 1.903.537.832 1.375 1.127
 2.388.877.76-.196 1.581-.645 2.35-1.282zm12.974
 1.04l-5.447.689c.799.739 1.552 1.368 2.548 1.703.988.319 1.78.01
 2.308-.777.209-.329.56-1.148.591-1.614zm.842
 6.461c-.388.01-.665.198-.87.355.002 1.798 0 4.127 0 6.223.586-.297
 1.135-.644 1.793-.998-.005-1.454.002-3.137-.005-4.707a.904.904 0
 00-.917-.873z" />
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
