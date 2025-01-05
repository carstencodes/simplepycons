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


class AtlassianIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "atlassian"

    @property
    def original_file_name(self) -> "str":
        return "atlassian.svg"

    @property
    def title(self) -> "str":
        return "Atlassian"

    @property
    def primary_color(self) -> "str":
        return "#0052CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Atlassian</title>
     <path d="M7.12 11.084a.683.683 0 00-1.16.126L.075 22.974a.703.703
 0 00.63 1.018h8.19a.678.678 0
 00.63-.39c1.767-3.65.696-9.203-2.406-12.52zM11.434.386a15.515 15.515
 0 00-.906 15.317l3.95 7.9a.703.703 0 00.628.388h8.19a.703.703 0
 00.63-1.017L12.63.38a.664.664 0 00-1.196.006z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://atlassian.design/resources/logo-libra'''

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
