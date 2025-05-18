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


class NetimIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "netim"

    @property
    def original_file_name(self) -> "str":
        return "netim.svg"

    @property
    def title(self) -> "str":
        return "Netim"

    @property
    def primary_color(self) -> "str":
        return "#FE8427"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Netim</title>
     <path d="M23.305
 11.95c-1.014-1.134-2.772-1.242-3.927-.248l-.67.577a2.48 2.48 0 0 1
 1.274 2.309 2.493 2.493 0 0 1-2.403 2.35 2.488 2.488 0 0
 1-2.564-2.484c.067-1.745 1.41-2.484
 2.517-2.484l-2.745-6.504c-.59-1.396-2.215-2.054-3.631-1.477-.296.128-1.101.463-1.55
 1.484l-2.149 4.994L5.35 5.486C4.765 4.09 3.134 3.432 1.718 4.009.295
 4.586-.376 6.184.214 7.574l4.632 10.96c.59 1.397 2.215 2.055 3.631
 1.477.437-.194 1.108-.53 1.55-1.483l2.149-4.994 2.108 4.987a2.756
 2.756 0 0 0 1.644 1.53 2.83 2.83 0 0 0 2.806-.51l4.33-3.738a2.7 2.7 0
 0 0 .241-3.853z" />
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
