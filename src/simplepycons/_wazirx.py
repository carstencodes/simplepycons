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


class WazirxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wazirx"

    @property
    def original_file_name(self) -> "str":
        return "wazirx.svg"

    @property
    def title(self) -> "str":
        return "WazirX"

    @property
    def primary_color(self) -> "str":
        return "#3067F0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WazirX</title>
     <path d="M.965
 21.964h21.924v-2.485H.965v2.485Zm6.752-3.81h15.195L24 6.343 7.717
 18.155Zm9.384-8.704L5.205 18.072H1.93l6.045-9.814 3.858-6.22 5.269
 7.412Zm-11.693.223L0 6.067l.994 10.762 4.414-7.156Z" />
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
