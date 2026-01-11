#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class AnichartIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "anichart"

    @property
    def original_file_name(self) -> "str":
        return "anichart.svg"

    @property
    def title(self) -> "str":
        return "AniChart"

    @property
    def primary_color(self) -> "str":
        return "#41B1EA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AniChart</title>
     <path d="M17.293 2.951a9 9 0 0 0-5.162 1.62l1.572 4.483a4.68 4.68
 0 0 1 3.596-1.706c1.068 0 2.113.364 2.935 1.045.51.41.957.487
 1.468.07l1.837-1.438c.552-.44.622-.98.135-1.467a9.12 9.12 0 0
 0-6.38-2.607M6.3 3.127 0 21.05h4.89l1.068-3.1h5.33l1.04
 3.1h4.871L10.92 3.127Zm2.3 5.882 1.674 4.966h-3.2Zm12.386
 6.318c-.272-.014-.544.103-.845.327-.81.646-1.808.98-2.841.98q-.502
 0-.976-.102l1.58 4.508a9.13 9.13 0 0 0
 5.583-2.421c.517-.494.446-1.057-.058-1.497l-1.797-1.515c-.223-.18-.434-.27-.646-.28"
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
