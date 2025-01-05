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


class FoursquareIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "foursquare"

    @property
    def original_file_name(self) -> "str":
        return "foursquare.svg"

    @property
    def title(self) -> "str":
        return "Foursquare"

    @property
    def primary_color(self) -> "str":
        return "#3333FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Foursquare</title>
     <path d="M2.376
 0h7.338v1.204h-6.12v3.372h5.44V5.78h-5.44v4.874H2.376V0zm-.208
 20.16l1.19-.268c.213 1.473 1.232 2.352 2.89 2.352 1.487 0 2.664-.694
 2.664-1.828
 0-.807-.595-1.487-2.919-2.18-2.635-.752-3.513-1.715-3.513-3.13
 0-1.829 1.473-2.805 3.613-2.805 2.393 0 3.456 1.218 3.825
 2.89l-1.19.269c-.299-1.374-1.233-1.955-2.679-1.955-1.36
 0-2.323.51-2.323 1.487 0 .793.624 1.403 2.777 2.083 2.565.793 3.67
 1.658 3.67 3.301 0 2.04-1.715 3.103-3.896
 3.103-2.281-.003-3.84-1.193-4.11-3.318zm9.223-2.238c0-3.159
 2.068-5.624 5.242-5.624 3.159 0 5.2 2.479 5.2 5.624 0 1.573-.525
 2.933-1.404 3.925a36.155 36.155 0 011.247 1.303l-.879.85a57.16 57.16
 0 00-1.303-1.346c-.807.524-1.771.822-2.861.822-3.061
 0-5.242-2.352-5.242-5.554zm7.181 3.825a31.241 31.241 0
 00-1.247-1.148l.85-.863a36.537 36.537 0 011.331 1.218c.638-.764
 1.02-1.813 1.02-3.046 0-2.493-1.516-4.39-3.896-4.39s-3.91 1.897-3.91
 4.39c0 2.565 1.658 4.363 3.91 4.363.725 0 1.375-.184 1.942-.524z" />
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
