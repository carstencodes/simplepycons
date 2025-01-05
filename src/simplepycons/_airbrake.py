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


class AirbrakeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "airbrake"

    @property
    def original_file_name(self) -> "str":
        return "airbrake.svg"

    @property
    def title(self) -> "str":
        return "Airbrake"

    @property
    def primary_color(self) -> "str":
        return "#FFA500"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Airbrake</title>
     <path d="M15.815.576 24 23.424h-6.072L10.679.576Zm-6.456 0 1.872
 5.929-2.447 7.751c1.038.183 2.09.28 3.144.288.576 0 1.175-.048
 1.824-.096l1.151 3.912a28.7 28.7 0 0 1-2.951.169 26.568 26.568 0 0
 1-4.32-.361L5.88 23.424H0L8.181.576Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/airbrake/slate/blob/c116f2'''

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
