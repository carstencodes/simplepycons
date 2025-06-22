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


class PlotlyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "plotly"

    @property
    def original_file_name(self) -> "str":
        return "plotly.svg"

    @property
    def title(self) -> "str":
        return "Plotly"

    @property
    def primary_color(self) -> "str":
        return "#7A76FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Plotly</title>
     <path d="M1.713.002A1.713 1.713 0 0 0 0 1.715a1.713 1.713 0 0 0
 1.713 1.713 1.713 1.713 0 0 0 1.714-1.713A1.713 1.713 0 0 0
 1.713.002Zm6.861 0a1.713 1.713 0 0 0-1.713 1.713 1.713 1.713 0 0 0
 1.713 1.713 1.713 1.713 0 0 0 1.713-1.713A1.713 1.713 0 0 0
 8.574.002Zm6.857 0a1.713 1.713 0 0 0-1.714 1.713 1.713 1.713 0 0 0
 1.714 1.713 1.713 1.713 0 0 0 1.713-1.713A1.713 1.713 0 0 0
 15.431.002zm6.856 0a1.713 1.713 0 0 0-1.713 1.713 1.713 1.713 0 0 0
 1.713 1.713A1.713 1.713 0 0 0 24 1.715 1.713 1.713 0 0 0
 22.287.002ZM1.713 6.859A1.713 1.713 0 0 0 0 8.572a1.713 1.713 0 0 0
 1.713 1.713 1.713 1.713 0 0 0 1.714-1.713A1.713 1.713 0 0 0 1.713
 6.86Zm6.861 0c-.948 0-1.713.765-1.713 1.713v13.713c0 .947.765 1.713
 1.713 1.713.948 0 1.713-.766
 1.713-1.713V8.572c0-.948-.765-1.713-1.713-1.713zm6.857 0a1.713 1.713
 0 0 0-1.714 1.713 1.713 1.713 0 0 0 1.714 1.713 1.713 1.713 0 0 0
 1.713-1.713 1.713 1.713 0 0 0-1.713-1.713zm6.856 0c-.947
 0-1.713.765-1.713 1.713v13.713c0 .947.766 1.713 1.713 1.713.948 0
 1.713-.766 1.713-1.713V8.572c0-.948-.765-1.713-1.713-1.713zM1.713
 13.715C.766 13.715 0 14.48 0 15.428v6.857c0 .947.766 1.713 1.713
 1.713.948 0 1.714-.766
 1.714-1.713v-6.857c0-.948-.766-1.713-1.714-1.713zm13.718 0c-.948
 0-1.714.765-1.714 1.713v6.857c0 .947.766 1.713 1.714 1.713.947 0
 1.713-.766 1.713-1.713v-6.857c0-.948-.766-1.713-1.713-1.713z" />
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
