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


class CairoMetroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cairometro"

    @property
    def original_file_name(self) -> "str":
        return "cairometro.svg"

    @property
    def title(self) -> "str":
        return "Cairo Metro"

    @property
    def primary_color(self) -> "str":
        return "#C10C0C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cairo Metro</title>
     <path d="M12.397 4.14h.882v.881h-.882zm-1.628
 0h.883v.881h-.883zm4.915
 1.055v3.402h-1.386V5.195h-.84v1.763h-2.983V5.196h-.84v3.402H8.543v.84h1.911V7.82h2.983v1.617h5.44V5.195zm2.352
 3.395h-1.512V6.028h1.512zM5.173
 5.195v2.604h2.353v.805H5.173v.833h3.193V5.195zm2.339
 1.757H5.999v-.924h1.513zm-2.64 12.177V9.726h4.175L12
 12.68l2.954-2.953h4.176v9.403h-4.176v-3.442L12
 18.754l-2.952-3.048v3.424zM12 0L8.485 3.515h-4.97v4.97L0 12l3.515
 3.515v4.97h4.97L12 24l3.515-3.515h4.97v-4.97L24
 12l-3.515-3.515v-4.97h-4.97zm0 1.708l3.014 3.015h4.263v4.263L22.292
 12l-3.015 3.014v4.263h-4.263L12
 22.292l-3.014-3.015H4.723v-4.263L1.708 12l3.015-3.014V4.723h4.263Z"
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
        return '''https://en.wikipedia.org/wiki/File:Cairo_metr'''

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
