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


class BuddyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "buddy"

    @property
    def original_file_name(self) -> "str":
        return "buddy.svg"

    @property
    def title(self) -> "str":
        return "Buddy"

    @property
    def primary_color(self) -> "str":
        return "#1A86FD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Buddy</title>
     <path d="M21.7 5.307L12.945.253a1.892 1.892 0 00-1.891 0L2.299
 5.306a1.892 1.892 0 00-.945 1.638v10.11c0 .675.36 1.3.945 1.637l8.756
 5.056a1.892 1.892 0 001.89
 0l8.756-5.055c.585-.338.945-.962.945-1.638V6.945c0-.675-.36-1.3-.945-1.638zm-7.45
 7.753l-3.805 3.804-1.351-1.351 3.804-3.805-3.804-3.806 1.35-1.35
 3.805 3.805 1.351 1.35-1.35 1.353z" />
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
