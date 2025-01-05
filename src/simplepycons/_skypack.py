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


class SkypackIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "skypack"

    @property
    def original_file_name(self) -> "str":
        return "skypack.svg"

    @property
    def title(self) -> "str":
        return "Skypack"

    @property
    def primary_color(self) -> "str":
        return "#3167FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Skypack</title>
     <path d="m19.82 11.27-5.997-2.994
 5.999-2.993c.28-.14.453-.42.453-.734a.815.815 0 0
 0-.454-.735L12.366.087a.814.814 0 0 0-.733 0L4.178 3.814a.815.815 0 0
 0-.453.735v7.454c0 .28.15.548.384.699l.07.034 5.998 2.994-5.999
 2.993a.815.815 0 0 0-.453.734c0 .314.174.594.453.735l7.455
 3.727a.814.814 0 0 0 .361.081.814.814 0 0 0
 .361-.081l7.454-3.727c.28-.14.455-.42.455-.735v-7.454a.785.785 0 0
 0-.443-.733zm-7.814-9.54 5.625 2.819-5.625 2.818L6.38 4.55zm-6.64
 4.135 4.811 2.41-4.81 2.412zm1.014 6.138 5.626-2.819 5.625 2.82-5.625
 2.818zm4.81 5.044v4.81l-4.81-2.41zm7.455 1.91-5.824
 2.911v-5.625l5.824-2.912v5.625z" />
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
