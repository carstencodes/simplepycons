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


class ToshibaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "toshiba"

    @property
    def original_file_name(self) -> "str":
        return "toshiba.svg"

    @property
    def title(self) -> "str":
        return "Toshiba"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Toshiba</title>
     <path d="M5.174 10.172c-1.065 0-1.578.187-1.65 1.148a8.92 8.92 0
 00-.022.68c0 .218.004.451.021.68.073.96.586 1.148 1.65 1.148 1.065 0
 1.58-.188 1.653-1.148.018-.229.022-.462.022-.68
 0-.217-.005-.451-.022-.68-.073-.96-.588-1.148-1.652-1.148zm3.79
 0c-.41 0-.82.04-.985.121-.322.156-.545.38-.545 1.02 0
 .375.1.654.293.796.281.21.553.23 1.31.27.305.016.47.078.47.34 0
 .332-.294.332-.564.332-.28
 0-.366-.025-.46-.096-.084-.063-.105-.176-.106-.348h-.95c0
 .487.01.884.47 1.084.41.18 1.67.18
 2.048.014.328-.145.563-.337.563-.994
 0-.455-.091-.735-.44-.941-.248-.147-.945-.17-1.298-.192-.258-.016-.356-.11-.356-.338
 0-.297.285-.308.53-.308.202 0
 .34.018.439.105.038.039.086.099.088.307h.947c0-.408-.014-.848-.455-1.051-.175-.08-.587-.121-.998-.121zm2.206.062v3.532h.996v-1.362h1.156v1.362h.996v-3.532h-.996v1.29h-1.156v-1.29h-.996zm4.023
 0v3.532h1.002v-3.532h-1.002zm1.891 0v3.532h1.887c.869 0 1.162-.376
 1.162-.952 0-.401-.092-.755-.643-.894.444-.114.574-.379.574-.762
 0-.776-.487-.924-1.181-.924h-1.799zm4.373 0l-1.068
 3.532h1.037l.187-.655h1.16l.19.655H24l-1.07-3.532h-1.473zM0
 10.236v.881h1.055v2.65H2.11v-2.65h1.055v-.88H0zm5.174.762c.418 0
 .633.063.66.607.004.085.01.201.01.395 0
 .195-.006.31-.01.395-.027.544-.242.607-.66.607-.418
 0-.633-.063-.66-.607A7.674 7.674 0 014.506
 12c0-.194.003-.31.008-.395.027-.544.242-.607.66-.607zm12.906.045h.69c.18
 0 .293.085.293.291 0
 .176-.112.285-.293.285h-.69v-.576zm4.111.064h.006l.354
 1.22h-.713l.353-1.22zm-4.11 1.207h.689c.279 0
 .337.124.337.323s-.11.32-.337.32h-.69v-.643z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Toshi'''

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
