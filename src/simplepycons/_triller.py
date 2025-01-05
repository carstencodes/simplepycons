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


class TrillerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "triller"

    @property
    def original_file_name(self) -> "str":
        return "triller.svg"

    @property
    def title(self) -> "str":
        return "Triller"

    @property
    def primary_color(self) -> "str":
        return "#FF0089"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Triller</title>
     <path d="M15.548 5.216L7.005 20.012l-.29-.167 8.54-14.788a9.365
 9.365 0 0 0-6.07-.906L2.73 15.333l-.609 1.055a9.34 9.34 0 0 0 3.818
 4.806l-1.522 2.64.289.166 2.303-3.987h-.002a9.367 9.367 0 0 0
 6.068.905l6.321-10.945.287.167-6.168 10.683-.964 1.67a9.322 9.322 0 0
 0 7.55-7.555 9.267 9.267 0 0 0-.413-4.802l2.299-3.982-.29-.167L20.14
 8.68a9.343 9.343 0 0 0-3.816-4.806zm-5.842-2.64a9.324 9.324 0 0
 0-7.132 12.359L8.893 3.989l.292.162L11.483.167 11.193 0z" />
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
