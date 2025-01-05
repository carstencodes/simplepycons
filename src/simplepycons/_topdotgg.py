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


class TopdotggIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "topdotgg"

    @property
    def original_file_name(self) -> "str":
        return "topdotgg.svg"

    @property
    def title(self) -> "str":
        return "Top.gg"

    @property
    def primary_color(self) -> "str":
        return "#FF3366"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Top.gg</title>
     <path d="M0 4.3785h7.6215V12H2.329A2.3212 2.3212 0 0 1 .0077
 9.6788Zm24 0H8.757v15.243h3.1144a4.5071 4.5071 0 0 0
 4.507-4.5071V12h3.1145A4.5073 4.5073 0 0 0 24 7.4929z" />
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
