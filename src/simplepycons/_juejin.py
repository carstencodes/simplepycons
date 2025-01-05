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


class JuejinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "juejin"

    @property
    def original_file_name(self) -> "str":
        return "juejin.svg"

    @property
    def title(self) -> "str":
        return "Juejin"

    @property
    def primary_color(self) -> "str":
        return "#007FFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Juejin</title>
     <path d="m12 14.316 7.454-5.88-2.022-1.625L12
 11.1l-.004.003-5.432-4.288-2.02 1.624 7.452 5.88Zm0-7.247
 2.89-2.298L12 2.453l-.004-.005-2.884 2.318 2.884 2.3Zm0
 11.266-.005.002-9.975-7.87L0 12.088l.194.156 11.803 9.308
 7.463-5.885L24 12.085l-2.023-1.624Z" />
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
