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


class NineGagIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "9gag"

    @property
    def original_file_name(self) -> "str":
        return "9gag.svg"

    @property
    def title(self) -> "str":
        return "9GAG"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>9GAG</title>
     <path d="m17.279 21.008 5.193-2.995V5.992l-5.193-2.996C14.423
 1.348 12.048 0 12 0c-.048 0-2.423 1.348-5.279 2.996L1.528
 5.992v2.354l5.193 2.996c2.856 1.648 5.232 2.996 5.28 2.996.048 0
 1.469-.797 3.157-1.772a229.633 229.633 0 0 1 3.097-1.772c.016 0 .027
 1.096.027 2.437l-.002 2.436-3.076 1.772c-1.692.975-3.115 1.783-3.163
 1.795-.048.013-1.471-.776-3.162-1.752-1.69-.976-3.113-1.775-3.161-1.775-.155
 0-4.036 2.274-4.011 2.35.031.093 10.136 5.937 10.276 5.943.057.002
 2.44-1.344 5.296-2.992ZM9.847 8.391c-1.118-.65-2.033-1.2-2.033-1.222
 0-.071 4.06-2.376 4.186-2.376.125 0 4.186 2.305 4.186 2.376 0
 .063-4.047 2.375-4.184 2.39-.068.007-1.037-.519-2.155-1.168Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:9gag_'''

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
