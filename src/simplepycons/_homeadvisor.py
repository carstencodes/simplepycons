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


class HomeadvisorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "homeadvisor"

    @property
    def original_file_name(self) -> "str":
        return "homeadvisor.svg"

    @property
    def title(self) -> "str":
        return "HomeAdvisor"

    @property
    def primary_color(self) -> "str":
        return "#F68315"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HomeAdvisor</title>
     <path d="M15.98 2.442H8.02L0 10.46h2.275l6.882-6.88 6.881
 6.881H24l-8.02-8.018m-.492 9.348L9.157 5.459 4.01 10.605v4.987a1.33
 1.33 0 0 0 1.329 1.329h6.077l4.637 4.637v-4.637h2.598a1.33 1.33 0 0 0
 1.33-1.33V11.79h-4.494Z" />
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
