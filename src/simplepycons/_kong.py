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


class KongIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kong"

    @property
    def original_file_name(self) -> "str":
        return "kong.svg"

    @property
    def title(self) -> "str":
        return "Kong"

    @property
    def primary_color(self) -> "str":
        return "#003459"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kong</title>
     <path d="M7.88 18.96h4.405l2.286
 2.876-.393.979h-5.69l.139-.979-1.341-2.117.594-.759Zm3.152-12.632
 2.36-.004L24 18.97l-.824 3.845h-4.547l.283-1.083L9
 9.912l2.032-3.584Zm4.17-5.144 4.932 3.876-.632.651.855
 1.191v1.273l-2.458 2.004-4.135-4.884h-2.407l.969-1.777
 2.876-2.334ZM4.852 13.597l3.44-2.989 4.565 5.494-1.296
 2.012h-4.21l-2.912 3.822-.665.879H0v-4.689l3.517-4.529h1.335Z" />
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
