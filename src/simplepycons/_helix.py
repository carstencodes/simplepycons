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


class HelixIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "helix"

    @property
    def original_file_name(self) -> "str":
        return "helix.svg"

    @property
    def title(self) -> "str":
        return "Helix"

    @property
    def primary_color(self) -> "str":
        return "#281733"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Helix</title>
     <path d="M12.968 4.97 4.364 0v3.55c0 .449.239.863.627 1.087l4.276
 2.47zm5.339 3.083-3.7 2.138 4.86
 2.807c.11-.19.17-.407.17-.633V9.552c0-.452-.241-.87-.633-1.096zm1.33
 12.397c0-.449-.24-.863-.627-1.087l-4.253-2.456-3.7 2.137L19.637
 24zm-13.92-4.49 3.7-2.137c-2.703-1.562-4.884-2.82-4.884-2.82a1.26
 1.26 0 0 0-.17.632v2.813c0 .452.242.87.634 1.096zm-.287-1.252a.93.93
 0 0 1
 .343-.342l12.455-7.194-.01.007.786-.455c.392-.226.633-.643.633-1.096V2.815c0-.452-.241-.87-.633-1.096l-.765-.442a.944.944
 0 0 1-.005 1.617l-.006.004-13.231 7.641a1.26 1.26 0 0 0-.633
 1.096v2.813c0 .453.24.87.633 1.096l.72.416h.002a.944.944 0 0
 1-.29-1.252m12.873-6.652a.945.945 0 0 1-.07 1.575l-.005.004-13.231
 7.641a1.26 1.26 0 0 0-.633 1.096v2.813c0 .452.24.87.633
 1.096l.765.442a.945.945 0 0 1
 .01-1.62l12.456-7.194-.01.006.786-.454c.392-.226.633-.644.633-1.096V9.552c0-.453-.241-.87-.633-1.096l-.697-.403z"
 />
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
