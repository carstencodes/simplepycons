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


class GoogleCloudIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlecloud"

    @property
    def original_file_name(self) -> "str":
        return "googlecloud.svg"

    @property
    def title(self) -> "str":
        return "Google Cloud"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Cloud</title>
     <path d="M12.19 2.38a9.344 9.344 0 0 0-9.234
 6.893c.053-.02-.055.013 0 0-3.875 2.551-3.922 8.11-.247
 10.941l.006-.007-.007.03a6.717 6.717 0 0 0 4.077
 1.356h5.173l.03.03h5.192c6.687.053 9.376-8.605 3.835-12.35a9.365
 9.365 0 0 0-2.821-4.552l-.043.043.006-.05A9.344 9.344 0 0 0 12.19
 2.38zm-.358 4.146c1.244-.04 2.518.368 3.486 1.15a5.186 5.186 0 0 1
 1.862 4.078v.518c3.53-.07 3.53 5.262 0
 5.193h-5.193l-.008.009v-.04H6.785a2.59 2.59 0 0
 1-1.067-.23h.001a2.597 2.597 0 1 1 3.437-3.437l3.013-3.012A6.747
 6.747 0 0 0 8.11 8.24c.018-.01.04-.026.054-.023a5.186 5.186 0 0 1
 3.67-1.69z" />
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
