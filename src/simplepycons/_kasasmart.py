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


class KasaSmartIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kasasmart"

    @property
    def original_file_name(self) -> "str":
        return "kasasmart.svg"

    @property
    def title(self) -> "str":
        return "Kasa Smart"

    @property
    def primary_color(self) -> "str":
        return "#4ACBD6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kasa Smart</title>
     <path d="M12 0c-.5 0-1 .25-1.5.75L7.97 3.28l8.83 8.83c1 1 1.5 2
 1.5 3V24h3.3c1.6 0 2.4-.8 2.4-2.4v-8.85c0-1-.5-2-1.5-3l-9-9C13 .25
 12.5 0 12 0zM6.9 4.34L2.89 8.37 9.6 15.1c1 1 1.5 2 1.5
 3V24h5.7v-8.89c-.03-.83-.6-1.46-1.06-1.94L6.91 4.34zm-5.08
 5.1l-.32.31c-1 1-1.5 2-1.5 3v8.85C0 23.2.8 24 2.4
 24h7.2v-5.9c-.03-.8-.56-1.42-1.06-1.95Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.tp-link.com/us/support/download/h'''

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
