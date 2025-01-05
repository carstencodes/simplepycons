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


class QuicklookIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "quicklook"

    @property
    def original_file_name(self) -> "str":
        return "quicklook.svg"

    @property
    def title(self) -> "str":
        return "QuickLook"

    @property
    def primary_color(self) -> "str":
        return "#0078D3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>QuickLook</title>
     <path d="m22.682 19.189-.002-.002-3.07-3.068a7.027 7.027 0 0 0
 1.332-4.12 7.068 7.068 0 0 0-7.068-7.067V1.037A1.04 1.04 0 0 0
 12.653.016L1.67 1.965a.832.832 0 0 0-.687.818v18.434c0
 .403.29.748.687.818l10.982 1.949a1.04 1.04 0 0 0
 1.22-1.022v-3.894a7.027 7.027 0 0 0 4.12-1.332l3.069 3.07c.446.446
 1.17.447 1.617 0h.001c.447-.447.448-1.17.002-1.617zm-8.808-.62a6.576
 6.576 0 0 1-6.569-6.57 6.576 6.576 0 0 1 6.569-6.567A6.576 6.576 0 0
 1 20.442 12a6.576 6.576 0 0 1-6.568 6.568zm5.28-6.57a5.287 5.287 0 0
 1-5.28 5.282c-2.913 0-5.282-2.369-5.282-5.28s2.37-5.282
 5.282-5.282a5.287 5.287 0 0 1 5.28 5.28z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/QL-Win/QuickLook/blob/f726'''

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
