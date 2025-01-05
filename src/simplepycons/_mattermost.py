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


class MattermostIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mattermost"

    @property
    def original_file_name(self) -> "str":
        return "mattermost.svg"

    @property
    def title(self) -> "str":
        return "Mattermost"

    @property
    def primary_color(self) -> "str":
        return "#0058CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mattermost</title>
     <path d="M12.081 0C7.048-.034 2.339 3.125.637 8.153c-2.125 6.276
 1.24 13.086 7.516 15.21 6.276 2.125 13.086-1.24 15.21-7.516
 1.727-5.1-.172-10.552-4.311-13.557l.126 2.547c2.065 2.282 2.88 5.512
 1.852 8.549-1.534 4.532-6.594 6.915-11.3
 5.321-4.708-1.593-7.28-6.559-5.745-11.092 1.031-3.046 3.655-5.121
 6.694-5.67l1.642-1.94A4.87 4.87 0 0 0 12.08 0zm3.528 1.094a.284.284 0
 0 0-.123.024l-.004.001a.33.33 0 0
 0-.109.071c-.145.142-.657.828-.657.828L13.6 3.4l-1.3 1.585-2.232
 2.776s-1.024 1.278-.798 2.851c.226 1.574 1.396 2.34 2.304
 2.648.907.307 2.302.408 3.438-.704 1.135-1.112 1.098-2.75
 1.098-2.75l-.087-3.56-.07-2.05-.047-1.775s.01-.856-.02-1.057a.33.33 0
 0 0-.035-.107l-.006-.012-.007-.011a.277.277 0 0 0-.229-.14z" />
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
