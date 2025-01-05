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


class ThurgauerKantonalbankIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "thurgauerkantonalbank"

    @property
    def original_file_name(self) -> "str":
        return "thurgauerkantonalbank.svg"

    @property
    def title(self) -> "str":
        return "Thurgauer Kantonalbank"

    @property
    def primary_color(self) -> "str":
        return "#006D41"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Thurgauer Kantonalbank</title>
     <path d="M21.872 2.262H10.775l-6.14 9.743 6.14
 9.771h11.097l-6.135-9.77 6.135-9.744zM0 .297v23.406h24V.297H0zm23.057
 22.486L.943 22.778V1.228h22.109l.005 21.555z" />
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
