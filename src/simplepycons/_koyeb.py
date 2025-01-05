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


class KoyebIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "koyeb"

    @property
    def original_file_name(self) -> "str":
        return "koyeb.svg"

    @property
    def title(self) -> "str":
        return "Koyeb"

    @property
    def primary_color(self) -> "str":
        return "#121212"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Koyeb</title>
     <path d="M0 12.822V7.044L11.985.115 24 7.037v5.77L11.992
 5.892Zm11.985 1.114L1.92 19.759 0 18.645v-3.557l11.985-6.93L24
 15.089v3.542l-1.92 1.13Zm-3.028 9.949L3.95 21.004l8.036-4.656 8.066
 4.656-5.009 2.88-3.05-1.759Z" />
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
