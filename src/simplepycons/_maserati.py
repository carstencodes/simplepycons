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


class MaseratiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "maserati"

    @property
    def original_file_name(self) -> "str":
        return "maserati.svg"

    @property
    def title(self) -> "str":
        return "Maserati"

    @property
    def primary_color(self) -> "str":
        return "#0C2340"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Maserati</title>
     <path d="M9.678 21.213h4.67v.909h-4.67v-.909zm.87
 2.787h2.93v-1.409h-2.93V24zm-.844-5.313c.575.523.881 1.28.83
 2.056h2.944a2.575 2.575 0 0 1
 .818-2.056H9.704zm-3.052-2.17v.683h10.696v-.683H6.652zm.478
 3.087a3.833 3.833 0 0 0 1.74-.917H7.009l.121.917zm9.74
 0l.121-.917h-1.86c.49.451 1.089.768 1.739.917zm-8.666-4.556A73.645
 73.645 0 0 0 5.913 8.63c.644.102 1.283.237 1.913.405A18.885 18.885 0
 0 0 3.51 5.583c1.226 2.378 2.378 5.987 2.965 9.465h1.73zm9.326
 0c.587-3.478 1.74-7.087 2.961-9.465a18.877 18.877 0 0 0-4.308
 3.452c.63-.169 1.268-.304 1.913-.405a65.966 65.966 0 0 0-2.292
 6.418h1.726zM6.087
 16.17h11.83v-.679H6.087v.679zm5.135-1.144c.312-.74.569-1.5.77-2.278.203.777.462
 1.538.773
 2.278h2.052c-1.743-2.87-2.234-6.665-2.343-10-.009-.343.13-.43.46-.283l1.053.474A15.501
 15.501 0 0 1 11.991 0 15.494 15.494 0 0 1 10
 5.217l1.052-.474c.33-.152.457-.06.457.283-.109 3.313-.6 7.109-2.34
 10h2.053zm-5.135 3.191h11.83v-.678H6.087v.678z" />
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
