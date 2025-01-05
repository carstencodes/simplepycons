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


class AircallIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "aircall"

    @property
    def original_file_name(self) -> "str":
        return "aircall.svg"

    @property
    def title(self) -> "str":
        return "Aircall"

    @property
    def primary_color(self) -> "str":
        return "#00B388"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Aircall</title>
     <path d="M23.451 5.906a6.978 6.978 0 0 0-5.375-5.39C16.727.204
 14.508 0 12 0S7.273.204 5.924.516a6.978 6.978 0 0 0-5.375 5.39C.237
 7.26.034 9.485.034 12s.203 4.74.515 6.094a6.978 6.978 0 0 0 5.375
 5.39C7.273 23.796 9.492 24 12 24s4.727-.204 6.076-.516a6.978 6.978 0
 0 0 5.375-5.39c.311-1.354.515-3.578.515-6.094
 0-2.515-.203-4.74-.515-6.094zm-5.873
 12.396l-.003.001c-.428.152-1.165.283-2.102.377l-.147.014a.444.444 0 0
 1-.45-.271 1.816 1.816 0 0
 0-1.296-1.074c-.351-.081-.928-.134-1.58-.134s-1.229.053-1.58.134a1.817
 1.817 0 0 0-1.291 1.062.466.466 0 0 1-.471.281 8 8 0 0
 0-.129-.012c-.938-.094-1.676-.224-2.105-.377l-.003-.001a.76.76 0 0
 1-.492-.713c0-.032.003-.066.005-.098.073-.979.666-3.272
 1.552-5.89C8.5 8.609 9.559 6.187 10.037 5.714a1.029 1.029 0 0 1
 .404-.26l.004-.002c.314-.106.892-.178 1.554-.178.663 0 1.241.071
 1.554.178l.005.002a1.025 1.025 0 0 1 .405.26c.478.472 1.537 2.895
 2.549 5.887.886 2.617 1.479 4.91 1.552
 5.89.002.032.005.066.005.098a.76.76 0 0 1-.491.713z" />
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
