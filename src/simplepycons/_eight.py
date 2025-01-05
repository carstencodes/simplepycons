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


class EightIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "eight"

    @property
    def original_file_name(self) -> "str":
        return "eight.svg"

    @property
    def title(self) -> "str":
        return "Eight"

    @property
    def primary_color(self) -> "str":
        return "#0054FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Eight</title>
     <path d="M5.908 6.092a5.908 5.908 0 1 0 0 11.816 5.908 5.908 0 0
 0 0-11.816zm9.23 0v2.955h5.909V6.092h-5.908zm5.909
 2.955v5.906H24V9.047h-2.953zm0
 5.906h-5.908v2.955h5.908v-2.955zm-5.908
 0V9.047h-2.953v5.906h2.953zm-9.23-5.906A2.956 2.956 0 0 1 8.86
 12a2.956 2.956 0 0 1-2.953 2.953A2.958 2.958 0 0 1 2.953 12a2.958
 2.958 0 0 1 2.955-2.953z" />
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
