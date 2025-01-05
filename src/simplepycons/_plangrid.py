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


class PlangridIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "plangrid"

    @property
    def original_file_name(self) -> "str":
        return "plangrid.svg"

    @property
    def title(self) -> "str":
        return "PlanGrid"

    @property
    def primary_color(self) -> "str":
        return "#0085DE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PlanGrid</title>
     <path d="M16.6 0c2.6 0 4.262.009 5.828 1.574C23.99 3.141 24 4.794
 24 7.401v9.2c0 2.6-.01 4.261-1.574 5.828C20.859 23.991 19.207 24
 16.598 24h-9.2c-2.599 0-4.26-.009-5.827-1.574C.01 20.861 0 19.207 0
 16.599v-9.2C0 4.8.01 3.138 1.574 1.572 3.141.01 4.793 0 7.4
 0h9.201-.001zm4.398 11.151C20.57 6.578 16.684 3.002 12 3.002c-4.971
 0-9 4.027-9 8.998 0 4.801 3.752 8.734 8.485 9h7.136c1.313-.003
 2.375-1.066 2.379-2.381v-7.47l-.002.002zm-2.285 8.589c-.564
 0-1.023-.46-1.023-1.024 0-.566.459-1.024 1.023-1.024.566 0 1.025.458
 1.025 1.024 0 .564-.459 1.024-1.025 1.024zM12 18.949C8.163 18.945
 5.055 15.836 5.051 12 5.055 8.164 8.163 5.055 12 5.051c3.836.004
 6.945 3.113 6.949 6.949-.004 3.836-3.113 6.945-6.949 6.949z" />
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
