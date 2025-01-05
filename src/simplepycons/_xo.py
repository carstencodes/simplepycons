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


class XoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "xo"

    @property
    def original_file_name(self) -> "str":
        return "xo.svg"

    @property
    def title(self) -> "str":
        return "XO"

    @property
    def primary_color(self) -> "str":
        return "#5ED9C7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>XO</title>
     <path d="m1.629 5.698 4.275 5.367 4.274-5.367h1.613l-5.089 6.384
 4.958 6.219h-1.613L5.903 13.1l-4.142 5.201H.131l4.957-6.219L0
 5.698h1.629Zm16.48-.082C21.423 5.616 24 8.632 24 12c0 3.425-2.613
 6.331-5.883 6.383-3.301-.1-5.804-2.878-5.911-6.164L12.202 12c0-3.436
 2.637-6.384 5.907-6.384Zm0 1.268c-2.59 0-4.639 2.4-4.639 5.116.078
 2.736 1.983 4.996 4.444 5.111l.195.004c2.583 0 4.623-2.406
 4.623-5.115 0-2.752-2.086-5.116-4.623-5.116Zm.944 3.71c.507 0
 1.1.662.702 1.473-.297.605-1.373 1.192-1.609
 1.315l-.045.024s-1.32-.658-1.655-1.339c-.397-.811.196-1.473.703-1.473.56
 0 .952.535.952.535s.391-.535.952-.535Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/xojs/xo/tree/f9c7db99255d0'''

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
