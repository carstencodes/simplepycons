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


class ManIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "man"

    @property
    def original_file_name(self) -> "str":
        return "man.svg"

    @property
    def title(self) -> "str":
        return "MAN"

    @property
    def primary_color(self) -> "str":
        return "#E40045"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MAN</title>
     <path d="M10.979 14.943h2.05L15.46
 18.7h-2.054l-.263-.409h-2.278l-.264.41H8.548zm1.025
 1.568l-.458.711h.916l-.458-.712zM0 17.372C0 10.704 5.372 5.3 12
 5.3s12 5.405 12 12.073c0 .449-.024.892-.072
 1.328H22.58c.054-.435.082-.878.082-1.328
 0-5.924-4.774-10.726-10.662-10.726-5.889 0-10.661 4.802-10.661 10.726
 0 .45.027.893.08 1.328H.073A12.254 12.274 0 0 1 0
 17.372zm2.237-2.43h1.83l1.22 1.228
 1.22-1.227h1.831V18.7H6.363v-1.38l-1.075
 1.082-1.076-1.082v1.38H2.237v-3.757zm13.42 0h1.927l2.17
 1.62v-1.62h1.975V18.7h-1.942l-2.156-1.605V18.7h-1.975Z" />
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
