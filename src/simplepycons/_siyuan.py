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


class SiyuanIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "siyuan"

    @property
    def original_file_name(self) -> "str":
        return "siyuan.svg"

    @property
    def title(self) -> "str":
        return "SiYuan"

    @property
    def primary_color(self) -> "str":
        return "#D23F31"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SiYuan</title>
     <path d="m0 8.455 6.818-6.819L12 6.818l5.182-5.182L24
 8.455v13.909l-6.818-6.819v-2.314l5.182 5.182v-9.28L17.182
 3.95v11.594L12 20.727l-5.182-5.182v-2.314L12 18.413v-9.28L6.818
 3.95v11.594L0 22.364Z" />
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
        yield from [
            "sy",
        ]
