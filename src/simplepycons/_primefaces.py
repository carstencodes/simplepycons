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


class PrimefacesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "primefaces"

    @property
    def original_file_name(self) -> "str":
        return "primefaces.svg"

    @property
    def title(self) -> "str":
        return "PrimeFaces"

    @property
    def primary_color(self) -> "str":
        return "#263238"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PrimeFaces</title>
     <path d="M6.43 0 3.875 2.564l3.833.367L8.988 0Zm3.104 0L8.081
 3.465 1.5 2.931l1.094 4.58 7.853 2.931h1.095V0Zm2.74
 0v10.442h1.278l7.853-2.93 1.095-4.58-6.756.547L14.283 0Zm2.556 0 1.28
 2.931 3.834-.367L17.387 0ZM2.778 8.244v6.229l4.383
 3.663v-5.68l1.278-1.83-1.643.366-2.009-2.016zm18.261
 0-2.009.732-2.009 2.016-1.643-.367 1.278 1.832v5.68l4.383-3.664zM9.17
 10.625l-1.462 2.199v8.243l1.097 1.65L10.083 24h3.652l1.278-1.284
 1.096-1.649v-8.243l-1.46-2.199-.914.55h-3.652zm-4.383 6.23v2.38l2.374
 2.382V18.87zm14.243 0-2.374 2.015v2.747l2.374-2.381z" />
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
