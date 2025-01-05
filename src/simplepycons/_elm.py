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


class ElmIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "elm"

    @property
    def original_file_name(self) -> "str":
        return "elm.svg"

    @property
    def title(self) -> "str":
        return "Elm"

    @property
    def primary_color(self) -> "str":
        return "#1293D8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Elm</title>
     <path d="M23.986 12.806V23.2l-5.197-5.197zM6.796
 6.01H17.19l-5.197 5.197zm9.275-1.12H5.677L.8.015h10.394zm7.116
 7.117L17.99 6.81l-5.197 5.197 5.197 5.197zm.813-.813L12.806 0H24zM0
 23.2V.813l11.194 11.194zm23.187.8H.8l11.193-11.194Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/elm/foundation.elm-lang.or'''

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
