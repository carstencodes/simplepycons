#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class PangolinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pangolin"

    @property
    def original_file_name(self) -> "str":
        return "pangolin.svg"

    @property
    def title(self) -> "str":
        return "Pangolin"

    @property
    def primary_color(self) -> "str":
        return "#F36118"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pangolin</title>
     <path d="M19.729 7.988a.852.852 0 1 1 0 1.705.85.85 0 0 1
 0-1.701m3.345 3.557c-.087 2.835-2.249 6.577-5.178 7.537-3.425
 1.123-6.022-.563-6.846-2.54-.642-1.542-.159-3.383 1.04-4.162
 1.013-.661 2.895-.831
 4.479.208-.556-1.459-2.053-2.419-3.38-2.706a5.67 5.67 0 0
 0-3.681.54c1.263-1.398 4.218-2.748 7.431-1.043 2.155 1.145 3.081
 2.748 3.996 4.914C23.33 10.63 21.66 6.219 18.75 3.6A14.44 14.44 0 0 0
 8.71.009c1.013.627 2.2 1.52 3.3 2.562-4.853-.6-8.856.503-11.328
 3.867a21.6 21.6 0 0 1 5.02-.355C2.164 8.578.107 12.766 1.154
 17.139a20.2 20.2 0 0 1 2.73-3.666c-.353 3.262.136 7.673 4.33
 10.527a19 19 0 0 1-.465-3.137c1.962 1.534 4.812 2.797 8.35 1.924
 6.245-1.543 7.915-7.58 6.974-11.242" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/fosrl/pangolin/blob/b4c013'''

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
