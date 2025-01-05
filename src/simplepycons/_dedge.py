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


class DedgeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dedge"

    @property
    def original_file_name(self) -> "str":
        return "dedge.svg"

    @property
    def title(self) -> "str":
        return "D-EDGE"

    @property
    def primary_color(self) -> "str":
        return "#432975"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>D-EDGE</title>
     <path d="M19.986 0v8.338C16.09 2.93 7.61 2.8 3.74 8.733-.523
 15.27 4.191 23.99 11.996 24h.001c5.447-.003 9.872-4.43
 9.87-9.877V0Zm-7.99 6.14a8.004 8.004 0 0 1 7.99 7.988 7.986 7.986 0 0
 1-4.93 7.381 7.986 7.986 0 0 1-8.707-1.73 7.985 7.985 0 0
 1-1.733-8.707 7.986 7.986 0 0 1 7.38-4.932Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/d-edge/JoinUs/blob/4d8b5cf'''

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
