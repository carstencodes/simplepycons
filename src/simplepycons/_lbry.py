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


class LbryIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lbry"

    @property
    def original_file_name(self) -> "str":
        return "lbry.svg"

    @property
    def title(self) -> "str":
        return "LBRY"

    @property
    def primary_color(self) -> "str":
        return "#2F9176"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LBRY</title>
     <path d="M23.3493 14.1894l.169-1.0651-1.0315-.1775.0676-.4142
 1.4456.245-.2365 1.4795zm.152-5.495v1.1921l-11.7338
 7.211-8.8425-4.3367.0169-.6677 8.7918 4.3282
 11.1759-6.8644v-.4904L12.3592 3.9773.5917 11.2561v3.2547l11.142
 5.5119 11.6322-7.135.33.5074-11.9284 7.3038L0 14.8828v-3.9563L12.3254
 3.301z" />
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
