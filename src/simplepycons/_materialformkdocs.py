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


class MaterialForMkdocsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "materialformkdocs"

    @property
    def original_file_name(self) -> "str":
        return "materialformkdocs.svg"

    @property
    def title(self) -> "str":
        return "Material for MkDocs"

    @property
    def primary_color(self) -> "str":
        return "#526CFE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Material for MkDocs</title>
     <path d="m17.029 18.772.777 1.166-5.417 2.709L0
 16.451V4.063l5.417-2.709 5.298 7.948 7.867-5.24L24 1.354V16.84l-5.417
 2.709zm2.023-13.827v13.253l3.949-1.975V2.97zM5.076 2.642 1.458 4.45
 12.73 21.358l3.618-1.809z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/squidfunk/mkdocs-material/
blob/9ff75d11838cc01615697884c0eb9eb55f4652ad/src/templates/.icons/log'''

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
