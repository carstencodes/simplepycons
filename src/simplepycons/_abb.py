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


class AbbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "abb"

    @property
    def original_file_name(self) -> "str":
        return "abb.svg"

    @property
    def title(self) -> "str":
        return "ABB"

    @property
    def primary_color(self) -> "str":
        return "#FF000F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ABB</title>
     <path d="M13.086 16.594v-4.427h3.035c.25.418.362.947.362 1.476 0
 1.559-1.17 2.867-2.84
 2.951zm-.279-4.455v4.455h-2.784v-4.455zm3.147-.278h-2.868V7.406h.668c1.086
 0 1.949.863 1.949 1.949 0 .64-.334 1.225-.835 1.587.417.223.807.529
 1.086.919m-3.147-4.455v4.455h-2.784V7.406zm7.796
 9.188v-4.427h3.035c.251.418.362.947.362 1.476 0 1.559-1.169
 2.867-2.84
 2.951zm-.278-4.455v4.455h-2.784v-4.455zm3.146-.278h-2.868V7.406h.668c1.086
 0 1.949.863 1.949 1.949 0 .64-.334 1.225-.835 1.587.418.223.808.529
 1.086.919m-3.146-4.455v4.455h-2.784V7.406zM1.587
 12.139h2.868v2.506H2.979l-.668
 1.949H0zm2.868-4.733v4.455H1.671l1.587-4.455zm.278
 7.239v-2.506h2.868l1.587
 4.455H6.877l-.668-1.949zm2.784-2.784H4.733V7.406H5.93z" />
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
