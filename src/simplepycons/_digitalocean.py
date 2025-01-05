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


class DigitaloceanIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "digitalocean"

    @property
    def original_file_name(self) -> "str":
        return "digitalocean.svg"

    @property
    def title(self) -> "str":
        return "DigitalOcean"

    @property
    def primary_color(self) -> "str":
        return "#0080FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DigitalOcean</title>
     <path d="M12.04 0C5.408-.02.005 5.37.005 11.992h4.638c0-4.923
 4.882-8.731 10.064-6.855a6.95 6.95 0 014.147 4.148c1.889 5.177-1.924
 10.055-6.84 10.064v-4.61H7.391v4.623h4.61V24c7.86 0 13.967-7.588
 11.397-15.83-1.115-3.59-3.985-6.446-7.575-7.575A12.8 12.8 0 0012.039
 0zM7.39 19.362H3.828v3.564H7.39zm-3.563 0v-2.978H.85v2.978z" />
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
