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


class RuffIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ruff"

    @property
    def original_file_name(self) -> "str":
        return "ruff.svg"

    @property
    def title(self) -> "str":
        return "Ruff"

    @property
    def primary_color(self) -> "str":
        return "#D7FF64"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ruff</title>
     <path d="M3 0C1.338 0 0 1.338 0 3v18c0 1.662 1.338 3 3 3h18c1.662
 0 3-1.338 3-3V3c0-1.662-1.338-3-3-3Zm4.2 7.2h8.641c.53 0
 .959.43.959.959v3.266c0
 .53-.43.959-.959.959h-.961v.768h1.92V16.8h-4.416v-2.88h-.768v2.88H7.2Zm3.648
 3.648v.768h2.304v-.768z" />
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
