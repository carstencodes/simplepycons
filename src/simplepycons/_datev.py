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


class DatevIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "datev"

    @property
    def original_file_name(self) -> "str":
        return "datev.svg"

    @property
    def title(self) -> "str":
        return "DATEV"

    @property
    def primary_color(self) -> "str":
        return "#9BD547"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DATEV</title>
     <path d="M0 .165v16.9174h23.9147V.1651Zm.017
 18.1842v5.4857h1.9809c1.4754 0 2.7429-1.1832
 2.7429-2.7005-.042-1.686-1.0982-2.7852-2.5736-2.7852zm6.62 0-2.1079
 5.4857H5.706l1.6422-4.3428 1.3546
 3.454h-1.524v.8888h3.0392l-2.1502-5.4857Zm2.6498
 0v.9312h1.7778v4.5545h1.219v-4.5545h1.727v-.9312zm5.1894
 0v5.4857h3.7926v-.8889h-2.6159v-1.5153h2.3196v-.9313h-2.3196v-1.219h2.4889v-.9312zm3.962
 0 2.1502 5.4857h1.3037L24 18.3492h-2.9037v.9312h1.3884l-1.2699
 3.327-1.5577-4.2582zm-17.2869.9312h.9313c.9271 0 1.5576.6735 1.5153
 1.8117-.042 1.1804-.8425 1.8116-1.8116 1.8116h-.635Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Datev'''

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
