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


class RepublicOfGamersIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "republicofgamers"

    @property
    def original_file_name(self) -> "str":
        return "republicofgamers.svg"

    @property
    def title(self) -> "str":
        return "Republic of Gamers"

    @property
    def primary_color(self) -> "str":
        return "#FF0029"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Republic of Gamers</title>
     <path d="M21.3906
 5.5833c-1.3467.0115-3.4338.19541-5.9375.97657-1.6024.49851-3.916
 2.74203-8.22459 6.90823-.56973.3204-2.67017-.8912-3.88085-1.461 0 0
 1.9929 3.1699 2.70507 4.0957 1.06825 1.46 3.02735 2.3145 3.02735
 2.3145-.17804-.1781-1.53019-1.6029-1.92188-2.4219-.24926-.3917.03418-.9624
 1.95703-2.3867C10.86 12.3268 17.0569 7.09358 23.0391 5.66924c0
 0-.601-.09488-1.6485-.08593V5.5833ZM24
 7.7708c-2.0653.21366-4.06.81878-5.9473 1.70899C14.2783 11.2602 7.9043
 15.8177 7.9043 15.8177c.28486.178.5706.3556.85546.498 3.06234 1.3531
 7.58484 2.1716 8.43944 1.8867 2.3858-.7833 5.056-5.8026 5.875-8.1172
 0 0-2.4933.9968-5.0215 2.1719-2.1009.9971-4.414 2.1368-4.414
 2.1368l5.875-1.7813s-1.5676 3.7036-3.6328
 4.1309c-2.0653.4273-5.6973-1.0332-5.6973-1.0332.2849-.2493
 4.1302-3.0629
 13.1035-6.73051.3917-.28487.6417-.74608.7129-1.20898V7.7708ZM0
 11.2942c.35608.9615.8194 1.8525 1.35352 2.7071.64094.819 3.27477
 1.4952 3.63086 1.5664C3.34638 14.4282 0 11.2942 0 11.2942Z" />
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
            "ASUS ROG",
            "ROG",
        ]
