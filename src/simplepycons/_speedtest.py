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


class SpeedtestIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "speedtest"

    @property
    def original_file_name(self) -> "str":
        return "speedtest.svg"

    @property
    def title(self) -> "str":
        return "Speedtest"

    @property
    def primary_color(self) -> "str":
        return "#141526"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Speedtest</title>
     <path d="M11.628 16.186l-2.047-2.14 6.791-5.953 1.21 1.302zm8.837
 6.047c2.14-2.14 3.535-5.117 3.535-8.466 0-6.604-5.395-12-12-12s-12
 5.396-12 12c0 3.35 1.302 6.326 3.535
 8.466l1.674-1.675c-1.767-1.767-2.79-4.093-2.79-6.79A9.568 9.568 0 0 1
 12 4.185a9.568 9.568 0 0 1 9.581 9.581c0 2.605-1.116 5.024-2.79
 6.791Z" />
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
