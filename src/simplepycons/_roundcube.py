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


class RoundcubeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "roundcube"

    @property
    def original_file_name(self) -> "str":
        return "roundcube.svg"

    @property
    def title(self) -> "str":
        return "Roundcube"

    @property
    def primary_color(self) -> "str":
        return "#37BEFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Roundcube</title>
     <path d="M12.002.072a8.302 8.302 0 0 0-8.266 7.512L.498
 9.454l4.682 2.704A7.8 7.8 0 0 1 12.002.572a7.802 7.802 0 0 1 6.824
 11.582l4.676-2.7-3.236-1.87A8.302 8.302 0 0 0 12.002.072zM0
 9.742v7.399l11.75 6.787v-7.399L0 9.742zm24 0l-5.777 3.338-5.248
 3.031h-.002l-.108.063-.615.355v7.399L24 17.14V9.744z" />
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
