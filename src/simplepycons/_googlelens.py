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


class GoogleLensIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlelens"

    @property
    def original_file_name(self) -> "str":
        return "googlelens.svg"

    @property
    def title(self) -> "str":
        return "Google Lens"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Lens</title>
     <path d="M12 16.667a4.666 4.666 0 100-9.333 4.666 4.666 0 000
 9.333m8 6a2.666 2.666 0 100-5.333 2.666 2.666 0 000
 5.333m-13.333-2a3.343 3.343 0 01-3.334-3.334v-2.666H0v2.666A6.665
 6.665 0 006.667 24h2.666v-3.333zm-3.334-14c0-1.834 1.5-3.334
 3.334-3.334h2.666V0H6.667A6.665 6.665 0 000
 6.667v2.666h3.333zm14-3.334c1.834 0 3.334 1.5 3.334
 3.334v2.666H24V6.667A6.665 6.665 0 0017.333 0h-2.666v3.333Z" />
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
