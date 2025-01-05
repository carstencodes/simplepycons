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


class NounProjectIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nounproject"

    @property
    def original_file_name(self) -> "str":
        return "nounproject.svg"

    @property
    def title(self) -> "str":
        return "Noun Project"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Noun Project</title>
     <path d="M17.672 8.846H24v6.327h-6.328zM6.328 11.99a3.164 3.164 0
 0 1-3.164 3.163A3.164 3.164 0 0 1 0 11.991a3.164 3.164 0 0 1
 3.164-3.164 3.164 3.164 0 0 1 3.164 3.164m5.504 1.142l2.04 2.021
 1.142-1.16-2.022-2.003 2.022-2.003-1.142-1.142-2.04 2.003L9.81 8.846
 8.649 9.988l2.022 2.003-2.022 2.003 1.16 1.16Z" />
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
