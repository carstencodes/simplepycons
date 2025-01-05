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


class HypothesisIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hypothesis"

    @property
    def original_file_name(self) -> "str":
        return "hypothesis.svg"

    @property
    def title(self) -> "str":
        return "Hypothesis"

    @property
    def primary_color(self) -> "str":
        return "#BD1C2B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hypothesis</title>
     <path d="M3.425 0c-.93 0-1.71.768-1.71 1.72v17.14c0 .94.78 1.71
 1.71 1.71h5.95l2.62 3.43 2.62-3.43h5.95c.93 0 1.72-.77
 1.72-1.71V1.72c0-.95-.79-1.72-1.72-1.72H3.425m1.71
 3.43h2.58v6s.86-1.71 2.56-1.71c1.72 0 3.46.85 3.46
 3.52v5.9h-2.58V12c0-1.39-.88-1.93-1.73-1.71-.86.21-1.71 1.12-1.71
 3v3.85h-2.58V3.43m12.86 10.29c.95 0 1.72.78 1.72 1.7a1.71 1.71 0
 01-1.72 1.71 1.71 1.71 0 01-1.71-1.71c0-.92.76-1.71 1.71-1.71z" />
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
