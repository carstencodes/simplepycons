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


class HelpScoutIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "helpscout"

    @property
    def original_file_name(self) -> "str":
        return "helpscout.svg"

    @property
    def title(self) -> "str":
        return "Help Scout"

    @property
    def primary_color(self) -> "str":
        return "#1292EE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Help Scout</title>
     <path d="m3.497 14.044 7.022-7.021a4.946 4.946 0 0 0
 1.474-3.526A4.99 4.99 0 0 0 10.563 0L3.54 7.024a4.945 4.945 0 0
 0-1.473 3.525c0 1.373.55 2.6 1.43 3.496zm17.007-4.103-7.023
 7.022a4.946 4.946 0 0 0-1.473 3.525c0 1.36.55 2.601 1.43
 3.497l7.022-7.022a4.943 4.943 0 0 0
 1.474-3.526c0-1.373-.55-2.6-1.43-3.496zm-.044-2.904a4.944 4.944 0 0 0
 1.474-3.525c0-1.36-.55-2.6-1.43-3.497L3.54 16.965A4.986 4.986 0 0 0
 3.497 24Z" />
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
