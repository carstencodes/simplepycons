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


class HeadphoneZoneIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "headphonezone"

    @property
    def original_file_name(self) -> "str":
        return "headphonezone.svg"

    @property
    def title(self) -> "str":
        return "Headphone Zone"

    @property
    def primary_color(self) -> "str":
        return "#3C07FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Headphone Zone</title>
     <path d="M17.63 4.702 17.96 0 9.086 2.484c-.463 1.754-.694
 4.139.133 6.655.232-.067.463-.1.695-.133a4.724 4.724 0 0 1 5.133
 4.305 4.724 4.724 0 0 1-4.305 5.133 4.724 4.724 0 0 1-5.132-4.305
 4.618 4.618 0 0 1 1.159-3.543c-.86-1.325-1.987-3.609-1.954-6.49C1.107
 6.623-.847 11.258.378 15.86c1.49 5.828 7.45 9.305 13.245 7.782
 4.603-1.192 7.748-5.198 8.113-9.702l2.251-1.622-6.358-7.616Z" />
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
