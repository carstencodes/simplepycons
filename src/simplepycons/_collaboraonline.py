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


class CollaboraOnlineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "collaboraonline"

    @property
    def original_file_name(self) -> "str":
        return "collaboraonline.svg"

    @property
    def title(self) -> "str":
        return "Collabora Online"

    @property
    def primary_color(self) -> "str":
        return "#5C2983"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Collabora Online</title>
     <path d="M8.852 0 3.55 5.303 10.247 12 3.55 18.698 8.852
 24l12-12zM3.147 5.706v12.588L9.442 12z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.collaboraonline.com/branding-guid'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.collaboraonline.com/branding-guid'''

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
        yield from [
            "Collabora Office",
            "Collabora Productivity",
        ]
