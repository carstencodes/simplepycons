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


class PeakDesignIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "peakdesign"

    @property
    def original_file_name(self) -> "str":
        return "peakdesign.svg"

    @property
    def title(self) -> "str":
        return "Peak Design"

    @property
    def primary_color(self) -> "str":
        return "#1C1B1C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Peak Design</title>
     <path d="m24 10.523-9.446 6.493-4.74-3.271 4.723-3.255 3.738 2.57
 3.705-2.537zm-6.743 3.255-2.72-1.886-2.704 1.853 2.737
 1.869zm-7.794-.284-3.738-2.57-3.706 2.554h-2.019l9.43-6.493 4.756
 3.255zm-2.737-3.254 2.737 1.869 2.704-1.869-2.737-1.87z" />
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
