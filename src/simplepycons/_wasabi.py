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


class WasabiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wasabi"

    @property
    def original_file_name(self) -> "str":
        return "wasabi.svg"

    @property
    def title(self) -> "str":
        return "Wasabi"

    @property
    def primary_color(self) -> "str":
        return "#01CD3E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wasabi</title>
     <path d="M20.483 3.517A11.91 11.91 0 0 0 12 0a11.91 11.91 0 0
 0-8.483 3.517A11.91 11.91 0 0 0 0 12a11.91 11.91 0 0 0 3.517
 8.483A11.91 11.91 0 0 0 12 24a11.91 11.91 0 0 0 8.483-3.517A11.91
 11.91 0 0 0 24 12a11.91 11.91 0 0 0-3.517-8.483Zm1.29
 7.387-5.16-4.683-5.285 4.984-2.774 2.615V9.932l4.206-3.994
 3.146-2.969c3.163 1.379 5.478 4.365 5.867 7.935zm-.088 2.828a10.632
 10.632 0 0 1-1.025 2.951l-2.952-2.668v-3.87Zm-8.183-11.47-2.227
 2.103-2.739 2.598v-4.17A9.798 9.798 0 0 1 12 2.155c.513 0 1.007.035
 1.502.106zM6.398 13.891l-4.083-3.658a9.744 9.744 0 0 1
 1.078-2.987L6.398 9.95zm0-9.968v3.129l-1.75-1.573a8.623 8.623 0 0 1
 1.75-1.556Zm-4.189 9.102 5.284 4.736 5.302-4.983
 2.74-2.598v3.817l-7.423 7.016a9.823 9.823 0 0 1-5.903-7.988Zm8.306
 8.695 5.02-4.754v4.206a9.833 9.833 0 0 1-3.553.654c-.495
 0-.99-.035-1.467-.106zm7.176-1.714v-3.11l1.714 1.555a9.604 9.604 0 0
 1-1.714 1.555z" />
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
