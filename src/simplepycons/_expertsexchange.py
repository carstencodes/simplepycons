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


class ExpertsExchangeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "expertsexchange"

    @property
    def original_file_name(self) -> "str":
        return "expertsexchange.svg"

    @property
    def title(self) -> "str":
        return "Experts Exchange"

    @property
    def primary_color(self) -> "str":
        return "#00AAE7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Experts Exchange</title>
     <path d="M7.28.9H0L8.36 12 0 23.1h7.28L15.64 12zM24 .9h-7.28l-2.3
 3.06 3.64 4.82zM14.42 20.05l2.3 3.05H24l-5.94-7.88z" />
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
