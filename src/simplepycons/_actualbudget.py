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


class ActualBudgetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "actualbudget"

    @property
    def original_file_name(self) -> "str":
        return "actualbudget.svg"

    @property
    def title(self) -> "str":
        return "Actual Budget"

    @property
    def primary_color(self) -> "str":
        return "#6B46C1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Actual Budget</title>
     <path d="m17.442 10.779.737 2.01-16.758 6.145a.253.253 0 0
 1-.324-.15l-.563-1.536a.253.253 0 0 1 .15-.324zM1.13 23.309
 12.036.145A.253.253 0 0 1 12.265 0h.478c.097 0 .185.055.227.142l7.036
 14.455 2.206-.848c.13-.05.277.015.327.145l.587 1.526a.253.253 0 0
 1-.145.327l-2.034.783 2.51 5.156a.253.253 0 0
 1-.117.338l-1.47.716a.253.253 0 0 1-.339-.117l-2.59-5.322-17.37
 6.682a.253.253 0 0 1-.328-.145c0-.001
 0-.003-.002-.004l-.12-.33a.252.252 0 0 1 .009-.195zM12.528 4.127
 4.854 20.425 18 15.369z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/actualbudget/actual/blob/8
4af8b76be6bb6c866c32a5be6e8c7a092ab9e38/packages/desktop-client/src/ic'''

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
