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


class OpnsenseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "opnsense"

    @property
    def original_file_name(self) -> "str":
        return "opnsense.svg"

    @property
    def title(self) -> "str":
        return "OPNsense"

    @property
    def primary_color(self) -> "str":
        return "#E44A20"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OPNsense</title>
     <path d="M5.25 0v5.25h13.5v13.5H24V7.5L16.5 0Zm13.5
 18.75H5.25V5.25H0V16.5L7.5 24h11.25Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/opnsense/core/blob/f4b69b9
b565d2747eb40d7d23e060f4a3c81a071/src/opnsense/www/themes/opnsense/bui'''

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
