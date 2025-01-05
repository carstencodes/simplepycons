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


class DepositphotosIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "depositphotos"

    @property
    def original_file_name(self) -> "str":
        return "depositphotos.svg"

    @property
    def title(self) -> "str":
        return "Depositphotos"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Depositphotos</title>
     <path d="M12 24c5.119 0 9.061-3.942 9.061-9.06S17.119 5.88 12
 5.88c-5.117 0-9.059 3.942-9.059 9.06S6.883 24 12 24Zm0-5.598c-1.954
 0-3.461-1.508-3.461-3.462 0-1.955 1.507-3.462 3.461-3.462 1.955 0
 3.462 1.507 3.462 3.462 0 1.954-1.507 3.462-3.462
 3.462Zm2.634-12.241h6.161V0h-6.161v6.161Z" />
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
