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


class SymphonyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "symphony"

    @property
    def original_file_name(self) -> "str":
        return "symphony.svg"

    @property
    def title(self) -> "str":
        return "Symphony"

    @property
    def primary_color(self) -> "str":
        return "#0098FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Symphony</title>
     <path d="M20.471 8.118v-4.22c0-.864-.468-1.677-1.22-2.12C18.124
 1.113 15.684 0 12 0S5.876 1.113 4.75 1.777a2.476 2.476 0 0 0-1.22
 2.12v6.338l13.412 3.882v2.824c0 .382-.24.65-.648.849L12
 19.941l-4.315-2.162c-.386-.188-.626-.456-.626-.838v-2.118L3.53
 13.764v3.177c0 1.744 1 3.228 2.588 4.001L12 24l5.86-3.047c1.61-.784
 2.61-2.268 2.61-4.011v-5.294L7.059 7.765V4.542C8.017 4.08 9.651 3.529
 12 3.529c2.349 0 3.983.55 4.941 1.013v2.517l3.53 1.059z" />
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
