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


class InvidiousIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "invidious"

    @property
    def original_file_name(self) -> "str":
        return "invidious.svg"

    @property
    def title(self) -> "str":
        return "Invidious"

    @property
    def primary_color(self) -> "str":
        return "#00B6F0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Invidious</title>
     <path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0zm0 .742A11.257 11.257 0 0 1 23.258 12 11.257
 11.257 0 0 1 12 23.258 11.257 11.257 0 0 1 .742 12 11.257 11.257 0 0
 1 12 .742zm-.66 4.375a.776.776 0 0 0-.777.778.776.776 0 0 0
 .777.775.776.776 0 0 0 .775-.775.776.776 0 0 0-.775-.778zm.035
 2.266-.523 1.853-2.75 9.291h-.713v.373h1.974v-.373h-.875l2.606-8.806
 4.6 9.174h1.429L11.375 7.383z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/iv-org/invidious-redirect/
blob/d5e4d97f4f998b8c2512c51ed9961a8d989a7ce0/src/assets/img/invidious'''

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
