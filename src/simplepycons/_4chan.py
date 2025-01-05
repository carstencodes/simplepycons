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


class FourChanIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "4chan"

    @property
    def original_file_name(self) -> "str":
        return "4chan.svg"

    @property
    def title(self) -> "str":
        return "4chan"

    @property
    def primary_color(self) -> "str":
        return "#006600"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>4chan</title>
     <path d="M11.07 8.82S9.803 1.079 5.145 1.097C2.006 1.109.78 4.124
 3.055 4.802c0 0-2.698.973-2.698 2.697 0 1.725 4.274 3.54 10.713
 1.32zm1.931 5.924s.904 7.791 5.558 7.991c3.136.135 4.503-2.82
 2.262-3.604 0 0 2.74-.845
 2.82-2.567.08-1.723-4.105-3.737-10.64-1.82zm-3.672-1.55s-7.532
 2.19-6.952 6.813c.39 3.114 3.53 3.969 3.93 1.63 0 0 1.29 2.559 3.002
 2.351 1.712-.208 3-4.67.02-10.794zm5.623-2.467s7.727-1.35
 7.66-6.008c-.046-3.138-3.074-4.333-3.728-2.051 0
 0-1-2.686-2.726-2.668-1.724.018-3.494 4.312-1.206 10.727z" />
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
