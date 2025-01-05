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


class ElasticCloudIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "elasticcloud"

    @property
    def original_file_name(self) -> "str":
        return "elasticcloud.svg"

    @property
    def title(self) -> "str":
        return "Elastic Cloud"

    @property
    def primary_color(self) -> "str":
        return "#005571"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Elastic Cloud</title>
     <path d="M13.318 0c-6.628 0-12 5.372-12 12 0 2.008.495 3.9 1.368
 5.563a14.299 14.299 0 0 1 5.09-3.664c.307-.13.624-.22.948-.28A4.842
 4.842 0 0 1 8.443 12a4.875 4.875 0 0 1 7.494-4.11 2.218 2.218 0 0 0
 2.055.164 12.047 12.047 0 0 0 4.69-3.554A11.975 11.975 0 0 0 13.318
 0zM9.426 15.77c-.266.01-.531.069-.783.175a12.044 12.044 0 0 0-4.69
 3.555c2.2 2.742 5.576 4.5 9.365 4.5 3.789 0 7.165-1.758
 9.364-4.5a12.048 12.048 0 0 0-4.69-3.555 2.217 2.217 0 0 0-2.055.165
 4.845 4.845 0 0 1-2.62.765 4.846 4.846 0 0 1-2.618-.765 2.193 2.193 0
 0 0-1.273-.34z" />
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
