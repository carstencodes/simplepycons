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


class TplinkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tplink"

    @property
    def original_file_name(self) -> "str":
        return "tplink.svg"

    @property
    def title(self) -> "str":
        return "TP-Link"

    @property
    def primary_color(self) -> "str":
        return "#4ACBD6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TP-Link</title>
     <path d="M15.185 0C10.218 0 6.25 3.984 6.25
 8.903V10.8h4.99V8.903c0-2.135 1.736-3.863 3.946-3.863 2.187 0 3.708
 1.536 3.708 3.815 0 2.257-1.64 3.912-3.827
 3.912h-1.878v5.039h1.878c4.874 0 8.819-4.007 8.819-8.952C23.885 3.72
 20.2 0 15.185 0zM.115 12.6v4.103c0 .624.523 1.248 1.236
 1.248h4.753v4.801c0 .624.523 1.248 1.236 1.248h4.065V12.6Z" />
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
