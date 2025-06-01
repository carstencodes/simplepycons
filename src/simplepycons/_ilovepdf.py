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


class IlovepdfIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ilovepdf"

    @property
    def original_file_name(self) -> "str":
        return "ilovepdf.svg"

    @property
    def title(self) -> "str":
        return "iLovePDF"

    @property
    def primary_color(self) -> "str":
        return "#E5322D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>iLovePDF</title>
     <path d="M15.374 2.094c-1.347.65-2.356 1.744-3.094 2.985C11.095
 3.087 9.21 1.47 6.356 1.47 3.501 1.47 0 3.894 0 7.987c0 4.145 3.458
 6.109 5.171 7.218 1.831 1.185 4.955 3.339 7.11 7.325 2.154-3.986
 5.278-6.14 7.109-7.325 1.287-.834 3.56-2.151 4.61-4.514Zm-.104
 8.832V3.138l7.788 7.788H15.27z" />
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
