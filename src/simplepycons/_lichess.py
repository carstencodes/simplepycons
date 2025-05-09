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


class LichessIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lichess"

    @property
    def original_file_name(self) -> "str":
        return "lichess.svg"

    @property
    def title(self) -> "str":
        return "Lichess"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lichess</title>
     <path d="M10.457 6.161a.237.237 0 0 0-.296.165c-.8 2.785 2.819
 5.579 5.214 7.428.653.504 1.216.939 1.591 1.292 1.745 1.642 2.564
 2.851 2.733 3.178a.24.24 0 0 0 .275.122c.047-.013 4.726-1.3
 3.934-4.574a.257.257 0 0 0-.023-.06L18.204 3.407 18.93.295a.24.24 0 0
 0-.262-.293c-1.7.201-3.115.435-4.5 1.425-4.844-.323-8.718.9-11.213
 3.539C.334 7.737-.246 11.515.085 14.128c.763 5.655 5.191 8.631 9.081
 9.532.993.229 1.974.34 2.923.34 3.344 0 6.297-1.381 7.946-3.85a.24.24
 0 0 0-.372-.3c-3.411 3.527-9.002 4.134-13.296
 1.444-4.485-2.81-6.202-8.41-3.91-12.749C4.741 4.221 8.801 2.362
 13.888 3.31c.056.01.115 0 .165-.029l.335-.197c.926-.546 1.961-1.157
 2.873-1.279l-.694 1.993a.243.243 0 0 0 .02.202l6.082 10.192c-.193
 2.028-1.706 2.506-2.226
 2.611-.287-.645-.814-1.364-2.306-2.803-.422-.407-1.21-.941-2.124-1.56-2.364-1.601-5.937-4.02-5.391-5.984a.239.239
 0 0 0-.165-.295z" />
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
