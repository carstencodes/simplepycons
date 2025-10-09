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


class BlueskyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bluesky"

    @property
    def original_file_name(self) -> "str":
        return "bluesky.svg"

    @property
    def title(self) -> "str":
        return "Bluesky"

    @property
    def primary_color(self) -> "str":
        return "#1185FE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bluesky</title>
     <path d="M5.202 2.857C7.954 4.922 10.913 9.11 12
 11.358c1.087-2.247 4.046-6.436 6.798-8.501C20.783 1.366 24 .213 24
 3.883c0 .732-.42 6.156-.667 7.037-.856 3.061-3.978 3.842-6.755 3.37
 4.854.826 6.089 3.562 3.422 6.299-5.065
 5.196-7.28-1.304-7.847-2.97-.104-.305-.152-.448-.153-.327
 0-.121-.05.022-.153.327-.568 1.666-2.782 8.166-7.847
 2.97-2.667-2.737-1.432-5.473
 3.422-6.3-2.777.473-5.899-.308-6.755-3.369C.42 10.04 0 4.615 0
 3.883c0-3.67 3.217-2.517 5.202-1.026" />
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
        yield from [
            "bsky",
        ]
