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


class ThunderstoreIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "thunderstore"

    @property
    def original_file_name(self) -> "str":
        return "thunderstore.svg"

    @property
    def title(self) -> "str":
        return "Thunderstore"

    @property
    def primary_color(self) -> "str":
        return "#23FFB0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Thunderstore</title>
     <path d="m.322 13.174 4.706 8.192L7.2 16.855 4.824 12.72a1.416
 1.416 0 0 1 0-1.444l2.965-5.16c.265-.46.718-.723
 1.245-.723h1.595l-3.086 6.953h3.812L6.171 22.403 16.583
 9.914h-3.201l2.184-4.52h6.052L24 1.25H7.175c-.86 0-1.598.428-2.028
 1.174l-4.825 8.4a2.306 2.306 0 0 0 0 2.35m7.213 9.576h9.29a2.29 2.29
 0 0 0 2.03-1.176l4.825-8.4a2.317 2.317 0 0 0
 0-2.35l-1.93-3.36h-4.763l2.19 3.813c.262.46.262.987 0 1.444l-2.964
 5.162a1.41 1.41 0 0 1-1.248.723h-2.154l-1.497-.017z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://github.com/thunderstore-io/brand-guid'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/thunderstore-io/brand-guid
elines/blob/7b5d4b62ca192a61b8ce5842cd8f5ad1f24ffcfd/assets/logo/thund'''

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
