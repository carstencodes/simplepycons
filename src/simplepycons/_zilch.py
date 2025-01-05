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


class ZilchIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zilch"

    @property
    def original_file_name(self) -> "str":
        return "zilch.svg"

    @property
    def title(self) -> "str":
        return "Zilch"

    @property
    def primary_color(self) -> "str":
        return "#00D287"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zilch</title>
     <path d="M4.421 6.149c3.292-2.011 6.584-4.036
 9.862-6.046a.702.702 0 0 1 .83.073c1.312 1.18 2.637 2.36 3.948
 3.54a.694.694 0 0 1 .175.815 1737.248 1737.248 0 0 1-4.341
 9.338.61.61 0 0 0 .408.845c1.427.335 2.855.656 4.283.991a.546.546 0 0
 1 .204.976c-3.234 2.375-6.483 4.749-9.717 7.124a.986.986 0 0
 1-1.136.029l-4.633-3.016a.691.691 0 0 1-.248-.888c1.326-2.812
 2.666-5.623 3.992-8.421a.78.78 0 0 0-.146-.859 802.196 802.196 0 0
 0-3.583-3.569c-.277-.262-.219-.729.102-.932Z" />
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
