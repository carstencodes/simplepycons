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


class KeeneticIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "keenetic"

    @property
    def original_file_name(self) -> "str":
        return "keenetic.svg"

    @property
    def title(self) -> "str":
        return "Keenetic"

    @property
    def primary_color(self) -> "str":
        return "#009EE2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Keenetic</title>
     <path d="M15.718 10.188 24 2.376h-6.588L9.788
 9.812H4.33V2.376H0v19.248h4.33V14.14h7.623c3.2 0 5.412.706 6.588
 2.07.706.8 1.035 1.883 1.035
 3.248v2.165h4.33v-2.165c0-2.353-.706-4.424-2.07-6.024-1.46-1.647-3.483-2.776-6.118-3.247"
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
