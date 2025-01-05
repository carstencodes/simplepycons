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


class VfairsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vfairs"

    @property
    def original_file_name(self) -> "str":
        return "vfairs.svg"

    @property
    def title(self) -> "str":
        return "vFairs"

    @property
    def primary_color(self) -> "str":
        return "#EF4678"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>vFairs</title>
     <path d="M22.316 5.923c-.01-.014-.027-.024-.04-.035a.412.412 0 0
 0-.06-.047L12.223.061a.427.427 0 0 0-.08-.033C12.128.02 12.113.02
 12.1.015a.41.41 0 0 0-.325.046l-9.992 5.78a.418.418 0 0
 0-.143.141c-.015.014-.02.034-.028.05a.423.423 0 0
 0-.048.191v11.56a.418.418 0 0 0 .007.05c.007.14.088.266.212.331l9.992
 5.78a.555.555 0 0 0 .487 0l9.888-5.756a.437.437 0 0 0
 .284-.406V6.223a.408.408 0 0 0-.119-.3zM2.45 17.015V6.99l8.665
 5.012-8.665
 5.012zm10.452-5.023l8.648-5.001v10.024c-2.905-1.676-5.634-3.268-8.648-5.023zm-.46-.757V1.211l8.666
 5.012zm-.885 0L2.891 6.223l8.666-5.012zm0
 1.535v10.024l-8.665-5.012zm.925.023l5.477 3.168 3.129 1.821-8.606
 5.01Z" />
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
