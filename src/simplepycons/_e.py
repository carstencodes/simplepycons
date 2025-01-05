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


class EIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "e"

    @property
    def original_file_name(self) -> "str":
        return "e.svg"

    @property
    def title(self) -> "str":
        return "/e/"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>/e/</title>
     <path d="M.004 12.004A12.012 12.012 0 0 0 12 24a2.27 2.27 0 0 0
 2.266-2.266A2.27 2.27 0 0 0 12 19.467c-4.116
 0-7.463-3.347-7.463-7.463S7.884 4.541 12 4.541c3.323 0 6.15 2.186
 7.111 5.197H12a2.27 2.27 0 0 0-2.266 2.266A2.27 2.27 0 0 0 12
 14.27h9.73a2.27 2.27 0 0 0 2.266-2.266A12.02 12.02 0 0 0 12
 0C5.385.008.004 5.39.004 12.004" />
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
