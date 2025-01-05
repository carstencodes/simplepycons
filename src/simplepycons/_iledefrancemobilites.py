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


class IledefranceMobilitesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "iledefrancemobilites"

    @property
    def original_file_name(self) -> "str":
        return "iledefrancemobilites.svg"

    @property
    def title(self) -> "str":
        return "Île-de-France Mobilités"

    @property
    def primary_color(self) -> "str":
        return "#67B4E7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Île-de-France Mobilités</title>
     <path d="M18.54.001A5.461 5.447 0 0 1 24 5.447v13.107A5.461 5.447
 0 0 1 18.54 24H5.459A5.461 5.447 0 0 1 0 18.553V5.446A5.461 5.447 0 0
 1 5.46 0h13.081Zm-9.781 15.26c-1.365 1.816-2.503 3.405-3.925
 5.334-.34.454-.057.624.398.34.512-.34.967-.736
 1.309-1.247.3-.421.857-1.175
 1.448-1.977l.595-.808c.33-.445.646-.876.914-1.243.796-1.135
 2.047-1.023 2.9.17a398.137 397.144 0 0 0 3.242 4.481c.739 1.02
 2.957.851 3.924.794.17 0 .228-.17.17-.283a310.878 310.103 0 0
 0-4.663-6.467c-2.047-2.894-4.606-1.42-6.312.907ZM17.8 7.32c-2.9
 1.474-3.809 1.304-6.255 1.701-2.445.34-4.266.908-6.313
 3.064-.51.567-.74 1.021.058.624 2.9-1.475 3.81-1.305 6.254-1.702
 2.446-.34 4.267-.907
 6.314-3.064.512-.566.796-1.02-.057-.623Zm-5.06-4.142c-.966-.454-2.218.17-2.786
 1.419-.569 1.19-.228 2.553.74 3.007.966.454 2.217-.17
 2.786-1.42.568-1.246.228-2.609-.74-3.006Z" />
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
