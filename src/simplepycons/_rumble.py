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


class RumbleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rumble"

    @property
    def original_file_name(self) -> "str":
        return "rumble.svg"

    @property
    def title(self) -> "str":
        return "Rumble"

    @property
    def primary_color(self) -> "str":
        return "#85C742"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rumble</title>
     <path d="M14.4528
 13.5458c.8064-.6542.9297-1.8381.2756-2.6445a1.8802 1.8802 0 0
 0-.2756-.2756 21.2127 21.2127 0 0
 0-4.3121-2.776c-1.066-.51-2.256.2-2.4261 1.414a23.5226 23.5226 0 0
 0-.14 5.5021c.116 1.23 1.292 1.964 2.372 1.492a19.6285 19.6285 0 0 0
 4.5062-2.704v-.008zm6.9322-5.4002c2.0335 2.228 2.0396 5.637.014
 7.8723A26.1487 26.1487 0 0 1 8.2946
 23.846c-2.6848.6713-5.4168-.914-6.1662-3.5781-1.524-5.2002-1.3-11.0803.17-16.3045.772-2.744
 3.3521-4.4661 6.0102-3.832 4.9242 1.174 9.5443 4.196 13.0764
 8.0121v.002z" />
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
