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


class PinoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pino"

    @property
    def original_file_name(self) -> "str":
        return "pino.svg"

    @property
    def title(self) -> "str":
        return "pino"

    @property
    def primary_color(self) -> "str":
        return "#687634"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>pino</title>
     <path d="m9.225 5.555 2.789 5.472 2.756-5.505L11.999 0M1.979
 20.123h13.769v-.037L8.862 6.29m3.524 5.522 4.131 8.311h5.505L15.137
 6.291M4.5 24h14.87l-1.554-3.188H6.056" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/pinojs/pino/blob/bb31ed775'''

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
