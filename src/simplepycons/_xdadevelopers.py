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


class XdaDevelopersIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "xdadevelopers"

    @property
    def original_file_name(self) -> "str":
        return "xdadevelopers.svg"

    @property
    def title(self) -> "str":
        return "XDA Developers"

    @property
    def primary_color(self) -> "str":
        return "#EA7100"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>XDA Developers</title>
     <path d="M13.84
 3.052V0h7.843v17.583H13.84v-3.024h4.591V3.052zM5.569
 14.53V3.024h4.592V0H2.318v17.583H6.98L10.16 24v-9.483z" />
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
