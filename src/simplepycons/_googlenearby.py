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


class GoogleNearbyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlenearby"

    @property
    def original_file_name(self) -> "str":
        return "googlenearby.svg"

    @property
    def title(self) -> "str":
        return "Google Nearby"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Nearby</title>
     <path d="M6.5459 12.0003L12.001 6.545l5.4541 5.4552-5.4541
 5.454zm16.9763-1.154L13.158.48a1.635 1.635 0 00-2.314 0L.4778
 10.8462a1.629 1.629 0 000 2.305L10.848 23.5226a1.629 1.629 0 002.304
 0l10.3702-10.3712a1.629 1.629 0 000-2.305zM12
 20.7263l-8.7272-8.7281L12 3.27l8.7272 8.7282z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://developers.google.com/nearby/develope'''

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
