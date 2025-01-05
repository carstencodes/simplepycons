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


class TransportForIrelandIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "transportforireland"

    @property
    def original_file_name(self) -> "str":
        return "transportforireland.svg"

    @property
    def title(self) -> "str":
        return "Transport for Ireland"

    @property
    def primary_color(self) -> "str":
        return "#00B274"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Transport for Ireland</title>
     <path d="M0 0v12c0 6.62 5.38 12 12
 12h12V11.978h-.022c0-6.62-5.38-11.978-12-11.978zm3.376
 8.145h6.337v1.546h-2.33v6.12H5.706v-6.12h-2.33zm8.014
 0h5.837V9.67h-4.138v1.633h3.659v1.546h-3.659v2.962H11.39zm7.535
 0h1.678v7.666h-1.678Z" />
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
