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


class VueuseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vueuse"

    @property
    def original_file_name(self) -> "str":
        return "vueuse.svg"

    @property
    def title(self) -> "str":
        return "VueUse"

    @property
    def primary_color(self) -> "str":
        return "#41B883"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>VueUse</title>
     <path d="M.876.001v12.873C.876 19.018 5.856 24 12 24s11.124-4.982
 11.124-11.126V0h-9.218v12.874c0 2.543-3.812 2.543-3.812 0V0Zm4.609
 1.001h3.608v11.872C9.089 14.555 10.354 15.79 12 15.79s2.911-1.236
 2.907-2.916V1.002h3.608v11.872a6.515 6.515 0 0 1-13.03 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/vueuse/vueuse/blob/b2aa062'''

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
