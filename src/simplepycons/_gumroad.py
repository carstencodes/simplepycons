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


class GumroadIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gumroad"

    @property
    def original_file_name(self) -> "str":
        return "gumroad.svg"

    @property
    def title(self) -> "str":
        return "Gumroad"

    @property
    def primary_color(self) -> "str":
        return "#FF90E8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gumroad</title>
     <path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0Zm-.007 5.12c4.48 0 5.995 3.025 6.064
 4.744h-3.239c-.069-.962-.897-2.406-2.896-2.406-2.136 0-3.514
 1.857-3.514 4.126 0 2.27 1.378 4.125 3.514 4.125 1.93 0 2.758-1.512
 3.103-3.025h-3.103v-1.238h6.509v6.327h-2.855v-3.989c-.207 1.444-1.102
 4.264-4.617 4.264-3.516 0-5.584-2.82-5.584-6.326 0-3.645 2.276-6.602
 6.618-6.602z" />
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
