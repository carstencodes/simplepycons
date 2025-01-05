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


class StreamrunnersIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "streamrunners"

    @property
    def original_file_name(self) -> "str":
        return "streamrunners.svg"

    @property
    def title(self) -> "str":
        return "StreamRunners"

    @property
    def primary_color(self) -> "str":
        return "#6644F8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>StreamRunners</title>
     <path d="M23.572 12.737a.854.854 0 0 0
 0-1.48l-12.66-7.31c-.695-.4-1.51.292-1.225 1.043l.98
 2.587c.106.28-.1.578-.4.578H7.55c-.658 0-1.275.32-1.656.857L3.632
 12.21h8.553c.02 0 .034.02.027.04-.847 2.253-1.69 4.508-2.537
 6.761-.282.75.532 1.44 1.227 1.04zM.001 17.052a.005.005 0 0 0 0
 .006h8.297a.64.64 0 0 0 .612-.452l.656-2.134a.64.64 0 0
 0-.613-.83l-6.805.018a.078.078 0 0 0-.067.036C1.386 14.813.694 15.933
 0 17.052Z" />
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
