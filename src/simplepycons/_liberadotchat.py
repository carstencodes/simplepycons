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


class LiberadotchatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "liberadotchat"

    @property
    def original_file_name(self) -> "str":
        return "liberadotchat.svg"

    @property
    def title(self) -> "str":
        return "Libera.Chat"

    @property
    def primary_color(self) -> "str":
        return "#FF55DD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Libera.Chat</title>
     <path d="m14.26446 2.76095-1.22973 9.43224-1.6484 1.88226L9.67694
 2.7735h-.003a9.86072 9.86072 0 0 0-.19917.04247l-.067.01256a12.0901
 12.0901 0 0 0-.13158.0305l-.0646.01555a12.0503 12.0503 0 0
 0-1.7393.55086l-.03709.01855 3.39788
 11.26306-.1579.18062-1.59816-.70397-.10465.13457L3.4452
 6.09902a10.69674 10.69674 0 0 0-.92767 1.0473 12.5862 12.5862 0 0
 0-.55146.7596v.00598l6.48115 7.08106-1.02158
 1.31285-7.20486-4.1497a11.70731 11.70731 0 0 0-.2207 2.30931l6.85377
 2.57547L5.2778 19.0661l-4.31.02034a12.18198 12.18198 0 0 0 1.21297
 2.15261h.003l1.69625-.37322h.45038l4.86266-6.22276 1.5832.70098
 3.33807-3.81237c1.84965 3.14502 3.84345 6.17068 5.65635
 9.33714h.45337l-.0083-.01376 1.61251.36246.01556-.01794a11.03054
 11.03054 0 0 0 .77455-1.25604 11.3919 11.3919 0 0 0
 .35228-.72551l-3.78784-.064-1.3332-2.19567
 6.1468-2.24172v-.0311a6.93926 6.93926 0 0 0
 .0036-.20217v-.31223l-.0036-.06398v-.0676l-.003-.06757-.003-.067-.003-.06757-.003-.067-.0059-.0646-.003-.06757-.0066-.067-.003-.06757-.006-.064-.006-.06757-.006-.06758-.0066-.067-.006-.06458a9.69536
 9.69536 0 0 0-.11304-.7961v-.01555l-6.50625 3.71908-1.0467-1.72436
 5.7365-6.49311a10.80699 10.80699 0 0 0-.8876-1.16997 11.89718
 11.89718 0 0 0-.69202-.7285l-4.72569 7.45488-1.37147-2.25848
 2.1526-7.75393-.05502-.02093a11.6277 11.6277 0 0 0-2.00607-.59453
 12.20035 12.20035 0 0 0-.13158-.0275zm-.1591 9.33116-3.24596
 3.72086-1.5832-.65853-4.48346 5.7078h.49584l4.10365-5.25144
 1.57423.65195 3.08387-3.53664 4.8507 8.15167.47729-.009zm-.07357
 1.30149-2.91221 3.34405-1.60474-.65254-3.74538 4.77413
 12.63513.0066z" />
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
