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


class OpenmediavaultIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openmediavault"

    @property
    def original_file_name(self) -> "str":
        return "openmediavault.svg"

    @property
    def title(self) -> "str":
        return "openmediavault"

    @property
    def primary_color(self) -> "str":
        return "#5DACDF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>openmediavault</title>
     <path d="M.945 1.045A.947.947 0 0 0 0 1.988v20.024c0
 .534.436.943.945.943h22.11a.944.944 0 0 0 .945-.943V1.988a.941.941 0
 0 0-.945-.943Zm.118 1.064h21.875v19.784H1.063ZM3.53 4.385c-.198
 0-.361.149-.361.334v3.699c0 .185.162.334.361.334h16.94c.198 0
 .36-.15.36-.334v-3.7c0-.184-.161-.333-.36-.333zm2.057.886a1.3 1.3 0 0
 1 1.297 1.297 1.3 1.3 0 0 1-1.297 1.3 1.3 1.3 0 0 1-1.299-1.3 1.3 1.3
 0 0 1 1.299-1.297m-.002.62a.68.68 0 0 0-.676.677.68.68 0 0 0
 .678.678.68.68 0 0 0 .678-.678.68.68 0 0 0-.678-.677ZM3.53
 9.816c-.198 0-.361.15-.361.334v3.702c0
 .184.162.332.361.332h16.94c.198 0
 .36-.15.36-.334v-3.7c0-.184-.161-.334-.36-.334zm2.057.887A1.3 1.3 0 0
 1 6.885 12a1.3 1.3 0 0 1-1.297 1.299A1.3 1.3 0 0 1 4.289 12a1.3 1.3 0
 0 1 1.299-1.297m-.002.62A.68.68 0 0 0 4.91 12a.68.68 0 0 0
 .678.68.68.68 0 0 0 0-1.358ZM3.53 15.247c-.198
 0-.361.15-.361.334v3.701c0 .185.162.332.361.332h16.94c.198 0
 .36-.15.36-.334v-3.699c0-.184-.161-.334-.36-.334zm2.057.887a1.3 1.3 0
 0 1 1.297 1.297 1.3 1.3 0 0 1-1.297 1.298 1.3 1.3 0 0 1-1.299-1.298
 1.3 1.3 0 0 1 1.299-1.297m-.002.619a.68.68 0 0 0 .002 1.358.68.68 0 0
 0 0-1.358Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/openmediavault/openmediava
ult/blob/12f8ef70f19f967733b744d6fb6156a4181f1ddc/deb/openmediavault/w'''

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
