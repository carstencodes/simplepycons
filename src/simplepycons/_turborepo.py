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


class TurborepoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "turborepo"

    @property
    def original_file_name(self) -> "str":
        return "turborepo.svg"

    @property
    def title(self) -> "str":
        return "Turborepo"

    @property
    def primary_color(self) -> "str":
        return "#FF1E56"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Turborepo</title>
     <path d="M11.9906 4.1957c-4.2998 0-7.7981 3.501-7.7981
 7.8043s3.4983 7.8043 7.7981 7.8043c4.2999 0 7.7982-3.501
 7.7982-7.8043s-3.4983-7.8043-7.7982-7.8043m0 11.843c-2.229
 0-4.0356-1.8079-4.0356-4.0387s1.8065-4.0387 4.0356-4.0387S16.0262
 9.7692 16.0262 12s-1.8065 4.0388-4.0356
 4.0388m.6534-13.1249V0C18.9726.3386 24 5.5822 24 12s-5.0274
 11.66-11.356 12v-2.9139c4.7167-.3372 8.4516-4.2814
 8.4516-9.0861s-3.735-8.749-8.4516-9.0861M5.113
 17.9586c-1.2502-1.4446-2.0562-3.2845-2.2-5.3046H0c.151 2.8266 1.2808
 5.3917 3.051 7.3668l2.0606-2.0622zM11.3372
 24v-2.9139c-2.02-.1439-3.8584-.949-5.3019-2.2018l-2.0606 2.0623c1.975
 1.773 4.538 2.9022 7.361 3.0534z" />
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
