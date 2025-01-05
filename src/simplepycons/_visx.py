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


class VisxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "visx"

    @property
    def original_file_name(self) -> "str":
        return "visx.svg"

    @property
    def title(self) -> "str":
        return "visx"

    @property
    def primary_color(self) -> "str":
        return "#FF1231"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>visx</title>
     <path d="M.00195 0 12 11.51953 23.99805 0h-5.8711L12 6.08984
 5.87305 0Zm23.9961 0L12.47852 11.99805l11.51953
 11.99804V18.125l-6.08985-6.12695
 6.08985-6.12696ZM.00195.0039V5.875l6.08985 6.12695-6.08985
 6.12696V24l11.5039-11.99805Zm0 23.9961h5.8711L12 17.91016 18.12695
 24h5.8711L12 12.4707Z" />
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
