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


class KThreeSIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "k3s"

    @property
    def original_file_name(self) -> "str":
        return "k3s.svg"

    @property
    def title(self) -> "str":
        return "K3s"

    @property
    def primary_color(self) -> "str":
        return "#FFC61C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>K3s</title>
     <path d="M21.46 2.172H2.54A2.548 2.548 0 0 0 0 4.712v14.575a2.548
 2.548 0 0 0 2.54 2.54h18.92a2.548 2.548 0 0 0 2.54-2.54V4.713a2.548
 2.548 0 0 0-2.54-2.54ZM10.14 16.465 5.524 19.15a1.235 1.235 0 1
 1-1.242-2.137L8.9 14.33a1.235 1.235 0 1 1 1.241
 2.136zm1.817-4.088h-.006a1.235 1.235 0 0 1-1.23-1.24l.023-5.32a1.236
 1.236 0 0 1 1.236-1.23h.005a1.235 1.235 0 0 1 1.23 1.241l-.023
 5.32a1.236 1.236 0 0 1-1.235 1.23zm8.17 6.32a1.235 1.235 0 0
 1-1.688.453l-4.624-2.67a1.235 1.235 0 1 1 1.235-2.14l4.624 2.67a1.235
 1.235 0 0 1 .452 1.688z" />
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
