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


class MastercomfigIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mastercomfig"

    @property
    def original_file_name(self) -> "str":
        return "mastercomfig.svg"

    @property
    def title(self) -> "str":
        return "mastercomfig"

    @property
    def primary_color(self) -> "str":
        return "#009688"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>mastercomfig</title>
     <path d="M12 0C5.479 0 .174 5.304.174
 11.826V24h1.337v-6.716C3.486 21.064 7.446 23.65 12 23.65c4.554 0
 8.514-2.586 10.49-6.367V24h1.336V11.826h-1.337c0 5.798-4.69
 10.489-10.489 10.489-5.798 0-10.49-4.691-10.49-10.49C1.51 6.028 6.203
 1.338 12 1.338zm0 3.72a8.107 8.107 0 100 16.214 8.107 8.107 0
 000-16.215zm0 1.336a6.77 6.77 0 110 13.538 6.77 6.77 0 010-13.538z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/mastercomfig/mastercomfig.
github.io/blob/d910ce7e868a6ef32106e36996c3473d78da2ce3/img/mastercomf'''

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
