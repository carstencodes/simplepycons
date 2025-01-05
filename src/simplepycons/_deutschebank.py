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


class DeutscheBankIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "deutschebank"

    @property
    def original_file_name(self) -> "str":
        return "deutschebank.svg"

    @property
    def title(self) -> "str":
        return "Deutsche Bank"

    @property
    def primary_color(self) -> "str":
        return "#0018A8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Deutsche Bank</title>
     <path d="M3.375 3.375v17.25h17.25V3.375H3.375zM0
 0h24v24H0V0zm5.25 18.225 9.15-12.45h4.35L9.6 18.225H5.25z" />
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
