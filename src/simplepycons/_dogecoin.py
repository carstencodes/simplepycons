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


class DogecoinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dogecoin"

    @property
    def original_file_name(self) -> "str":
        return "dogecoin.svg"

    @property
    def title(self) -> "str":
        return "Dogecoin"

    @property
    def primary_color(self) -> "str":
        return "#C2A633"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dogecoin</title>
     <path d="M12.288
 7.908h-1.715v3.38h2.697v1.415h-2.697v3.38h1.799c.462 0 3.794.052
 3.789-3.933-.005-3.984-3.232-4.242-3.873-4.242zM12 0C5.373 0 0 5.373
 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm.472
 18.481H8.126v-5.778H6.594v-1.415h1.532V5.511h3.73c.882 0 6.727-.183
 6.727 6.594-.001 6.888-6.111 6.376-6.111 6.376z" />
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
