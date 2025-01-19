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


class UltralyticsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ultralytics"

    @property
    def original_file_name(self) -> "str":
        return "ultralytics.svg"

    @property
    def title(self) -> "str":
        return "Ultralytics"

    @property
    def primary_color(self) -> "str":
        return "#111F68"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ultralytics</title>
     <path d="m12.736 7.341-.002 2.897c.012 3.953-3.188 7.177-7.098
 7.171-1.553-.003-2.967-.48-4.112-1.313 2.056 3.725 5.999 6.24 10.48
 6.245 6.511-.003 11.891-5.343 11.992-11.91l-.002-.027c.006-.151
 0-2.951.006-3.075-.01-3.116-2.538-5.677-5.63-5.67-3.105-.006-5.645
 2.54-5.634 5.683zM5.629 4.573C2.525 4.573 0 7.118 0 10.246s2.525
 5.673 5.63 5.673c3.103 0 5.629-2.545
 5.629-5.673s-2.526-5.673-5.63-5.673" />
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
