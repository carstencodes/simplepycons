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


class NextcloudIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nextcloud"

    @property
    def original_file_name(self) -> "str":
        return "nextcloud.svg"

    @property
    def title(self) -> "str":
        return "Nextcloud"

    @property
    def primary_color(self) -> "str":
        return "#0082C9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nextcloud</title>
     <path d="M12.018 6.537c-2.5 0-4.6 1.712-5.241
 4.015-.56-1.232-1.793-2.105-3.225-2.105A3.569 3.569 0 0 0 0 12a3.569
 3.569 0 0 0 3.552 3.553c1.432 0 2.664-.874 3.224-2.106.641 2.304
 2.742 4.016 5.242 4.016 2.487 0 4.576-1.693 5.231-3.977.569 1.21
 1.783 2.067 3.198 2.067A3.568 3.568 0 0 0 24 12a3.569 3.569 0 0
 0-3.553-3.553c-1.416 0-2.63.858-3.199
 2.067-.654-2.284-2.743-3.978-5.23-3.977zm0 2.085c1.878 0 3.378 1.5
 3.378 3.378 0 1.878-1.5 3.378-3.378 3.378A3.362 3.362 0 0 1 8.641
 12c0-1.878 1.5-3.378 3.377-3.378zm-8.466 1.91c.822 0 1.467.645 1.467
 1.468s-.644 1.467-1.467 1.468A1.452 1.452 0 0 1 2.085
 12c0-.823.644-1.467 1.467-1.467zm16.895 0c.823 0 1.468.645 1.468
 1.468s-.645 1.468-1.468 1.468A1.452 1.452 0 0 1 18.98
 12c0-.823.644-1.467 1.467-1.467z" />
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
