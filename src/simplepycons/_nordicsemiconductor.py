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


class NordicSemiconductorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nordicsemiconductor"

    @property
    def original_file_name(self) -> "str":
        return "nordicsemiconductor.svg"

    @property
    def title(self) -> "str":
        return "Nordic Semiconductor"

    @property
    def primary_color(self) -> "str":
        return "#00A9CE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nordic Semiconductor</title>
     <path d="m11.3384 12.4477 12.0796 6.9917-2.8939 1.73-1.92
 1.0924c-.2979.1987-.5627.298-.8938.1656h-.033c-.0331 0-.0663
 0-.0994-.0331L6.1572 15.8067v6.72c-.2453
 0-.3825-.0384-.5627-.1324L.5627 19.448C.2317 19.2495 0 18.8853 0
 18.488V5.8713l10.7656 6.2395.5728.3369zm5.7544-10.7733-4.4662 2.5522
 4.4662 2.5965V1.6744zm6.0465
 2.546-4.4359-2.5489c-.2648-.1324-.5627-.1986-.8606-.1986v6.6538l-9.9642-5.793-1.1255-.629c-.4966-.2649-.9269-.298-1.4234-.0663L3.3765
 2.7971.8607 4.2536c-.331.1986-.5628.4634-.7283.8276l.2437.1412 3.2623
 1.8908 7.4234 4.3024-.6586-.3817.7385.428.577.3392 5.0774 2.939
 6.9976
 4.0502.107.062c.0662-.2318.0993-.6536.0993-.6536V5.7101c0-.629-.331-1.1917-.8607-1.4896zM6.9073
 22.2528l4.4525-2.5792-4.4526-2.5683v5.1475z" />
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
