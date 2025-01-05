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


class NvidiaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nvidia"

    @property
    def original_file_name(self) -> "str":
        return "nvidia.svg"

    @property
    def title(self) -> "str":
        return "NVIDIA"

    @property
    def primary_color(self) -> "str":
        return "#76B900"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NVIDIA</title>
     <path d="M8.948 8.798v-1.43a6.7 6.7 0 0 1 .424-.018c3.922-.124
 6.493 3.374 6.493 3.374s-2.774 3.851-5.75 3.851c-.398
 0-.787-.062-1.158-.185v-4.346c1.528.185 1.837.857 2.747
 2.385l2.04-1.714s-1.492-1.952-4-1.952a6.016 6.016 0 0
 0-.796.035m0-4.735v2.138l.424-.027c5.45-.185 9.01 4.47 9.01
 4.47s-4.08 4.964-8.33 4.964c-.37
 0-.733-.035-1.095-.097v1.325c.3.035.61.062.91.062 3.957 0 6.82-2.023
 9.593-4.408.459.371 2.34 1.263 2.73 1.652-2.633 2.208-8.772
 3.984-12.253 3.984-.335 0-.653-.018-.971-.053v1.864H24V4.063zm0
 10.326v1.131c-3.657-.654-4.673-4.46-4.673-4.46s1.758-1.944
 4.673-2.262v1.237H8.94c-1.528-.186-2.73 1.245-2.73 1.245s.68 2.412
 2.739 3.11M2.456 10.9s2.164-3.197 6.5-3.533V6.201C4.153 6.59 0 10.653
 0 10.653s2.35 6.802 8.948
 7.42v-1.237c-4.84-.6-6.492-5.936-6.492-5.936z" />
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
